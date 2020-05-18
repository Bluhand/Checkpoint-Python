from funcoes import *

vazamento = {"alberico": ["alberico@gmail.com", "123452"], "gustavo" : ["gustavo@gmail.com", "123456"]}

resp = "S"

while resp == "S":
    print("\nEntre com a opcao correspondente")
    print("Digite 1 para cadastrar um email vazado .")
    print("Digite 2 para mostrar a lista vazamento.")
    print("Digite 3 para verificar se você tem algum vazamento.")
    print("Digite 4 para retirar seu vazamento da lista .")
    print("Digite 5 para sair.")
    opcao = int(input("Qual a opcao escolhida: "))

    if opcao == 1:
        cadastroEmail(vazamento)
    elif opcao == 2:
        exibirEmail(vazamento)
    elif opcao == 3:
        buscarEmail(vazamento)
    elif opcao == 4:
        deletarEmail(vazamento)
    elif opcao == 5:
        break
    else:
        print("Opcao Invalida!")
        print("Tente Novamente!!!!!")