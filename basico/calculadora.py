def obter_numero(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.lower() in ['sair', 'q']:
            return 'sair'  
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido! Tente novamente.")
        
def obter_operacao():
    operacoes_validas = ['+', '-', '*', '/', '%']
    while True:
        op = input("Qual será a operação (+, -, *, /, %): ")
        if op in operacoes_validas:
            return op
        print("Operação inválida!")

def calcular(num1, op, num2):  
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        if num2 == 0:
            return("ERRO: Divisão por zero!")   
    elif op == "*":
        return num1 * num2
    elif op == "%":
        return (num1 * num2) / 100

def main():
    while True:
        num1 = obter_numero("Digite o primeiro número(ou 'sair' para encerrar): ")
        if num1 == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        op = obter_operacao()

        num2 = obter_numero("Digite o segundo número: ")
        if num2 == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        resultado = calcular(num1,op,num2)
        print(f"{num1} {op} {num2} = {resultado}\n")
    
main()

