import socket
import time

class ClienteAtuador:
    def __init__(self):
        self.host = "localhost"  # Endereço IP do servidor
        self.port = 8080  # Porta do servidor
        self.socket_cliente = None

    def start(self):
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_cliente.connect((self.host, self.port))

        while True:
            mensagem = "ASSINAR,Luminosidade"
            self.socket_cliente.send(mensagem.encode())
            valor_luminosidade = self.socket_cliente.recv(1024).decode()
            self.atualizar_cortina(valor_luminosidade)
            time.sleep(10)

        self.socket_cliente.close()

    def atualizar_cortina(self, valor_luminosidade):
        if valor_luminosidade:
            valor_luminosidade = int(valor_luminosidade)
            if valor_luminosidade >= 60:
                print("Abrindo Cortina")
            else:
                print("Fechando cortina")

if __name__ == "__main__":
    cliente_atuador = ClienteAtuador()
    cliente_atuador.start()
