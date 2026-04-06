#Nome:Alef de Souza Lima        - RA:10431891
#Nome:Renan Horochk de Andrade  - RA:10438120
import socket #importa modulo socket

TCP_IP = '192.168.0.111' # endereço IP do servidor 
TCP_PORTA = 38120 # porta com 5 ultimos digitos do RA
TAMANHO_BUFFER = 1024 # definição do tamanho do buffer

# Criação de socket TCP com SOCK_STREAM indicando TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))
#Define o limite de conexões
servidor.listen(1)

print(f"Servidor de Chat iniciado em {TCP_IP}:{TCP_PORTA}")
print("Aguardando..")
# Aceita conexão 
conn, addr = servidor.accept()
print(f"Cliente conectado: {addr}")


while True:
    #dados retidados da mensagem recebida do cliente    
    data = conn.recv(TAMANHO_BUFFER)
    #decodifica mensagem recebida
    mensagem = data.decode('utf-8').strip()
    #se não recebeu corretamente
    if not data:
        print("O cliente encerrou o chat")
        break
    #se mensagem igual a quit encerra o programa 
    if mensagem == "quit":
        print("Programa encerrado pelo cliente")
        break
    print(f"Cliente diz: {data.decode('UTF-8')}")
        

    resposta = input("Digite a resposta: ")
    # envia mensagem para servidor 
    conn.send(resposta.encode('UTF-8'))
    #se mensagem igual a quit encerra o programa 
    if resposta.lower() == "quit":
        print("Programa encerrado")
        break
        

conn.close()
servidor.close()
