while True:
    # Pede para o usuário digitar o primeiro número ou 'sair' para encerrar o programa
    entrada = input("Digite o primeiro número (ou 'sair' para encerrar): ")
    # Verifica se o usuário quer sair (digitou 'sair' ou 'q', sem diferenciar maiúsculas/minúsculas)
    if entrada.lower() in ['sair', 'q']:
        print("Encerrando a calculadora. Até mais!")
        break  # Sai do loop infinito e encerra o programa
    # Tenta converter a entrada para número decimal (float)
    try:
        num1 = float(entrada)
    except ValueError:
        # Se der erro na conversão, avisa e volta para o início do loop para tentar novamente
        print("Valor inválido! Tente novamente.")
        continue
    # Pede para o usuário digitar a operação matemática desejada
    op = input("Qual será a operação (+, -, *, /, %): ")
    # Verifica se a operação é válida; se não for, avisa e reinicia o loop
    if op not in ['+', '-', '*', '/', '%']:
        print("Operação inválida!")
        continue 
    # Pede para o usuário digitar o segundo número
    entrada = input("Digite o segundo número: ")    
    # Tenta converter a entrada para float, caso contrário reinicia o loop
    try:
        num2 = float(entrada)
    except ValueError:
        print("Valor inválido! Tente novamente.")
        continue    
    # Executa a operação escolhida
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        try:
            # Tenta fazer a divisão, tratando o caso de divisão por zero
            result = num1 / num2
        except ZeroDivisionError:
            print("ERRO: Divisão por zero!")
            continue  # Volta para o início do loop sem imprimir resultado
    elif op == "*":
        result = num1 * num2
    elif op == "%":
        result = (num1 * num2) / 100
    # Mostra o resultado da operação para o usuário
    print(f"{num1} {op} {num2} = {result}\n")

