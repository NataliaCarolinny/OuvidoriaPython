import classe

x = 1

ocorrencia = classe.Ocorrencia()

while (x!=0):
    print("\n\n***SISTEMA DE OUVIDORIA***\nDigite a opção da operação que deseja realizar\n")
    print("1- Inserir sugestão, elogio ou reclamação;\n2- Listar todos os comentários realizados;\n3- Deletar informações;\n0 - Sair do sistema")
    x = int(input("\nOpção: "))
    if (x == 1): 
        print("\n**INSERIR**")
        opinserir = int(input("1- Elogio\n2- Reclamação\n3- Sugestão\n\nOpção: "))
        comentario = input("\nDigite seu comentário: ")
        ocorrencia.inserir(comentario, opinserir)
    elif (x == 2):
        categoria = int(input("\nListar:\n1- Elogios\n2- Reclamações\n3- Sugestões\nOpção: "))
        ocorrencia.listar(categoria)
    elif (x == 3):
        print("\n**DELETAR INFORMAÇÕES**\n1- Apagar todos os comentários;\n2- Apagar comentario especifico.")
        optodos_esp = int(input("Opção: "))
        if (optodos_esp == 1):
            opdel = int(input("\nDeletar: \n1- Elogios\n2- Reclamações\n3- Sugestões\nOpção: "))
        elif (optodos_esp == 2):
            print("\n**APAGANDO COMENTARIO**")
            opdel = int(input("Deletar comentário de: \n1- Elogios\n2- Reclamações\n3- Sugestões\nOpção: "))
        else:
            print("Opção inválida!")
        ocorrencia.deletar(optodos_esp, opdel)
    elif (x != 0):
        print("Opção inválida! Tente novamente!")

