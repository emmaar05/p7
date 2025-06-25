import socket
import threading
from datetime import datetime

class Client:
    def __init__(self, conn, addr):
        self.name = ""
        self.conn = conn
        self.addr = addr
        self.join_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_chat = None  # Para rastrear chats privados

class ChatServer:
    def __init__(self, host="0.0.0.0", port=65535):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.running = False
        
    def start(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(100)
            self.running = True
            print(f"Servidor escuchando en {self.host}:{self.port}")
            
            while self.running:
                conn, addr = self.server.accept()
                client = Client(conn, addr)
                self.clients.append(client)
                print(f"Nuevo cliente conectado: {addr}")
                
                threading.Thread(
                    target=self.client_handler,
                    args=(client,),
                    daemon=True
                ).start()
                
        except KeyboardInterrupt:
            print("\nDeteniendo servidor...")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            self.stop()
            
    def stop(self):
        self.running = False
        for client in self.clients:
            client.conn.close()
        self.server.close()
        print("Servidor detenido")
        
    def client_handler(self, client):
        try:
            client.conn.send(bytes("Bienvenido al Windows Live Messenger Server!\n", 'utf-8'))
            
            while self.running:
                message = client.conn.recv(1024)
                if not message:
                    break
                    
                msg = message.decode('utf-8')
                print(f"<{client.addr[0]}> {msg}")
                
                # Comandos especiales
                if msg.startswith('<name>'):
                    client.name = msg.removeprefix('<name>')
                    self.broadcast(f"{client.name} se ha unido al chat\n", client)
                elif msg.startswith('<command>'):
                    self.handle_command(msg, client)
                elif msg.startswith('<private>'):
                    # Manejar mensaje privado
                    parts = msg.removeprefix('<private>').split(':', 1)
                    if len(parts) == 2:
                        recipient, private_msg = parts
                        self.send_private(client, recipient, private_msg)
                    else:
                        # Solo el nombre del destinatario - iniciando chat privado
                        recipient = parts[0]
                        client.conn.send(bytes(f"Chat privado con {recipient} iniciado\n", 'utf-8'))
                else:
                    # Mensaje normal
                    sender_name = client.name if client.name else str(client.addr)
                    if client.current_chat:
                        # Enviar solo al chat privado
                        self.send_private(client, client.current_chat, msg)
                    else:
                        # Transmitir a todos
                        self.broadcast(f"<{sender_name}> {msg}\n", client)
                    
        except Exception as e:
            print(f"Error con cliente {client.addr}: {str(e)}")
        finally:
            self.remove_client(client)
            
    def broadcast(self, message, sender):
        """Envía un mensaje a todos los clientes excepto al remitente"""
        for client in self.clients:
            if client.conn != sender.conn and not client.current_chat:
                try:
                    client.conn.send(bytes(message, 'utf-8'))
                except:
                    self.remove_client(client)
                    
    def send_private(self, sender, recipient_name, message):
        """Envía mensaje privado a usuario específico"""
        for client in self.clients:
            if client.name == recipient_name:
                try:
                    sender_name = sender.name if sender.name else str(sender.addr)
                    msg = f"[PRIVADO de {sender_name}] {message}\n"
                    client.conn.send(bytes(msg, 'utf-8'))
                    # Enviar confirmación al remitente
                    sender.conn.send(bytes(f"[PRIVADO a {recipient_name}] {message}\n", 'utf-8'))
                    return True
                except:
                    self.remove_client(client)
        return False
            
    def handle_command(self, command, client):
        """Maneja comandos especiales del cliente"""
        cmd = command.removeprefix('<command>')
        if cmd == "list":
            users = "\n".join([c.name or str(c.addr) for c in self.clients])
            client.conn.send(bytes(f"Usuarios conectados:\n{users}\n", 'utf-8'))
            
    def remove_client(self, client):
        """Elimina un cliente de la lista y notifica a los demás"""
        if client in self.clients:
            self.clients.remove(client)
            if client.name:
                self.broadcast(f"{client.name} ha abandonado el chat\n", client)
            print(f"Cliente desconectado: {client.addr}")
            client.conn.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()