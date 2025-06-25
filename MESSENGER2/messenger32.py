from PySide6.QtWidgets import (
    QMainWindow, QDialog, QFileDialog, QMessageBox, QApplication, QInputDialog,
    QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QDialogButtonBox, QLineEdit
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Qt, QFile
from PySide6.QtUiTools import QUiLoader

from Iniciar_sesion_ui import Ui_Mensajeria
from Mensajeria_ui import Ui_MainWindow
from MiPeril_ui import Ui_miperfil
from Apps_ui import Ui_Apps

import sys
import socket
import os

# ==== Clases de Chats ====
class PrivChat():
    def __init__(self, idx, nme) -> None:
        self.chname = nme
        self.idx = idx

class GroupChat():
    def __init__(self, name, members):
        self.name = name
        self.members = members

# ==== Hilo para el Socket ====
class ThreadSocket(QThread):
    signal_message = Signal(str)
    
    def __init__(self, host, port, name, parent=None):
        super().__init__(parent)
        self.host = host
        self.port = port
        self.name = name
        self.connected = False
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.server.connect((self.host, self.port))
            self.connected = True
            self.server.send(bytes(f"<name>{self.name}", 'utf-8'))
            
            while self.connected:
                message = self.server.recv(1024)
                if message:
                    self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconnected!!>")
                    break
        except Exception as e:
            self.signal_message.emit(f"<!!error!!> {str(e)}")
        finally:
            self.server.close()
            self.connected = False
        
    def stop(self):
        self.connected = False
        self.wait()

# ==== Ventana Principal ====
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Windows Live Messenger - Desconectado")
        self.connection = None
        self.current_user = None
        self.user_image = "Usuario_sin_registrar.png"
        self.private_chats = []
        self.group_chats = []
        self.current_chat = None
        
        self.Boton_Enviar.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)
        self.Boton_ChatG.clicked.connect(lambda: self.show_chat("General"))
        self.Boton_NuevoChat.clicked.connect(self.new_chat)
        self.Boton_Perfil.clicked.connect(self.show_profile)
        self.pushButton_5.clicked.connect(self.show_apps)
        
        self.show_login_window()

    def show_login_window(self):
        self.login_window = LoginWindow(self)
        self.login_window.show()
        self.hide()

    def connect_to_server(self, host, port):
        try:
            self.connection = ThreadSocket(host, int(port), self.current_user)
            self.connection.signal_message.connect(self.receive_message)
            self.connection.start()
            self.setWindowTitle(f"Windows Live Messenger - Conectado como {self.current_user}")
            self.label_5.setText(f"Hola: {self.current_user}!")
            self.plainTextEdit.appendPlainText(f"Conectado al servidor {host}:{port}\n")
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar: {str(e)}")
            return False

    def send_message(self):
        if not (self.connection and self.connection.connected):
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
        message = self.lineEdit.text().strip()
        if not message:
            return
        try:
            if self.current_chat:
                if isinstance(self.current_chat, PrivChat):
                    full_msg = f"<private>{self.current_chat.chname}:{message}"
                elif isinstance(self.current_chat, GroupChat):
                    full_msg = f"<group>{self.current_chat.name}:{message}"
                self.connection.server.send(bytes(full_msg, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.name}> {message}\n")
            else:
                self.connection.server.send(bytes(message, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú> {message}\n")
            self.lineEdit.clear()
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"<!!error al enviar!!> {str(e)}\n")

    def receive_message(self, message):
        if message.startswith("Usuarios conectados:"):
            users = message.split("\n")[1:]
            users = [u.strip() for u in users if u.strip() and u.strip() != self.current_user]

            if not users:
                QMessageBox.information(self, "Nuevo Chat", "No hay otros usuarios conectados")
                return

            dialog = MultiSelectDialog(users)
            if dialog.exec() == QDialog.Accepted:
                selected = dialog.get_selected_users()
                if len(selected) == 1:
                    self.start_private_chat(selected[0])
                else:
                    group_name, ok = QInputDialog.getText(self, "Nombre del Grupo", "Ingrese el nombre del grupo:")
                    if ok and group_name:
                        self.start_group_chat(group_name, selected)
        else:
            self.plainTextEdit.appendPlainText(message)

    def start_private_chat(self, username):
        for chat in self.private_chats:
            if chat.chname == username:
                self.current_chat = chat
                self.plainTextEdit.clear()
                self.plainTextEdit.appendPlainText(f"Chat privado con {username}:\n")
                return
        new_chat = PrivChat(len(self.private_chats), username)
        self.private_chats.append(new_chat)
        self.current_chat = new_chat
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f"Iniciando chat privado con {username}...\n")
        try:
            self.connection.server.send(bytes(f"<private>{username}", 'utf-8'))
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Error al iniciar chat privado: {str(e)}\n")

    def start_group_chat(self, group_name, members):
        new_group = GroupChat(group_name, members)
        self.group_chats.append(new_group)
        self.current_chat = new_group
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f"Iniciando grupo '{group_name}' con: {', '.join(members)}\n")
        try:
            self.connection.server.send(bytes(f"<group>{group_name}", 'utf-8'))
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Error al iniciar grupo: {str(e)}\n")

    def new_chat(self):
        if not self.connection or not self.connection.connected:
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
        try:
            self.connection.server.send(bytes("<command>list", 'utf-8'))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo obtener la lista de usuarios: {str(e)}")

    def show_chat(self, chat_type):
        if chat_type == "General":
            self.current_chat = None
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText("Chat general:\n")

    def show_profile(self):
        self.hide()  
        self.profile_window = ProfileWindow(self.current_user, self.user_image, self)
        self.profile_window.show()

    def show_apps(self):
        self.apps_window = AppsWindow()
        self.apps_window.exec()

# ==== Login ====
class LoginWindow(QMainWindow, Ui_Mensajeria):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Windows Live Messenger - Iniciar sesión")
        self.parent_window = parent
        self.profile_image = None
        
        self.pushButton.clicked.connect(self.select_profile_image)
        self.pushButton_2.clicked.connect(self.handle_login)

    def select_profile_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.profile_image = file_name
            self.Foto_usuario.setPixmap(QPixmap(file_name).scaled(
                self.Foto_usuario.width(), self.Foto_usuario.height(),
                Qt.AspectRatioMode.KeepAspectRatio))

    def handle_login(self):
        username = self.textEdit.toPlainText().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Debe ingresar un nombre de usuario")
            return
            
        self.parent_window.current_user = username
        self.parent_window.user_image = self.profile_image or "Usuario_sin_registrar.png"
        
        # Conexión directa al servidor local
        if self.parent_window.connect_to_server("127.0.0.1", 65535):
            self.close()
            self.parent_window.show()

# ==== Ventana de Perfil ====
class ProfileWindow(QMainWindow):
    def __init__(self, username, image_path, main_window):
        super().__init__()
        self.ui = Ui_miperfil()
        self.ui.setupUi(self)
        self.setWindowTitle("Mi Perfil")

        self.main_window = main_window  # guardamos referencia a MainWindow

        self.ui.label_nombre.setText(username)
        self.ui.label_imagen.setPixmap(QPixmap(image_path).scaled(
            self.ui.label_imagen.width(), self.ui.label_imagen.height(),
            Qt.AspectRatioMode.KeepAspectRatio))

        self.ui.Boton_Salir.clicked.connect(self.salir_aplicacion)
        self.ui.Boton_RegresarM.clicked.connect(self.regresar_mensajeria)

    def salir_aplicacion(self):
        QApplication.quit()

    def regresar_mensajeria(self):
        self.close()
        self.main_window.show()

# ==== Ventana de Aplicaciones ====
class AppsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Apps()
        self.ui.setupUi(self)
        self.setWindowTitle("Aplicaciones")

        self.ui.Boton_Ajedrez.clicked.connect(self.Abrir_Ajedrez)
        self.ui.Boton_Gato.clicked.connect(self.Abrir_Gato)
        self.ui.Boton_Batimovil.clicked.connect(self.Abrir_Batimovil)
        self.ui.Boton_Regresar.clicked.connect(self.close)

    def Abrir_Ajedrez(self):
        os.system("python path/to/ajedrez_pygame.py")

    def Abrir_Gato(self):
        os.system("python path/to/gato.py")

    def Abrir_Batimovil(self):
        os.system("python path/to/Batimovil.py")

# ==== MultiSelect para Grupos ====
class MultiSelectDialog(QDialog):
    def __init__(self, user_list):
        super().__init__()
        self.setWindowTitle("Seleccionar Usuarios")
        self.layout = QVBoxLayout(self)
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        for user in user_list:
            item = QListWidgetItem(user)
            self.list_widget.addItem(item)
        self.layout.addWidget(self.list_widget)
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def get_selected_users(self):
        return [item.text() for item in self.list_widget.selectedItems()]

# ==== Main ====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())