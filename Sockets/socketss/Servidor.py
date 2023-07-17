import socket
from threading import Thread

class Servidor(Thread):
    def __init__(self):
        super().__init__()
        self.host = "localhost"  # Endereço IP do servidor
        self.port = 8080  # Porta do servidor
        self.socket_servidor = None #Ainda não ha nenhum objeto
        self.conexoes = []  # Lista de conexões com os clientes
        self.topicos = {}  # Dicionário para armazenar os tópicos e seus valores

    def run(self):
        # Cria um socket do servidor
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Vincula o socket à porta e endereço IP especificados
        self.socket_servidor.bind((self.host, self.port))

        # Coloca o socket em modo de escuta
        self.socket_servidor.listen(5)

        print("Servidor iniciado. Aguardando conexões...")

        while True:
            # Aceita uma nova conexão do cliente
            conexao, endereco = self.socket_servidor.accept()

            # Adiciona a conexão à lista de conexões
            self.conexoes.append(conexao)
            print(f"Cliente conectado: {endereco}")

            # Cria uma thread para tratar as mensagens do cliente
            trata_cliente = TrataCliente(conexao, self)
            trata_cliente.start()

    def enviar_mensagem(self, mensagem):
        # Envia a mensagem para todas as conexões ativas
        for conexao in self.conexoes:
            conexao.send(mensagem.encode())

class TrataCliente(Thread):
    def __init__(self, conexao, servidor):
        super().__init__()
        self.conexao = conexao  # Armazena a conexão do cliente
        self.servidor = servidor  # Armazena a referência ao objeto servidor



    def run(self):
        while True:
            # Recebe uma mensagem do cliente
            mensagem = self.conexao.recv(1024).decode()

            # Verifica se a mensagem está vazia, indicando que a conexão foi encerrada
            if not mensagem:
                # Remove a conexão da lista de conexões
                self.servidor.conexoes.remove(self.conexao)
                self.conexao.close()
                break

            # Tratar a mensagem recebida e responder de acordo com o protocolo
            operacao, *args = mensagem.split(",")

            if operacao == "PUBLICAR":
                # Extrai o tópico e o valor da mensagem
                topico, valor = args

                # Armazena o valor no dicionário de tópicos
                self.servidor.topicos[topico] = valor

            elif operacao == "ASSINAR":
                # Extrai o tópico da mensagem
                topico = args[0]

                # Obtém o valor correspondente ao tópico do dicionário de tópicos
                valor = self.servidor.topicos.get(topico, "")

                # Envia o valor de volta para o cliente
                self.conexao.send(valor.encode())

if __name__ == "__main__":
    # Cria uma instância do servidor
    servidor = Servidor()

    # Inicia o servidor
    servidor.start()
