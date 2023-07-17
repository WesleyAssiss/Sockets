import socket
import time

class ClienteAtuador:
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
            # Envia uma mensagem para o servidor solicitando a assinatura do tópico "Luminosidade"
            mensagem = "ASSINAR,Luminosidade"
            self.socket_cliente.send(mensagem.encode())

            # Recebe o valor de luminosidade do servidor
            valor_luminosidade = self.socket_cliente.recv(1024).decode()

            # Chama o método para atualizar a cortina com base no valor de luminosidade recebido
            self.atualizar_cortina(valor_luminosidade)

            # Aguarda por 10 segundos antes de enviar uma nova solicitação ao servidor
            time.sleep(10)

        # Fecha a conexão com o servidor
        self.socket_cliente.close()

    def atualizar_cortina(self, valor_luminosidade):
        # Verifica se o valor de luminosidade não está vazio
        if valor_luminosidade:
            # Converte o valor de luminosidade para um número inteiro
            valor_luminosidade = int(valor_luminosidade)

            # Verifica se o valor de luminosidade é maior ou igual a 60
            if valor_luminosidade >= 60:
                print("Abrindo Cortina")
            else:
                print("Fechando cortina")

if __name__ == "__main__":
    # Cria uma instância do cliente atuador
    cliente_atuador = ClienteAtuador()

    # Inicia o cliente atuador
    cliente_atuador.start()
