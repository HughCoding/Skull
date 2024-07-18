class TerminalColor:
  ERRO = '\033[91m'
  NORMAL = '\033[0m'  


def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def show_menu():
    print("Selecione uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")


while True:
    show_menu()
    escolha = input("Escolha uma opção (1/2/3/4): ")
    
    if escolha not in ["1", "2", "3", "4"]:
        print(TerminalColor.ERRO, "Opção inválida!" +
              TerminalColor.NORMAL)
        break

  
    if escolha in ["1", "2", "3", "4"]:
        num1_str = input("Digite o primeiro número: ")
        num2_str = input("Digite o segundo número: ")

        # Verifica se os números são válidos
        if not num1_str.isdigit() or not num2_str.isdigit():
            print(TerminalColor.ERRO, "Digite apenas números válidos!" +
                  TerminalColor.NORMAL)
            break
        
        num1 = float(num1_str)
        num2 = float(num2_str)

        if escolha == "1":
            resultado = adicao(num1, num2)
            operador = "+"
        elif escolha == "2":
            resultado = subtracao(num1, num2)
            operador = "-"
        elif escolha == "3":
            resultado = multiplicacao(num1, num2)
            operador = "*"
        elif escolha == "4":
            resultado = divisao(num1, num2)
            operador = "/"

        print(f"{num1} {operador} {num2} = {resultado}")
        resposta_correta = input("A resposta está correta? (sim/não): ")
        
        if resposta_correta.lower() in ["sim", "s"]:
                print("\033[92mSalvo!\033[0m")
                break

        else:
            resposta_correta.lower() in ["nao", "não", "n"]
            print(
                """\033[91m    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡶⠛⠛⢛⡉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠲⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡶⠿⡟⠉⠑⠒⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠍⣙⠿⢶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠛⠉⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡈⠙⠿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⠉⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡿⠃⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠹⢷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠟⢀⡴⠋⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠈⢻⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣿⠃⢠⡞⠁⠀⠀⠃⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀
⠀⠀⢀⣿⠁⢠⣿⠁⡀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠀⠀
⠀⠀⣾⠁⢠⣿⡿⠀⢿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠹⣷⠀⠀
⠀⣼⠏⢀⣟⣿⣿⠀⢸⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢻⣇⠀
⠀⣿⠀⢼⣹⣿⣿⡆⠀⢻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠈⣿⡀
⢸⡿⠀⠀⣾⣿⣿⣷⠀⠈⣿⡾⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⣿⡇
⢸⡇⠀⠀⢂⣿⣿⣿⡇⠀⢻⣿⡫⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⣿⡇
⢸⣧⠀⠀⣌⣽⣿⣿⣧⠀⠈⣿⣿⣿⡟⠧⣄⠀⠀⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⣿⡇
⠸⣿⠀⠀⠑⣿⣿⣿⣿⡄⠀⠻⠿⠟⠛⠛⠉⠉⠛⠃⠀⠀⠘⠛⠻⠶⣄⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⠋⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠤⠀⠀⠀⠀⢀⣿⡇
⠀⣿⣇⠀⠀⣿⣿⣿⣿⠷⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⢿⠀⠀⠀⠀⣸⡟⠀
⠀⠹⣿⠀⠀⢻⣿⣿⣏⠀⠀⠀⠀⢀⣀⣠⣴⣾⣿⣶⣶⣷⣦⣄⣀⠀⠀⠐⣦⣀⣀⢰⣋⠀⠀⠀⣀⣀⣤⣴⣶⣶⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⠸⣷⣿⠆⠀⠀⠀⣿⠁⠀
⠀⠀⢻⣆⠀⠀⢹⣿⡿⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢿⠛⠿⣧⡖⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣿⡇⠀⠀⠀⣼⡟⠀⠀
⠀⠀⠀⣿⡄⠀⠀⣹⡆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⠀⣠⡞⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⣟⠀⠀⠀⣠⡿⠀⠀⠀
⠀⠀⠀⢿⣷⣄⡾⢻⣷⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⠀⣿⡶⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢀⠉⠳⡄⢠⣿⠇⠀⠀⠀
⠀⠀⠀⠘⣧⣽⡇⢸⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⠋⣰⡌⢰⣄⠹⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢼⡄⠀⢷⢹⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣼⠃⠸⣿⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⠋⢁⣼⠇⣰⣿⡆⢸⣿⡇⢰⣄⠈⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢸⡇⠀⠸⣷⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣹⡇⠀⠀⠚⢻⣦⣄⣙⠛⠛⣿⠟⠛⠋⣉⣀⠀⣀⣠⡾⢻⡟⣰⣿⣿⣷⣿⣿⣷⡄⣿⢷⣤⣀⠀⠋⠙⢻⣟⠛⠛⢛⡛⠛⢁⣠⠾⠋⠀⠀⠀⠹⣟⠀⠀⠀⠀
⠀⠀⠀⣤⡟⠀⠀⠀⠀⢰⢻⡿⠋⠛⠋⠛⠂⠀⠀⠉⠉⠉⠉⢉⣠⣿⢇⣿⣿⣿⣿⣿⣿⣿⣇⢸⡌⠙⡿⣷⠶⠚⠁⠈⠙⠲⢬⡉⠉⠋⠁⠤⣄⣀⡀⠀⠀⢿⣧⠀⠀⠀
⠀⠀⠀⣿⡀⠀⠀⠀⠠⠃⢈⠅⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⠞⠉⣹⡟⢺⣿⣿⣿⣿⣿⣿⣿⣿⡜⣇⠀⠰⢦⣄⣀⠀⠀⠀⠀⠀⠙⠦⣄⡀⠀⠀⠉⠉⠳⣄⢀⣿⠀⠀⠀
⠀⠀⠀⠘⢿⣦⡀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠠⣞⠉⠉⠁⠀⠀⠘⢇⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠻⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⣹⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣆⡀⠘⣦⣀⣀⣀⣀⣀⣀⠀⠘⢦⠀⠀⠀⠀⠀⢸⡈⢿⣿⣿⣿⣹⣿⣿⣿⣦⡇⠀⠀⠀⠀⠀⡰⠂⢀⣀⣀⣠⣤⣴⣏⡀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢻⣿⣾⣿⣿⣿⣿⣿⣿⠟⢿⣶⡌⠷⠀⠀⢀⡀⠀⠳⣌⠻⣿⠏⠸⠿⢟⣩⠏⠁⠀⠀⠀⠠⠞⢁⣴⣿⠿⣿⣿⣿⣿⣿⣿⣷⣶⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡏⠀⠸⣿⡇⠀⠀⠀⣾⠁⢠⠀⠈⡿⣷⡀⢀⡴⠏⠁⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠀⢹⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠃⠻⠟⢿⣷⡄⠀⣹⡇⠀⠀⢠⠇⠀⢸⡀⢠⠀⠙⠧⠸⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⢻⡟⠀⢀⣼⡿⠋⠉⢻⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⠘⣿⣧⡀⢻⣷⣼⣆⣈⣶⣀⠘⢣⣈⠀⡀⠀⠀⠀⣨⡀⢰⣇⣀⣠⣄⣠⣿⢿⡇⢀⣾⣿⠀⣠⠀⢻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠸⡇⢹⣿⣷⣾⢈⡏⡙⡏⠏⠙⡿⠛⢿⠟⠛⢷⠖⠛⢻⡏⠙⡟⠉⣿⢻⡿⢻⣌⡧⣾⣿⠇⣼⠁⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢷⠀⢻⣿⣿⡟⣷⣷⣧⣇⠀⡇⠀⢸⠀⠀⠘⡆⠀⢠⡇⠀⢸⠀⣿⣿⣾⣾⣿⠁⣾⡏⢸⡏⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢃⠀⠀⠘⢇⠀⢻⣾⠻⣧⡇⢻⠙⢿⠷⣤⠼⣤⣀⣼⣦⣠⣼⢧⣴⠿⡟⠙⡇⢹⣼⠟⣴⡏⢀⡾⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡠⠀⠀⠀⠘⠆⠀⠹⡆⠾⣷⠾⣦⣼⡀⢹⡀⢿⠀⢸⠁⠈⡇⢰⡇⢀⣷⡼⢿⡿⠀⢰⠏⢠⠏⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠀⣉⡓⠚⠗⠚⡦⢾⠳⢴⡗⠻⠓⢛⣹⠅⠉⠀⠀⠁⠀⠏⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠳⠤⣤⣤⣬⣀⣼⣴⡶⠞⠋⠁⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣦⣤⣄⠀⠀⠠⣄⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠉⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⢸⣿⣴⣶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⢿⣦⣀⠈⠛⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⢀⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⠀⠈⠓⠚⠃⠀⠀⠠⠤⠤⠀⢲⠶⠎⠁⠀⣀⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣦⣄⣀⠀⣀⣀⣀⣀⣀⡀⠀⠀⢀⣴⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 \033[0m"""
            )
            break
