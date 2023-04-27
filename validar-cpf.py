CPF = []
CPFVerificacao = []

while len(CPF) <= 10:
    Valores = int(input("Escreva o CPF (um digito de cada vez)"))
    if len(str(Valores)) > 1:
        print("Número Inválido")
    else:
        CPF.append(Valores)
        CPFVerificacao.append(Valores)

CPF.pop()
CPF.pop()

Condição1 = False
Condição2 = False

while Condição1 != True:
    contador = 10
    resultados = []
    for i in CPF:
        resultado = i * contador
        resultados.append(resultado)
        contador -= 1
        if contador == 1:
            Condição1 = True

resto = sum(resultados)%11 

def verificacao1(Valor):
    if resto < 2:
        dígito = 0       
    if resto >= 2:
        dígito = 11 - resto       
    return dígito

CPF.append(verificacao1(resto))

while Condição2 != True:
    contador2 = 11
    resultados2 = []
    for i in CPF:
        resultado2 = i * contador2
        resultados2.append(resultado2)
        contador2 -= 1
        if contador2 == 1:
            Condição2 = True

resto2 = sum(resultados2)%11 

def verificacao2(Valor2):
    if resto2 < 2:
        dígito2 = 0       
    if resto2 >= 2:
        dígito2 = 11 - resto2       
    return dígito2

CPF.append(verificacao2(resto2))

if CPF == CPFVerificacao:
    print("CPF Válido")
else:
    print("CPF Inválido")