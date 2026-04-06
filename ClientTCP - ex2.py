#Nome:Alef de Souza Lima        - RA:10431891
#Nome:Renan Horochk de Andrade  - RA:10438120
import socket #importa modulo socket

TCP_IP = '192.168.0.111' # endereço IP do servidor 
TCP_PORTA = 38120 # porta com 5 ultimos digitos do RA
TAMANHO_BUFFER = 1024 # definição do tamanho do buffer

# Criação de socket TCP com SOCK_STREAM indicando TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor IP com a porta especificada
cliente.connect((TCP_IP, TCP_PORTA))

while True:
    mensagem = input("Digite sua mensagem: ")
    # envia mensagem para servidor 
    cliente.send(mensagem.encode('UTF-8'))

    #se mensagem igual a quit encerra o programa    
    if mensagem.lower() == 'quit':
        print("Programa encerrado")
        break


    print("Aguardando resposta do servidor")
    #dados retidados da mensagem recebida
    data = cliente.recv(TAMANHO_BUFFER)
    #decodifica mensagem recebida
    res = data.decode('utf-8').strip()
    #se mensagem igual a quit encerra o programa 
    if res == "quit":
        print("Programa encerrado pelo servidor")
        break
    #se não recebeu corretamente
    if not data:
        print("Conexão perdida com o servidor")
        break
        
    print(f"Servidor diz: {data.decode('UTF-8')}")

#Encerra conexão
cliente.close()
