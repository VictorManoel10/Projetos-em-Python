# Função para ler um número (ou comando de saída)
def obter_numero(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.lower() in ['sair', 'q']:  # Permite encerrar o programa
            return 'sair'  
        try:
            return float(entrada)  # Converte entrada para número
        except ValueError:
            print("Valor inválido! Tente novamente.")
        
# Função para ler e validar a operação matemática
def obter_operacao():
    operacoes_validas = ['+', '-', '*', '/', '%']
    while True:
        op = input("Qual será a operação (+, -, *, /, %): ")
        if op in operacoes_validas:
            return op
        print("Operação inválida!")

# Função que executa o cálculo com base na operação escolhida
def calcular(num1, op, num2):  
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        if num2 == 0:
            return("ERRO: Divisão por zero!")  # Evita erro ao dividir por zero
        return num1 / num2
    elif op == "*":
        return num1 * num2
    elif op == "%":
        return (num1 * num2) / 100  # Calcula porcentagem do primeiro número

# Função principal que controla o fluxo da calculadora
def main():
    while True:
        num1 = obter_numero("Digite o primeiro número (ou 'sair' para encerrar): ")
        if num1 == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        op = obter_operacao()

        num2 = obter_numero("Digite o segundo número: ")
        if num2 == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        resultado = calcular(num1, op, num2)
        print(f"{num1} {op} {num2} = {resultado}\n")  # Exibe o resultado

# Inicia a execução do programa
main()