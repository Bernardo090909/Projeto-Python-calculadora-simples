from ast import operator


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def obter_numero(mensagem):
    while True:
       entrada = input(mensagem)

       if entrada.strip() == "":
           print("Entrada vazia. Por favor, digite um número.")
           continue

       try:
           return float(entrada)
       except ValueError:
           print("Entrada inválida. Por favor, insira um número.")

def main():
    print("bem-vindo à calculadora simples!")
    while True:
        num1 = obter_numero("Digite o primeiro número: ")
        operator = input("Escolha a operação (+, -, *, /): ")
        num2 = obter_numero("Digite o segundo número: ")

        if operator == '+':
            resultado = soma(num1, num2)
        elif operator == '-':
            resultado = subtracao(num1, num2)
        elif operator == '*':
            resultado = multiplicacao(num1, num2)
        elif operator == '/':
            resultado = divisao(num1, num2)
        else:
            print("Operador inválido. Por favor, escolha entre +, -, *, /.")
            continue

        print(f"Resultado: {resultado}")

        continuar = input("Deseja realizar outra operação? (s/n): " ).lower()
        if continuar != 's':
            print("encerrando a calculadora...")    
            break

if __name__ == "__main__":    main()
