import hashlib, time, struct

#Função:
def findNonce (dataToHash,bitsToBeZero):
    nonce = 0
    limite = 2 ** (256 - bitsToBeZero)    #essa parte da função pega o limite maximo que o hash pode se mover, pois é necessario os 0's

    tempo_iniciado = time.time()          #quando a função é chamada começa uma contagem de tempo

    while True:
            txt_e_nonce = struct.pack (">I", nonce) + dataToHash    #junta o nonce atual com o hash
            hash_256b = hashlib.sha256(txt_e_nonce).hexdigest       #transforma o nonce + o hash em uma string com elementos hexa
            int_hash = int(hash_256b,16)                            #como está em hexa na string é necessário o 16 para formatação pro inteiro
        
            if hash_int < limite:                       #só chegará aqui quando o nonce certo for executado
                tempo_passado = time.time - start_time  #o tempo menos o tempo iniciado para descobrir o decorrido
                return nonce, hash_256b, tempo_passado  #retorna o valor do nonce certo, o hash encontrado, e o tempo passado
            nonce = nonce + 1                           #se o nonce certo não for encontrado ele voltara ao inicio e somará o nonce +1 ate achar
#Resultado:

#for i in range (9):
     #print(f'Texto a validar {findNonce(“Esse um texto elementar”,)}')
