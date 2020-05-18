#Cadastro
def cadastroEmail(vazado):
    resp = "S"
    while resp =="S":
        tag = input("Qual o nome desse vazamento? ").upper()
        vazado[tag] = [input("\nEmail vazado: "), input("Senha do Email vazado: ")]
        resp = input("Deseja castrar mais um email? ").upper()

#Exibir
def exibirEmail(vazado):
    for tag, dados in vazado.items():
        print("\nTag.........", tag)
        print("Email.........", dados[0])
        print("Senha.........", dados[1])

#Busca
def buscarEmail(vazado):
    busca = input("Qual o seu nome:  ")
    lista = vazado.get(busca)
    if lista != None:
        print("\nEmail......... ", lista[0])
        print("Senha........... ", lista[1])
    else:
        print("Vazamento nao encontrado")

#Deletar
def deletarEmail(vazado):
    deletar = input("Qual o seu nome: ")
    if vazado.get(deletar) != None:
        del vazado[deletar]
    print("Vazamento excluido")