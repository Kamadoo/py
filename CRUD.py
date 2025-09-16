# Início da atividade (PUCPR)
# Autor: João V S M Nunes

# Separação de opções por função:
opcoes = ("(1) • Incluir.\n"
          "(2) • Listar.\n"
          "(3) • Atualizar.\n"
          "(4) • Excluir.\n"
          "(0) • Voltar ao menu principal.\n")
menu = ("(1) • Gerenciar estudantes.\n"
        "(2) • Gerenciar professores.\n"
        "(3) • Gerenciar disciplinas.\n"
        "(4) • Gerenciar turmas.\n"
        "(5) • Gerenciar matrículas.\n"
        "(0) • Sair.\n")
repetir = True

# Lista para armazenar os nomes dos estudantes
estudantes = []

# Criação do loop inicial do Menu Principal.
while repetir:
    while True:
        print("|---= MENU PRINCIPAL =---|\n")
        print(menu)
        opcao = int(input("Digite a opção desejada: "))
        print("\n")
        if opcao == 1:
            print("  -> Opção selecionada: Gerenciar estudantes\n")
            break
        elif opcao in range(2, 6):
            print("Em desenvolvimento\n")
        elif opcao == 0:
            print("   -> Saindo do sistema...\n")
            repetir = False
            break
        else:
            print("   -> Opção inválida. <- \n")
    if not repetir:
        break

    # Fim do loop inicial do Menu Principal/Início do loop secundário.
    while True:
        if opcao == 1:
            print("***|---= [ESTUDANTES] MENU DE OPERAÇÕES =---|***\n")
            print(opcoes)
            opcao2 = int(input("Digite a opção desejada: "))
            print("\n")
            if opcao2 == 1:  # Incluir estudante
                print("===-|Adicionar estudante|-===\n")
                nome = input("➢  Informe o nome do estudante: ")
                estudantes.append(nome)
                print("\n   -> Estudante incluído com sucesso!\n")
            elif opcao2 == 2:  # Listar estudantes
                print("===-|Lista de estudantes|-===\n")
                if estudantes:
                    for i, estudante in enumerate(estudantes, start=1):
                        print(f"{i}. {estudante}")
                    print("\n")
                else:
                    print("Não há estudantes cadastrados.\n")
            elif opcao2 in [3, 4]:  # Atualizar ou Excluir
                print("Em Desenvolvimento\n")
            elif opcao2 == 0:  # Voltar ao menu principal
                print(" -> Voltando ao menu principal...\n")
                break
            else:
                print("   -> Opção inválida. <- \n")
