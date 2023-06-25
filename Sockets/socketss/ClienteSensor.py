import socket
import random
import time

class ClienteSensor:
    def __init__(self):
        self.host = "localhost"  # Endereço IP do servidor
        self.port = 8080  # Porta do servidor
        self.socket_cliente = None

    def start(self):
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_cliente.connect((self.host, self.port))

        while True:
            valor_luminosidade = random.randint(0, 100)
            mensagem = f"PUBLICAR,Luminosidade,{valor_luminosidade}"
            self.socket_cliente.send(mensagem.encode())
            time.sleep(5)

        self.socket_cliente.close()
