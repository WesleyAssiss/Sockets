import socket
from threading import Thread

class Servidor(Thread):
    def __init__(self):
        super().__init__()
        self.host = "localhost"  # Endereço IP do servidor
        self.port = 8080  # Porta do servidor
        self.socket_servidor = None
        self.conexoes = []
        self.topicos = {}

    def run(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen(5)

        print("Servidor iniciado. Aguardando conexões...")

        while True:
            conexao, endereco = self.socket_servidor.accept()
            self.conexoes.append(conexao)
            print(f"Cliente conectado: {endereco}")

            trata_cliente = TrataCliente(conexao, self)
            trata_cliente.start()

    def enviar_mensagem(self, mensagem):
        for conexao in self.conexoes:
            conexao.send(mensagem.encode())

class TrataCliente(Thread):
    def __init__(self, conexao, servidor):
        super().__init__()
        self.conexao = conexao
        self.servidor = servidor

    def run(self):
        while True:
            mensagem = self.conexao.recv(1024).decode()
            if not mensagem:
                self.servidor.conexoes.remove(self.conexao)
                self.conexao.close()
                break

            # Tratar a mensagem recebida e responder de acordo com o protocolo
            operacao, *args = mensagem.split(",")
            if operacao == "PUBLICAR":
                topico, valor = args
                self.servidor.topicos[topico] = valor
            elif operacao == "ASSINAR":
                topico = args[0]
                valor = self.servidor.topicos.get(topico, "")
                self.conexao.send(valor.encode())

if __name__ == "__main__":
    servidor = Servidor()
    servidor.start()
