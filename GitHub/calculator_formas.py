import math

print("*FORMAS GEOMÉTRICAS - CALCULAR ÁREA*\n")
print("Selecione uma forma geométrica:\n")
print("a) Círculo")
print("b) Triângulo")
print("c) Quadrado")
print("d) Losango\n")

opcao = input("Digite a opção desejada (a, b, c ou d): ").lower()

match opcao:
    case 'a':

        raio = float(input("Digite o raio do círculo: "))
        area = math.pi * raio ** 2
        print(f"A área do círculo com raio {raio} é: {area:.2f}")
    case 'b':
       
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = 0.5 * base * altura
        print(f"A área do triângulo com base {base} e altura {altura} é: {area:.2f}")
    case 'c':
       
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"A área do quadrado com lado {lado} é: {area:.2f}")
    case 'd':
       
        diagonal_maior = float(input("Digite a diagonal maior do losango: "))
        diagonal_menor = float(input("Digite a diagonal menor do losango: "))
        area = (diagonal_maior * diagonal_menor) / 2
        print(f"A área do losango com diagonais {diagonal_maior} e {diagonal_menor} é: {area:.2f}")
    case _:
        
        print("Opção inválida. Por favor, escolha uma opção válida (a, b, c ou d).")
        