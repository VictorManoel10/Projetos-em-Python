def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

while True:
    entrada = input("Digite o primeiro número (ou 'sair' para encerrar): ")
    if entrada.lower() in ['sair', 'q']:
        print("Encerrando a calculadora. Até mais!")
        break
    try:
        num1 = float(entrada)
    except ValueError:
        print("Valor inválido! Tente novamente.")
        continue

    op = input("Qual será a operação (+, -, *, /): ")
    if op not in ['+', '-', '*', '/']:
        print("Operação inválida!")
        continue

    entrada = input("Digite o segundo número: ")
    try:
        num2 = float(entrada)
    except ValueError:
        print("Valor inválido! Tente novamente.")
        continue

    if op == "+":
        result = somar(num1, num2)
    elif op == "-":
        result = subtrair(num1, num2)
    elif op == "*":
        result = multiplicar(num1, num2)
    elif op == "/":
        result = dividir(num1, num2)

    print(f"{num1} {op} {num2} = {result}\n")
