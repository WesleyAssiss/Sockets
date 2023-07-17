# Importação dos módulos/classes necessários
from Servidor import Servidor
from ClienteSensor import ClienteSensor
from ClienteAtuador import ClienteAtuador

def main():
    # Criação das instâncias das classes Servidor, ClienteSensor e ClienteAtuador
    servidor = Servidor()
    cliente_sensor = ClienteSensor()
    cliente_atuador = ClienteAtuador()

    # Inicialização e execução dos threads das classes Servidor, ClienteSensor e ClienteAtuador
    servidor.start()
    cliente_sensor.start()
    cliente_atuador.start()

if __name__ == "__main__":
    main()
