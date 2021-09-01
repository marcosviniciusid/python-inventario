from Funcoes import *
usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios, input("Digite o login: ").upper())
    elif opcao == "P":
        pesquisar(usuarios, input("Digite o login para buscar: ").upper())
    elif opcao == "E":
        excluir(usuarios, input("Qual login excluir? ").upper())
    elif opcao == "L":
        listar(usuarios)
    opcao = perguntar()
