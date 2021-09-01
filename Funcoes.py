def perguntar():
    return input("\n O que deseja realizar?\n" +
                 "<I> - Para inserir um usuário\n" +
                 "<P> - Para pesquisar um usuário\n" +
                 "<E> - Para excluir um usuário\n" +
                 "<L> - Para listar um usuário: ").upper()

def inserir(users, login):
    users[login] = [input("Digite o nome: ").upper(),
                    input("Digite a última data de acesso: "),
                    input("Qual a última estação acessada: ").upper()]

def pesquisar(users, login):
    nome = users.get(login)
    if nome is None:
        print("Login **" + login + "** não foi encontrado!")
    else:
        print("\nNome...............: ", str(nome[0]))
        print("Estação............: ", str(nome[2]))
        print("Data último acesso.: ", str(nome[1]))
        print("Login..............: ", str(login))

def excluir(users, login):
    if users.get(login) is not None:
        print("\nUsuário **", str(users[login][0]), "** foi excluído com sucesso.")
        del users[login]
    else:
        print("\nUsuário não encontrado!")

def listar(users):
    for user in users:
        print("\nNome...............: ", str(users[user][0]))
        print("Estação............: ", str(users[user][2]))
        print("Data último acesso.: ", str(users[user][1]))
        print("Login..............: ", str(user), "\n")
