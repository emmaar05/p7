import socket
import threading
from datetime import datetime

class Client:
    def __init__(self, conn, addr):
        self.name = ""
        self.conn = conn
        self.addr = addr
        self.join_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.groups = set()

class ChatServer:
    def __init__(self, host="0.0.0.0", port=65535):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.groups = {}
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
            client.conn.send(b"Bienvenido al Windows Live Messenger Server!\n")

            while self.running:
                message = client.conn.recv(1024)
                if not message:
                    break

                msg = message.decode('utf-8').strip()
                print(f"<{client.addr[0]}> {msg}")

                if msg.startswith('<name>'):
                    client.name = msg.removeprefix('<name>')
                    self.broadcast(f"{client.name} se ha unido al chat\n", client)

                elif msg.startswith('<command>'):
                    self.handle_command(msg, client)

                elif msg.startswith('<create_group>'):
                    group_name = msg.removeprefix('<create_group>')
                    if group_name in self.groups:
                        client.conn.send(f"<error>El grupo '{group_name}' ya existe\n".encode())
                    else:
                        self.groups[group_name] = []
                        client.conn.send(f"<group_created>{group_name}\n".encode())

                elif msg.startswith('<add_to_group>'):
                    parts = msg.removeprefix('<add_to_group>').split(':', 1)
                    if len(parts) == 2:
                        group_name, member_name = parts
                        if group_name in self.groups:
                            if member_name not in self.groups[group_name]:
                                self.groups[group_name].append(member_name)
                                for c in self.clients:
                                    if c.name == member_name:
                                        c.groups.add(group_name)
                                        c.conn.send(f"<joined_group>{group_name}:{','.join(self.groups[group_name])}\n".encode())
                                        break
                            client.conn.send(f"<added_to_group>{group_name}:{member_name}\n".encode())
                        else:
                            client.conn.send(f"<error>El grupo '{group_name}' no existe\n".encode())

                elif msg.startswith('<leave_group>'):
                    group_name = msg.removeprefix('<leave_group>')
                    if group_name in self.groups and client.name in self.groups[group_name]:
                        self.groups[group_name].remove(client.name)
                        client.groups.discard(group_name)
                        client.conn.send(f"<left_group>{group_name}\n".encode())
                        for member in self.groups[group_name]:
                            for c in self.clients:
                                if c.name == member:
                                    c.conn.send(f"<group_notice>{group_name}:{client.name} ha abandonado el grupo\n".encode())
                        if not self.groups[group_name]:
                            del self.groups[group_name]
                    else:
                        client.conn.send(f"<error>No perteneces al grupo '{group_name}'\n".encode())

                elif msg.startswith('<group>'):
                    parts = msg.removeprefix('<group>').split(':', 1)
                    if len(parts) == 2:
                        group_name, group_msg = parts
                        self.send_group_message(client, group_name, group_msg)

                elif msg.startswith('<private>'):
                    parts = msg.removeprefix('<private>').split(':', 1)
                    if len(parts) == 2:
                        recipient, private_msg = parts
                        self.send_private(client, recipient, private_msg)
                    else:
                        recipient = parts[0]
                        client.conn.send(f"Chat privado con {recipient} iniciado\n".encode())

                elif msg.startswith('<private_buzz>'):
                    parts = msg.removeprefix('<private_buzz>').split(':', 1)
                    if len(parts) == 2:
                        recipient, buzz_msg = parts
                        self.send_private_buzz(client, recipient, buzz_msg)

                elif msg.startswith('<group_buzz>'):
                    parts = msg.removeprefix('<group_buzz>').split(':', 1)
                    if len(parts) == 2:
                        group, buzz_msg = parts
                        self.send_group_buzz(client, group, buzz_msg)

                elif msg.startswith('<buzz_general>'):
                    buzz_msg = msg.removeprefix('<buzz_general>')
                    self.broadcast(f"[ZUMBIDO GENERAL de {client.name}] {buzz_msg}\n", client)

                else:
                    sender_name = client.name or str(client.addr)
                    self.broadcast(f"<{sender_name}> {msg}\n", client)

        except Exception as e:
            print(f"Error con cliente {client.addr}: {str(e)}")
            self.remove_client(client)
        finally:
            self.remove_client(client)

    def broadcast(self, message, sender):
        for client in self.clients:
            if client.conn != sender.conn:
                try:
                    client.conn.send(message.encode())
                except Exception:
                    self.remove_client(client)

    def send_private(self, sender, recipient_name, message):
        for client in self.clients:
            if client.name == recipient_name:
                try:
                    msg = f"[PRIVADO de {sender.name} {message}\n"
                    client.conn.send(msg.encode())
                    sender.conn.send(f"[PRIVADO a {recipient_name}] {message}\n".encode())
                    return True
                except Exception:
                    self.remove_client(client)
        return False

    def send_group_message(self, sender, group_name, message):
        if group_name not in self.groups:
            sender.conn.send(f"El grupo '{group_name}' no existe\n".encode())
            return False

        msg = f"[GRUPO {group_name} - {sender.name}] {message}\n"
        for member_name in self.groups[group_name]:
            for client in self.clients:
                if client.name == member_name:  # Enviar a todos los miembros incluido el remitente
                    try:
                        client.conn.send(msg.encode())
                    except Exception:
                        self.remove_client(client)
        return True

    def send_private_buzz(self, sender, recipient_name, buzz_msg):
        for client in self.clients:
            if client.name == recipient_name:
                try:
                    msg = f"[ZUMBIDO PRIVADO de {sender.name}] {buzz_msg}\n"
                    client.conn.send(msg.encode())
                    sender.conn.send(f"[ZUMBIDO PRIVADO a {recipient_name}] {buzz_msg}\n".encode())
                    return True
                except Exception:
                    self.remove_client(client)
        return False

    def send_group_buzz(self, sender, group_name, buzz_msg):
        if group_name not in self.groups:
            sender.conn.send(f"El grupo '{group_name}' no existe\n".encode())
            return False

        msg = f"[ZUMBIDO GRUPO {group_name} - {sender.name}] {buzz_msg}\n"
        for member_name in self.groups[group_name]:
            for client in self.clients:
                if client.name == member_name:
                    try:
                        client.conn.send(msg.encode())
                    except Exception:
                        self.remove_client(client)
        return True

    def handle_command(self, command, client):
        cmd = command.removeprefix('<command>')
        if cmd == "list":
            users = "\n".join([c.name for c in self.clients if c.name != client.name])
            client.conn.send(f"Usuarios conectados:\n{users}\n".encode())

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            if client.name:
                self.broadcast(f"{client.name} ha abandonado el chat\n", client)
                for group_name in list(client.groups):
                    if group_name in self.groups:
                        self.groups[group_name].remove(client.name)
                        if not self.groups[group_name]:
                            del self.groups[group_name]
            print(f"Cliente desconectado: {client.addr}")
            client.conn.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()