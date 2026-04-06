#Nome:Alef de Souza Lima        - RA:10431891
#Nome:Renan Horochk de Andrade  - RA:10438120
import socket
import threading
import math

TCP_IP = '192.168.0.111' # Ouve em qualquer IP da máquina
TAMANHO_BUFFER = 1024 # definição do tamanho do buffer
# O cliente agora detém o controle das portas alvo
portas_alvo = [31891, 38120, 38121, 31892]#Portas

def enviar_para_portas(lista_portas, mensagem):
    #Pega o nome da thread atual
    nome_thread = threading.current_thread().name
    for p in lista_portas:
        try:
            # Cria o socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Evita que a thread trave se a porta estiver fechada
            sock.settimeout(2)
            # Conecta ao servidor IP com a porta especificada
            sock.connect((TCP_IP, p))
            # envia mensagem
            sock.send(mensagem.encode('UTF-8'))
            print(f"[{nome_thread}] Sucesso: Porta {p}")
            #Encerra conexão
            sock.close()
        except Exception as e:
            print(f"[{nome_thread}] Falha na porta {p}: {e}")

def disparar_lote(alvos, n_threads, msg):
    #Se não tiver alvos ele finaliza
    if not alvos: return

    #Divide o tamanho para cada thread
    tamanho = math.ceil(len(alvos) / n_threads)
    threads_list = []

    for i in range(n_threads):
        #Inicio do range
        inicio = i * tamanho
        #Fim do range
        fim = (i + 1) * tamanho
        #Range dos alvos
        Range = alvos[inicio:fim]
        
        if Range:
            #Instancia a thread
            t = threading.Thread(target=enviar_para_portas, args=(Range, msg), name=f"Thread-{i}")
            #Coloca no array de thread
            threads_list.append(t)
            #Cria a Thread
            t.start()

    for t in threads_list:
        #Inicia a Thread
        t.join()
    print("Disparo concluído.")


print(f"Cliente carregado com portas: {portas_alvo}")
num_threads = int(input("Defina o número de threads para o envio: "))

while True:
    print("1. Adicionar Porta ")
    print("2. Enviar para TODAS ")
    print("3. Enviar para RANGE ")
    print("4. Enviar para uma unica")
    print("5. Sair \n")
    op = input("Escolha: ")

    if op == "1":
        nova = int(input("Nova porta: "))
        portas_alvo.append(nova)
        
    elif op == "2":
        texto = input("Mensagem: ")
        disparar_lote(portas_alvo, num_threads, texto)

    elif op == "3":
        p_ini = int(input("Início do range: "))
        p_fim = int(input("Fim do range: "))
        #Busca as portas no range
        selecionadas = [p for p in portas_alvo if p_ini <= p <= p_fim]
        texto = input(f"Mensagem para o range {p_ini}-{p_fim}: ")
        #Dispara mensagens
        disparar_lote(selecionadas, num_threads, texto)

    elif op == "4":
        p_ini = int(input("Numero da porta: "))
        p_fim = p_ini
        #Busca as portas no range
        selecionadas = [p for p in portas_alvo if p_ini <= p <= p_fim]
        texto = input(f"Mensagem para a porta {p_ini}: ")
        #Dispara mensagens
        disparar_lote(selecionadas, num_threads, texto)
    elif op == "5":
        break
