import runpy


def menu():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Converter metros para centímetros")
        print("2 - Calcular a área de um círculo")
        print("3 - Calcular a área de um quadrado")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            #runpy.run_path("5.py") opção melhor para usar
            exec(open("5.py").read())
        elif opcao == "2":
            #runpy.run_path("6.py")
            exec(open("6.py").read())
        elif opcao == "3":
            #runpy.run_path("7.py")
            exec(open("7.py").read())
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o menu

if __name__ == "__main__":
    menu()
