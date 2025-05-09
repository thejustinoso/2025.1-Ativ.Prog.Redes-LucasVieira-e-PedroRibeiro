import hashlib, time, struct
import encodings.aliases

#Função:
def findNonce (dataToHash,bitsToBeZero):
    nonce = 0
    limite = 2 ** (256 - bitsToBeZero)  #essa parte da função pega o limite maximo que o hash pode se mover, pois é necessario os 0's

    tempo_iniciado = time.time() # quando a função é chamada começa uma contagem de tempo

    while True:
            txt_e_nonce = struct.pack (">I", nonce) + dataToHash #junta o nonce atual com o hash
            hash_256b = hashlib.sha256(txt_e_nonce).hexdigest() #transforma o nonce + o txt(em bytes) em uma string com elementos hexa
            int_hash = int(hash_256b,16) #como está em hexa na string é necessário o 16 para formatação pro inteiro
        
            if int_hash < limite:       #só chegará aqui quando o nonce certo for executado
                tempo_passado = time.time()-tempo_iniciado #o tempo menos o tempo iniciado para descobrir o decorrido
                return nonce, hash_256b, tempo_passado # retorna o valor do nonce certo, o hash encontrado, e o tempo passado
            nonce = nonce + 1   #se o nonce certo não for encontrado ele voltara ao inicio e somará o nonce +1 ate achar
#Resultado:


print("Texto: ","|||||||" "Bits em zero: ","|||||||" " Nonce: ","|||||||" "Tempo(em s): ") 

for i in range(9): # 9 repetições pois se pede 9 itens
     
    if i == 0:
        textostr = "Esse um texto elementar"
        bits0 = 8
    if i == 1:
        textostr = "Esse um texto elementar"
        bits0 = 10
    if i == 2:
        textostr = "Esse um texto elementar"
        bits0 = 15
    if i == 3:
        textostr = "Textinho"
        bits0 = 8
    if i == 4:
        textostr = "Textinho"
        bits0 = 18
    if i == 5:
        textostr = "Textinho"
        bits0 = 22
    if i == 6:
        textostr = "Meu texto médio"
        bits0 = 18
    if i == 7:
        textostr = "Meu texto médio"
        bits0 = 19
    if i == 8:
        textostr = "Meu texto médio"
        bits0 = 20
    
    texto = textostr.encode("utf-8") #esse encode é necessario pois precisa do valor em bytes desse str
    nonce, hash_encontrado, tempo_s = findNonce(texto,bits0) #atribuo os valores encontrado na função findNonce
    print(textostr,"|||||||",bits0,"|||||||",nonce ,"|||||||",tempo_s) #tabela com os resultados
