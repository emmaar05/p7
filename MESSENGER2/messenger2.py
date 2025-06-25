from PySide6.QtWidgets import (
    QMainWindow, QDialog, QFileDialog, QMessageBox, QApplication, QInputDialog,
    QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QDialogButtonBox, QLineEdit
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Qt, QPoint, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtUiTools import QUiLoader

from Iniciar_sesion_ui import Ui_Mensajeria
from Mensajeria_ui import Ui_MainWindow
from MiPeril_ui import Ui_miperfil
from Apps_ui import Ui_Apps

import sys
import socket
import os
import random
import time

class PrivChat():
    def __init__(self, idx, nme) -> None:
        self.name = nme
        self.idx = idx
        self.messages = []

class GroupChat():
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.messages = []

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
        self.general_chat_messages = []
        self.pending_user_list_action = None

        self.Boton_Enviar.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)
        self.Boton_ChatG.clicked.connect(self.show_general_chat)
        self.Boton_NuevoChat.clicked.connect(self.new_private_chat)
        self.Boton_Perfil.clicked.connect(self.show_profile)
        self.pushButton_5.clicked.connect(self.show_apps)
        self.Boton_Zumbido.clicked.connect(self.send_buzz)
        self.Boton_Grupos.clicked.connect(self.create_new_group)
        self.Boton_Grupos_2.clicked.connect(self.select_group_to_chat)
        self.Boton_Grupos_3.clicked.connect(self.leave_group)

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
            self.general_chat_messages.append(f"Conectado al servidor {host}:{port}\n")
            self.show_general_chat()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar: {str(e)}")
            return False

    def show_general_chat(self):
        self.current_chat = None
        self.plainTextEdit.clear()
        for msg in self.general_chat_messages:
            self.plainTextEdit.appendPlainText(msg)
        self.plainTextEdit.appendPlainText("--- Chat General (todos los usuarios) ---\n")

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
                    full_msg = f"<private>{self.current_chat.name}:{message}"
                    self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.name}> {message}\n")
                    self.current_chat.messages.append(f"<Tú> {message}\n")
                elif isinstance(self.current_chat, GroupChat):
                    full_msg = f"<group>{self.current_chat.name}:{message}"
                    self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.name}> {message}\n")
                    self.current_chat.messages.append(f"<Tú> {message}\n")
                self.connection.server.send(bytes(full_msg, 'utf-8'))
            else:
                self.connection.server.send(bytes(message, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú> {message}\n")
                self.general_chat_messages.append(f"<Tú> {message}\n")
            self.lineEdit.clear()
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"<!!error al enviar!!> {str(e)}\n")

    def send_buzz(self):
        if not (self.connection and self.connection.connected):
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return

        try:
            if self.current_chat:
                if isinstance(self.current_chat, PrivChat):
                    full_msg = f"<private_buzz>{self.current_chat.name}: Zumbido!"
                    self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.name}> Zumbido!\n")
                    self.current_chat.messages.append(f"<Tú> Zumbido!\n")
                elif isinstance(self.current_chat, GroupChat):
                    full_msg = f"<group_buzz>{self.current_chat.name}: Zumbido!"
                    self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.name}> Zumbido!\n")
                    self.current_chat.messages.append(f"<Tú> Zumbido!\n")
                self.connection.server.send(bytes(full_msg, 'utf-8'))
            else:
                full_msg = f"<buzz_general>{self.current_user} envió un zumbido general!"
                self.connection.server.send(bytes(full_msg, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú> Zumbido!\n")
                self.general_chat_messages.append(f"<Tú> Zumbido!\n")
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"<!!error al enviar zumbido!!> {str(e)}\n")

    def create_new_group(self):
        if not self.connection or not self.connection.connected:
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
        self.pending_user_list_action = 'group_creation'
        try:
            self.connection.server.send(bytes("<command>list", 'utf-8'))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo obtener la lista de usuarios: {str(e)}")
            
    def select_group_to_chat(self):
        if not self.group_chats:
            QMessageBox.information(self, "Grupos", "No perteneces a ningún grupo")
            return
        
        group_names = [group.name for group in self.group_chats]
        group_name, ok = QInputDialog.getItem(
            self, "Seleccionar Grupo", "Grupos disponibles:", group_names, 0, False)
        
        if ok and group_name:
            for group in self.group_chats:
                if group.name == group_name:
                    self.current_chat = group
                    self.plainTextEdit.clear()
                    for msg in group.messages:
                        self.plainTextEdit.appendPlainText(msg)
                    self.plainTextEdit.appendPlainText(f"Chat grupal: {group_name}\n")
                    break

    def leave_group(self):
        if not self.group_chats:
            QMessageBox.information(self, "Grupos", "No perteneces a ningún grupo")
            return
        
        group_names = [group.name for group in self.group_chats]
        group_name, ok = QInputDialog.getItem(
            self, "Salir de Grupo", "Selecciona un grupo para salir:", group_names, 0, False)
        
        if ok and group_name:
            try:
                self.connection.server.send(bytes(f"<leave_group>{group_name}", 'utf-8'))
                self.group_chats = [g for g in self.group_chats if g.name != group_name]
                
                if self.current_chat and isinstance(self.current_chat, GroupChat) and self.current_chat.name == group_name:
                    self.show_general_chat()
                
                QMessageBox.information(self, "Grupo", f"Has salido del grupo '{group_name}'")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo salir del grupo: {str(e)}")

    def new_private_chat(self):
        if not self.connection or not self.connection.connected:
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
        self.pending_user_list_action = 'private_chat'
        try:
            self.connection.server.send(bytes("<command>list", 'utf-8'))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo obtener la lista de usuarios: {str(e)}")

    def receive_message(self, message):
        message = message.strip()
        
        if message.startswith("Usuarios conectados:"):
            users = message.split("\n")[1:]
            users = [u.strip() for u in users if u.strip() and u.strip() != self.current_user]

            if not users:
                QMessageBox.information(self, "Usuarios", "No hay otros usuarios conectados")
                return

            if self.pending_user_list_action == 'private_chat':
                user, ok = QInputDialog.getItem(
                    self, "Seleccionar Usuario", "Usuarios disponibles:", users, 0, False)
                if ok and user:
                    self.start_private_chat(user)

            elif self.pending_user_list_action == 'group_creation':
                dialog = MultiSelectDialog(users)
                if dialog.exec() == QDialog.Accepted:
                    selected = dialog.get_selected_users()
                    if not selected:
                        return

                    group_name, ok = QInputDialog.getText(
                        self, "Nombre del Grupo", "Ingrese el nombre del grupo:")

                    if ok and group_name:
                        self.start_group_chat(group_name, selected)
                        try:
                            self.connection.server.send(bytes(f"<create_group>{group_name}", 'utf-8'))
                            for member in selected:
                                self.connection.server.send(bytes(f"<add_to_group>{group_name}:{member}", 'utf-8'))
                            self.connection.server.send(bytes(f"<add_to_group>{group_name}:{self.current_user}", 'utf-8'))
                        except Exception as e:
                            QMessageBox.critical(self, "Error", f"No se pudo crear el grupo: {str(e)}")

            self.pending_user_list_action = None

        elif message.startswith("<group_created>"):
            QMessageBox.information(self, "Grupo", f"Grupo '{message.removeprefix('<group_created>')}' creado exitosamente")
        
        elif message.startswith("<joined_group>"):
            parts = message.removeprefix("<joined_group>").split(":")
            group_name = parts[0]
            members = parts[1].split(",") if len(parts) > 1 else []
            self.start_group_chat(group_name, members)
        
        elif message.startswith("<left_group>"):
            group_name = message.removeprefix("<left_group>")
            self.group_chats = [g for g in self.group_chats if g.name != group_name]
            if self.current_chat and isinstance(self.current_chat, GroupChat) and self.current_chat.name == group_name:
                self.show_general_chat()
        
        elif message.startswith("[ZUMBIDO PRIVADO de "):
            self.plainTextEdit.appendPlainText(message)
            self.shake_window()
            
        elif message.startswith("[ZUMBIDO GRUPO "):
            self.plainTextEdit.appendPlainText(message)
            self.shake_window()
        
        elif message.startswith("[ZUMBIDO GENERAL de "):
            self.plainTextEdit.appendPlainText(message)
            self.shake_window()
        
        elif message.startswith("[PRIVADO de "):
            parts = message.split(" ", 3)
            print(parts)
            
            if len(parts) >= 4:
                sender = parts[2]
                msg_content = parts[3]
                
                chat_exists = False
                print(len(self.private_chats))
                for chat in self.private_chats:
                    print(chat.name)
                    if chat.name == sender:
                        chat.messages.append(message)
                        chat_exists = True
                        if self.current_chat == chat:
                            self.plainTextEdit.appendPlainText(message)
                        break
                
                if not chat_exists:
                    new_chat = PrivChat(len(self.private_chats), sender)
                    new_chat.messages.append(message)
                    self.private_chats.append(new_chat)
                    if self.current_chat == new_chat:
                        self.plainTextEdit.appendPlainText(message)
        
        elif message.startswith("[GRUPO "):
            parts = message.split(" ", 2)
            if len(parts) >= 3:
                group_name = parts[1].rstrip(" -").rstrip("]")
                msg_content = parts[2]
                
                for group in self.group_chats:
                    if group.name == group_name:
                        group.messages.append(message)
                        if self.current_chat == group:
                            self.plainTextEdit.appendPlainText(message)
                        break
        
        else:
            self.general_chat_messages.append(message)
            if self.current_chat is None:
                self.plainTextEdit.appendPlainText(message)

    def shake_window(self):
        original_pos = self.pos()
        sound = QSoundEffect()
        sound.setSource(QUrl.fromLocalFile("buzz.wav"))
        sound.setLoopCount(1)
        sound.setVolume(0.9)
        sound.play()

        for _ in range(10):
            offset = QPoint(random.randint(-10, 10), random.randint(-10, 10))
            self.move(original_pos + offset)
            QApplication.processEvents()
            time.sleep(0.02)

        self.move(original_pos)

    def start_private_chat(self, username):
        for chat in self.private_chats:
            if chat.name == username:
                self.current_chat = chat
                self.plainTextEdit.clear()
                for msg in chat.messages:
                    self.plainTextEdit.appendPlainText(msg)
                self.plainTextEdit.appendPlainText(f"Reunido con {username}...\n")
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
        for chat in self.group_chats:
            if chat.name == group_name:
                self.current_chat = chat
                self.plainTextEdit.clear()
                for msg in chat.messages:
                    self.plainTextEdit.appendPlainText(msg)
                self.plainTextEdit.appendPlainText(f"Reunido con grupo '{group_name}'\n")
                return
        
        new_group = GroupChat(group_name, members)
        self.group_chats.append(new_group)
        self.current_chat = new_group
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f"Grupo '{group_name}' creado con: {', '.join(members)}\n")

    def show_profile(self):
        self.hide()  
        self.profile_window = ProfileWindow(self.current_user, self.user_image, self)
        self.profile_window.show()

    def show_apps(self):
        self.apps_window = AppsWindow()
        self.apps_window.exec()

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
        
        if self.parent_window.connect_to_server("127.0.0.1", 65535):
            self.close()
            self.parent_window.show()

class ProfileWindow(QMainWindow):
    def __init__(self, username, image_path, main_window):
        super().__init__()
        self.ui = Ui_miperfil()
        self.ui.setupUi(self)
        self.setWindowTitle("Mi Perfil")
        self.main_window = main_window

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())