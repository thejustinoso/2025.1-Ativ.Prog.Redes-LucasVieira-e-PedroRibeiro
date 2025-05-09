def calcular_subrede():
    # Entrada de dados
    ip = input('Digite o IPv4 (ex: 192.168.1.1):').strip()
    mask = int(input('Digite a máscara em bits (ex: 24):')).strip()

    # Converte IP para inteiro (32 bits)
    a, b, c, d = map(int, ip.split('.'))
    ip_num = (a << 24) | (b << 16) | (c << 8) | d

    # Realiza operações bit a bit (Cálculo bitwise)
    mask_num = (0xFFFFFFFF << (32 - mascara)) & 0xFFFFFFFF #0xFFFFFFFF é um número hexadecimal que representa um valor de 32 bits onde todos os bits são 1. Que é mais simples do que representar 32 caracteres 1 ou o decimal que os representa. 
    rede = ip_num & mask_num
    broadcast = rede | ((1 << (32 - mask)) -1)
    gateway = broadcast - 1

    # Converte os resultados para IP
    def int_to_ip(n):
        return f'{n >> 24 & 0xFF}.{n >> 16 & 0xFF}.{n >> 8 & 0xFF}.{n & 0xFF}.' #Os bits estão sendo deslocados para formar os octetos.

    #Saída de resultados
    print(f"\nEndereço da rede: {int_to_ip(rede)}")
    print(f"Broadcast: {int_to_ip(broadcast)}")
    print(f"Gateway: {int_to_ip(gateway)}")
    print(f"Hosts possíveis: {((1 << (32 - mascara)) - 2)}")

    # Executa o programa
    if __name__ == "__main__":
        calcular_subrede()
