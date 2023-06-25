# Sockets
Atividade de Redes de Computadores I


Você deverá desenvolver um sistema de comunicação (Veja Figura 1) para abrir e fechar uma cortina eletrônica através da luminosidade do ambiente externo. A cortina é controlada pelo Cliente Atuador, e depende da luminosidade (neste caso esse tópico) para tomar a decisão de abrir ou fechar a cortina. O Cliente Sensor envia as informações de luminosidade para o servidor. O Cliente Atuador solicita a luminosidade ao Servidor.

Para desenvolver esse sistema, siga as seguintes instruções:

Replique os códigos Cliente.java para os atores “Cliente Sensor” e “Cliente Atuador”:

Cliente Sensor: Essa classe deve se conectar de 5 em 5 segundos com o servidor e publicar valores de luminosidade (tópico) que são gerados de maneira aleatória entre 0 e 100;
Cliente Atuador: Essa classe deve se conectar de 10 em 10 segundos com o servidor e assinar (solicitar) valores de luminosidade. Recebido o valor de luminosidade, o atuador deve abrir a cortina se a luminosidade for maior ou igual a 60. Caso contrário, e o valor da luminosidade seja menor que 60, a cortina deve fechar. Para simular a abertura/fechamento da cortina, imprima na tela do Cliente Atuador a mensagem: “Abrindo Cortina” ou “Fechando cortina”.

Altere o código TrataCliente.java para que o servidor possa receber e tratar as solicitações do cliente:

“PUBLICAR, TOPICO, VALOR”: O cliente envia uma string contendo três informações que podem ser acessadas pelo TrataCliente.java individualmente pela função .split(“,”):

PUBLICAR: string que representa a operação no qual o servidor deve guardar um valor de um tópico;
TOPICO: string que representa uma chave para identificar um valor;
VALOR: string que representa o valor daquele tópico e que é enviado a um cliente atuador que assina aquele tópico.

“ASSINAR, TOPICO”: O cliente envia uma string contendo duas informações que podem ser acessadas individualmente pela função .split(“,”):
ASSINAR: string que representa a operação no qual o servidor deve responder um valor de um tópico;
TOPICO: string que representa uma chave para identificar um valor.

Altere o código Servidor.java e defina um Dictionary para representar os tópicos e seus respectivos valores. Passe esse dicionário como argumento para a classe TrataCliente.java para que você consigna armazenar/alterar (dicionario.put(“TOPICO”, “VALOR”)) um tópico, ou consultar (dicionario.get(“TOPICO”)).
