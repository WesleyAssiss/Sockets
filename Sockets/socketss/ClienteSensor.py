import socket
import random
import time

class ClienteSensor:
    def __init__(self):
        self.host = "localhost"  # Endereço IP do servidor
        self.port = 8080  # Porta do servidor
        self.socket_cliente = None

    def start(self):
        # Cria um socket do cliente
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta o cliente ao servidor usando o endereço IP e a porta fornecidos
        self.socket_cliente.connect((self.host, self.port))

        while True:
            # Gera um valor de luminosidade aleatório entre 0 e 100
            valor_luminosidade = random.randint(0, 100)

            # Cria uma mensagem no formato "PUBLICAR,Luminosidade,valor_luminosidade"
            mensagem = f"PUBLICAR,Luminosidade,{valor_luminosidade}"

            # Codifica a mensagem em bytes e envia para o servidor
            self.socket_cliente.send(mensagem.encode())

            # Aguarda por 5 segundos antes de enviar a próxima mensagem
            time.sleep(5)

        # Fecha a conexão com o servidor
        self.socket_cliente.close()
