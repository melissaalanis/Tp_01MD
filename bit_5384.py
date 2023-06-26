#Trabalho Prático (TP) da disciplina de Matemática Discreta

# Declarando Entradas
n1 = int(input())
n2 = int(input())
base = int(input())
vetorbinario = []

if n1 < 0 or n1 > 512:
    print("ERRO")
elif n2 < 0 or n2 > 512:
    print("ERRO")
else:
    def TransformaBinario(num):
        vetorbinario = [] # Para que o vetor esteja vazio na hora do n2.
        while num >= 2:
            resto = num % 2
            num = num // 2
            vetorbinario.append(resto)
        vetorbinario.append(num) # para add a ultima divisao.
        vetorbinario.reverse() # Função utilizada para inverter os elementos do vetor.

        return vetorbinario

    v1 = TransformaBinario(n1)
    v2 = (TransformaBinario(n2))

    def SomaBinario(num1, num2):
        #Tornando os meus dois números binários do mesmo tamanho p/ somar
        if len(num1) > len(num2):
            for i in range(len(num1)-len(num2)):
                v2.insert(0, 0)
        elif (len(num1)<len(num2)):
            for i in range(len(num2)-len(num1)):
                v1.insert(0, 0)

        #Fazendo a soma
        vsoma = []
        vai1 = 0
        # v1.reverse() # A soma começa da direita para a esquerda
        # v2.reverse()
        for j in range(len(v2)-1, -1, -1):
            soma = v1[j] + v2[j] + vai1
            if soma == 1 or soma == 3:
                unidade = 1
            else:
                unidade = 0

            if soma == 2 or soma == 3:
                vai1 = 1
            else:
                vai1 = 0

            vsoma.append(unidade)
            
        if vai1 == 1:
            vsoma.append(vai1)
        vsoma.reverse()
        return vsoma
    soma = SomaBinario(v1, v2) #Variável da soma


    # Transformando Binário pra Decimal
    def BinarioDecimal(vsoma):
        somatorio = 0
        for i in range(len(vsoma)):
            n = len(vsoma) - i -1
            somatorio += (2**n)*(vsoma[i])
        return somatorio

    # Transformando Decimal pra Hexadecimal
    def DeciHexa(decimal):
        hexa = []
        if decimal == 0:
            hexa.append(0)
        else:
            while decimal != 0:
                resto = decimal % 16
                decimal = decimal //16

                if resto == 10:
                    hexa.append("A")
                elif resto == 11:
                    hexa.append("B")
                elif resto == 12:
                    hexa.append("C")
                elif resto == 13:
                    hexa.append("D")
                elif resto == 14:
                    hexa.append("E")
                elif resto == 15:
                    hexa.append("F")
                else:
                    hexa.append(resto)
            hexa.reverse()
        return hexa
    #Transformando de Decimal Para Octal:
    def DeciOctal(decimal):
        octal= []
        if decimal == 0:
            octal.append(0)
        else:
            while decimal != 0:
                resto = decimal % 8
                decimal = decimal // 8

                octal.append(resto)
            octal.reverse()
        return octal

    # Tratando a saída binária
    if base == 2:
        while len(soma)<11:
            soma.insert(0,0)
        print("".join(map(str, soma)))

    # Tratando a saída Decimal
    elif base == 10:
        print(BinarioDecimal(soma))

    # Tratando a saída Hexadecimal
    elif base == 16:
        hex = BinarioDecimal(soma)
        hexV = DeciHexa(hex)
        while len(hexV)<3:
            hexV.insert(0,0)
        print("".join(map(str, hexV)))
    # Tratando a saída Octal
    elif base == 8:
        oct = BinarioDecimal(soma)
        octV = DeciOctal(oct)
        while len(octV)<4:
            octV.insert(0, 0)
        print("".join(map(str, octV)))
    else:
        print("ERRO")



    




        
