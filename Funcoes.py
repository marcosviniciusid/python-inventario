def perguntar():
    return input("O que deseja realizar?\n" +
                "<I> - Para inserir um usuário\n" +
                "<P> - Para pesquisar um usuário\n" +
                "<E> - Para excluir um usuário\n" +
                "<L> - Para listar um usuário: ").upper()

def inserir(users):
    users[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]

def pesquisar(users):
    login = input("Digite o login para buscar: ").upper()
    nome = users.get(str(login))

    if nome is None:
        print("Login **"+login+"** não foi encontrado!")
    else:
        print("Nome...............: ", str(nome[0]))
        print("Estação............: ", str(nome[2]))
        print("Data último acesso.: ", str(nome[1]))
        print("Login..............: ", str(login))

def excluir(users):
    login = input("Qual login excluir? ").upper()
    del users[login]
    print("Usuário **", str(users[login][0]), "** foi excluído com sucesso.")

def listar(users):
    for user in users:
        print("Nome...............: ", str(users[user][0]))
        print("Estação............: ", str(users[user][2]))
        print("Data último acesso.: ", str(users[user][1]))
        print("Login..............: ", str(user), "\n")
