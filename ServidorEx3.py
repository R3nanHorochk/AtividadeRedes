#Nome:Alef de Souza Lima        - RA:10431891
#Nome:Renan Horochk de Andrade  - RA:10438120
import socket
import threading
import time

TCP_IP = '192.168.0.111' # Ouve em qualquer IP da máquina
portas = [31891, 38120, 38121, 31892,31893,38122] #Portas
TAMANHO_BUFFER = 1024 # definição do tamanho do buffer

def escutar_porta(p):
    try:
        # Criação de socket TCP com SOCK_STREAM indicando TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # IP e porta que o servidor deve aguardar a conexão
        sock.bind((TCP_IP, p))
        #Define o limite de conexões
        sock.listen(len(portas))
        print(f"[*] Porta {p} monitorada.")
        
        while True:
            # Aceita conexão 
            conn, addr = sock.accept()
            #dados retidados da mensagem recebida do cliente 
            data = conn.recv(TAMANHO_BUFFER)
            #se recebeu corretamente
            if data:
                print(f"\n[PORTA {p}] Mensagem de {addr}: {data.decode('UTF-8')}")
            # Fecha conexão
            conn.close()
    except Exception as e:
        print(f"Erro na porta {p}: {e}")

print("SERVIDOR DE LOGS ATIVO (Aguardando disparos) ")

for p in portas:
    # Inicia as threads de escuta
    threading.Thread(target=escutar_porta, args=(p,), daemon=True).start()

# Loop infinito para o programa não fechar e as threads continuarem vivas
try:
    while True:
        #Espera 1 segundos para não repetir
        time.sleep(1) 
except KeyboardInterrupt:
    print("\nEncerrando servidor...")
