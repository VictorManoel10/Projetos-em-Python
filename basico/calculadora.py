num1 =  0
op =    ''
num2 =   0
result = 0

while True:
    num1 = float(input("Digite o primeiro número: "))
    op = input("Qual será a operação: ")
    num2 = float(input("Digite o segundo número: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("ERRO: Divisão por zero!")
            continue
    elif op == "*":
        result = num1 * num2
    else:
        print("Operação desconhecida!")

    print(f"{num1} {op} {num2} = {result}")
