from Servidor import Servidor
from ClienteSensor import ClienteSensor
from ClienteAtuador import ClienteAtuador

def main():
    servidor = Servidor()
    cliente_sensor = ClienteSensor()
    cliente_atuador = ClienteAtuador()

    servidor.start()
    cliente_sensor.start()
    cliente_atuador.start()

if __name__ == "__main__":
    main()
