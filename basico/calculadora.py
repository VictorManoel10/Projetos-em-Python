from colorama import Fore, Style, init
init(autoreset=True)

# Função para ler um número (ou comando de saída)
def obter_numero(mensagem, resultado_anterior):
    while True:
        entrada = input(Fore.YELLOW + mensagem + Style.RESET_ALL)
        if entrada.lower() in ['sair', 'q']:  # Permite encerrar o programa
            return 'sair'
        if entrada.lower() == 'ans':
            return resultado_anterior  
        try:
            return float(entrada)  # Converte entrada para número
        except ValueError:
            print(Fore.RED + "Valor inválido! Tente novamente."+ Style.RESET_ALL)
        
# Função para ler e validar a operação matemática
def obter_operacao():
    operacoes_validas = ['+', '-', '*', '/', '%']
    while True:
        op = input(Fore.CYAN + "Qual será a operação (+, -, *, /, %): " + Style.RESET_ALL)
        if op in operacoes_validas:
            return op
        print(Fore.RED + "Operação inválida!" + Style.RESET_ALL)

# Função que executa o cálculo com base na operação escolhida
def calcular(num1, op, num2):  
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        if num2 == 0:
            return Fore.RED + "ERRO: Divisão por zero!" + Style.RESET_ALL  # Evita erro ao dividir por zero
        return num1 / num2
    elif op == "*":
        return num1 * num2
    elif op == "%":
        return (num1 * num2) / 100  # Calcula porcentagem do primeiro número

def exibir_interface(ans):
    print(Fore.MAGENTA + "=" * 40)
    print("CALCULADORA INTERATIVA DE TERMINAL".center(40))
    print("=" * 40 + Style.RESET_ALL)
    print(f"{Fore.BLUE}[último resultado = {ans}]{Style.RESET_ALL}")

# Função principal que controla o fluxo da calculadora
def main():
    resultado_anterior = 0
    while True:
        exibir_interface(resultado_anterior)
        num1 = obter_numero("Digite o primeiro número (ou 'ans',  'sair' para encerrar): ", resultado_anterior)
        if num1 == 'sair':
            print(Fore.GREEN + "Encerrando a calculadora. Até mais!" + Style.RESET_ALL)
            break

        op = obter_operacao()

        num2 = obter_numero("Digite o segundo número(ou 'ans'): ", resultado_anterior)
        if num2 == 'sair':
            print(Fore.GREEN + "Encerrando a calculadora. Até mais!" + Style.RESET_ALL)
            break

        resultado = calcular(num1, op, num2)
        print(Fore.GREEN + f"\n Resultado {num1} {op} {num2} = {resultado}\n"+ Style.RESET_ALL)  # Exibe o resultado

        if isinstance(resultado, (int,float)):
            resultado_anterior = resultado

# Inicia a execução do programa
main()