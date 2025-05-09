import struct

#Questão 3:
hexa = open("img.jpg", "rb")  # Abre a imagem para leitura em binário
primeirosBytes = hexa.read(6)             # Lê os primeiros 6 bytes
app1DataSize = struct.unpack(">H",primeirosBytes[4:6]) [0]     # Pega os bytes 4 e 5 (tamanho) e empacota eles em um inteiro
print(app1DataSize)                       # O tamanho obtido em um inteiro
hexa.close()                              # Fechamento do arquivo

#Questão 3-a):

hexa = open("img.jpg", "rb")
hexa.read(6)                  #os primeiros bytes lidos na primeira parte 
hexa.read(4)                  # os proximos 4 bytes para serem lidos e ignorados
app1Data = hexa.read(app1DataSize)  #o tamanho de cada bloco
print(app1Data)               #só para visualização



