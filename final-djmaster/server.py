import socket
import threading

HOST = 'tx8.debugueando.com'
PORT = 3004

def manejar_mensajes(sock):
    buffer = ''
    while True:
        try:
            datos = sock.recv(1024)
            if not datos:
                print("Servidor desconectado.")
                break

            buffer += datos.decode()
            while '\n' in buffer:
                linea, buffer = buffer.split('\n', 1)
                if ':' in linea:
                    accion, payload = linea.split(':', 1)
                    print(f"[Servidor] {accion.strip()}: {payload.strip()}")
                else:
                    print(f"[Servidor] {linea.strip()}")
        except Exception as e:
            print(f"Error al recibir datos: {e}")
            break

def conectar_a_servidor():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")
        return sock
    except Exception as e:
        print(f"No se pudo conectar al servidor: {e}")
        return None

def main():
    sock = conectar_a_servidor()
    if sock:
        hilo = threading.Thread(target=manejar_mensajes, args=(sock,), daemon=True)
        hilo.start()

        try:
            while True:
                mensaje = input("Escribe un mensaje para enviar al servidor (o 'salir'): ")
                if mensaje.lower() == 'salir':
                    break
                sock.sendall(f"{mensaje}\n".encode())
        except KeyboardInterrupt:
            pass
        finally:
            sock.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    main()
