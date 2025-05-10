import struct

imagem = 'img.jpg'

try:
    with open(imagem, "rb") as hexa:
        primeirosBytes = hexa.read(6) #a) Lê os primeiros 6 bytes da imagem JPEG.
        hexa.close()

    # Obtém o tamanho dos metadados (app1DataSize) nas posições 4 e 5.
        app1DataSize = struct.unpack(">H", primeirosBytes[4:6])[0] #Pega os bytes 4 e 5 (tamanho) e empacota eles em um inteiro
        print(f"Tamanho dos metadados: {app1DataSize} bytes")

    # Reabre o arquivo para próxima apontar os dados
        with open(imagem, "rb") as hexa_reaberto:
            # Lê os primeiros 6 bytes (já lidos).
            hexa_reaberto.read(6)
            # Lê os próximos 4 bytes e os ignora
            hexa_reaberto.read(4)
            # Lê o número de bytes em app1DataSize para app1Data.
            app1Data = hexa_reaberto.read(app1DataSize)
            print(f"Primeiros bytes de app1Data (para visualização): {app1Data[:20]}") # Mostra os primeiros 20 bytes


        # Na posição 16 de app1Data há 2 bytes que indicam quantos metadados (tags EXIF) essa imagem tem.
        if len(app1Data) >= 18:
            numero_metadados = struct.unpack(">H", app1Data[16:18])[0]
            print(f"Número de metadados (tags EXIF) na imagem: {numero_metadados}")
        else:
            print("Erro: app1Data não tem tamanho suficiente para ler o número de metadados.")
            exit()

        offset_atual = 18  # b) A partir da posição 18 de app1Data estão efetivamente os metadados.
        altura = None
        largura = None

        while offset_atual < len(app1Data) - 12:
            # 2 bytes: qual o metadado (TagId)
            if offset_atual + 2 > len(app1Data):
                break
            tag_id = struct.unpack(">H", app1Data[offset_atual:offset_atual + 2])[0]
            offset_atual += 2

            # 2 bytes: o tipo do metadado (TagType) - ignorar por enquanto
            offset_atual += 2

            # 4 bytes: o número de repetições (Count) - ignorar por enquanto
            offset_atual += 4

            # 4 bytes: o valor do metadado (Value/Offset)
            if offset_atual + 4 > len(app1Data):
                break
            valor_offset = struct.unpack(">I", app1Data[offset_atual:offset_atual + 4])[0]
            offset_atual += 4

            if tag_id == 0x0101:
                altura = valor_offset
            elif tag_id == 0x0100:
                largura = valor_offset

            if altura is not None and largura is not None:
                break
            
        #Se a tag 0x0101 (indicadora da altura da imagem) for encontrada, será exposto seu valor
        if altura is not None:
            print(f"Altura da imagem: {altura}")
        else:
            print("Tag de altura não encontrada.")

        #Se a tag 0x0100 (indicadora da largura da imagem) for encontrada, será exposto seu valor
        if largura is not None:
            print(f"Largura da imagem: {largura}")
        else:
            print("Tag de largura não encontrada.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{imagem}' não encontrado.")
except struct.error as e:
    print(f"Erro ao desembalar os bytes: {e}")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
