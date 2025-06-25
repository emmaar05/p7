from PySide6.QtWidgets import (QMainWindow, QDialog, QFileDialog, 
                              QMessageBox, QApplication, QInputDialog)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Qt
from conectar_ui import Ui_Dialog
from Iniciar_sesion_ui import Ui_Mensajeria
from Mensajeria_ui import Ui_MainWindow
import sys
import socket
import os
#======Clases de Chat=======
class PrivChat():
    def __init__(self, idx, nme) -> None:
        self.chname = nme
        self.idx = idx
#======Hilo para el Socket=======
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
#======Ventana Principal=====
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Configuración inicial
        self.setWindowTitle("Windows Live Messenger - Desconectado")
        self.connection = None
        self.current_user = None
        self.user_image = "Usuario_sin_registrar.png"
        self.private_chats = []  # Lista de chats privados
        self.current_chat = None  # Chat actual (None para chat general)
        
        # Conectar señales
        self.Boton_Enviar.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)
       # self.Boton_Perfil.clicked.connect(self.show_profile)
        self.Boton_ChatG.clicked.connect(lambda: self.show_chat("General"))
        self.Boton_NuevoChat.clicked.connect(self.new_chat)
        #self.Boton_Grupos.clicked.connect(self.show_groups)
        #self.pushButton_5.clicked.connect(self.show_apps)
        
        # Mostrar ventana de login primero
        self.show_login_window()

    def show_login_window(self):
        self.login_window = LoginWindow(self)
        self.login_window.show()
        self.hide()

    def setup_ui_connections(self):
        """Configura las conexiones de la UI después del login"""
        # Mostrar imagen de usuario
        self.label_6.setPixmap(QPixmap(self.user_image).scaled(
            self.label_6.width(), self.label_6.height(), 
            Qt.AspectRatioMode.KeepAspectRatio))
        
        # Configurar botones de la barra lateral
        self.Boton_Perfil.clicked.connect(self.show_profile)
        self.Boton_ChatG.clicked.connect(lambda: self.show_chat("General"))
        self.Boton_NuevoChat.clicked.connect(self.new_chat)
        self.Boton_Grupos.clicked.connect(self.show_groups)
        self.pushButton_5.clicked.connect(self.show_apps)

    def connect_to_server(self, host, port):
        """Establece conexión con el servidor"""
        try:
            self.connection = ThreadSocket(host, int(port), self.current_user)
            self.connection.signal_message.connect(self.receive_message)
            self.connection.start()
            
            # Actualizar interfaz
            self.setWindowTitle(f"Windows Live Messenger - Conectado como {self.current_user}")
            self.label_5.setText(f"Hola: {self.current_user}!")
            self.plainTextEdit.appendPlainText(f"Conectado al servidor {host}:{port}\n")
            return True
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar: {str(e)}")
            return False

    def send_message(self):
        """Envía un mensaje al servidor"""
        if not (self.connection and self.connection.connected):
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
            
        message = self.lineEdit.text().strip()
        if not message:
            return
            
        try:
            if self.current_chat:
                # Enviar mensaje privado
                full_msg = f"<private>{self.current_chat.chname}:{message}"
                self.connection.server.send(bytes(full_msg, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú a {self.current_chat.chname}> {message}\n")
            else:
                # Enviar mensaje público
                self.connection.server.send(bytes(message, 'utf-8'))
                self.plainTextEdit.appendPlainText(f"<Tú> {message}\n")
                
            self.lineEdit.clear()
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"<!!error al enviar!!> {str(e)}\n")

    def receive_message(self, message):
        """Maneja los mensajes entrantes"""
        if message.startswith("Usuarios conectados:"):
            # Respuesta al comando 'list'
            users = message.split("\n")[1:]  # Saltar línea de encabezado
            users = [u.strip() for u in users if u.strip() and u.strip() != self.current_user]
            
            if not users:
                QMessageBox.information(self, "Nuevo Chat", "No hay otros usuarios conectados")
                return
                
            # Mostrar diálogo de selección de usuario
            user, ok = QInputDialog.getItem(
                self, "Nuevo Chat Privado", 
                "Selecciona un usuario:", 
                users, 0, False)
                
            if ok and user:
                self.start_private_chat(user)
        else:
            # Manejo normal de mensajes
            self.plainTextEdit.appendPlainText(message)
        
    def start_private_chat(self, username):
        """Inicia un nuevo chat privado"""
        # Verificar si ya existe un chat con este usuario
        for chat in self.private_chats:
            if chat.chname == username:
                self.current_chat = chat
                self.plainTextEdit.clear()
                self.plainTextEdit.appendPlainText(f"Chat privado con {username}:\n")
                return
                
        # Crear nuevo chat privado
        new_chat = PrivChat(len(self.private_chats), username)
        self.private_chats.append(new_chat)
        self.current_chat = new_chat
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(f"Iniciando chat privado con {username}...\n")
        
        # Notificar al servidor
        try:
            self.connection.server.send(bytes(f"<private>{username}", 'utf-8'))
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Error al iniciar chat privado: {str(e)}\n")

    def new_chat(self):
        """Muestra diálogo para nuevo chat privado"""
        if not self.connection or not self.connection.connected:
            QMessageBox.warning(self, "Error", "No estás conectado al servidor")
            return
            
        # Solicitar lista de usuarios al servidor
        try:
            self.connection.server.send(bytes("<command>list", 'utf-8'))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo obtener la lista de usuarios: {str(e)}")

class LoginWindow(QMainWindow, Ui_Mensajeria):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Windows Live Messenger - Iniciar sesión")
        self.parent_window = parent
        self.profile_image = None
        
        # Conectar botones
        self.pushButton.clicked.connect(self.select_profile_image)
        self.pushButton_2.clicked.connect(self.handle_login)

    def select_profile_image(self):
        """Permite al usuario seleccionar una imagen de perfil"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.profile_image = file_name
            self.Foto_usuario.setPixmap(QPixmap(file_name).scaled(
                self.Foto_usuario.width(), self.Foto_usuario.height(),
                Qt.AspectRatioMode.KeepAspectRatio))

    def handle_login(self):
        """Maneja el proceso de inicio de sesión"""
        username = self.textEdit.toPlainText().strip()
        if not username:
            QMessageBox.warning(self, "Error", "Debe ingresar un nombre de usuario")
            return
            
        # Configurar usuario en la ventana principal
        self.parent_window.current_user = username
        self.parent_window.user_image = self.profile_image or "Usuario_sin_registrar.png"
        
        # Mostrar diálogo de conexión
        dialog = ConnectDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            host = dialog.txtServer.text().strip()
            port = dialog.txtPort.text().strip()
            
            if host and port.isdigit():
                if self.parent_window.connect_to_server(host, int(port)):
                    self.close()
                    self.parent_window.show()
            else:
                QMessageBox.warning(self, "Error", "Datos de conexión inválidos")

class ConnectDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Configuración de conexión")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())