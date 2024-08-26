class Ocorrencia:
    reclamacoes = []
    elogios = []
    sugestoes = []

    def __init__(self):
        pass

    def inserir(self, comentario, categoria):
        if(categoria == 1):
            self.elogios.append(comentario)
        elif(categoria == 2):
            self.reclamacoes.append(comentario)
        elif(categoria == 3):
            self.sugestoes.append(comentario)
        else: 
            print("Opção inválida! Tente novamente!")

    def listar(self, categoria):
        if (categoria == 1):
            print("\n**LISTA ELOGIOS**") 
            if (self.elogios == []):
                print("Nenhum elogio encontrado!")
            else:
                for com in range(len(self.elogios)):
                    print("%d - %s" %(com+1, self.elogios[com]))
        elif (categoria == 2):
            print("\n**LISTA RECLAMAÇÕES**")
            if (self.reclamacoes == []):
                print("Nenhuma reclamação encontrada!")
            else:
                for com in range(len(self.reclamacoes)):
	                print("%d - %s" %(com+1, self.reclamacoes[com]))
        elif (categoria == 3):
            if (self.sugestoes == []):
                print("Nenhuma sugestão encontrada!")
            else:
                for com in range(len(self.sugestoes)):
	                print("%d - %s" %(com+1, self.sugestoes[com]))
        else:
            print("Opção inválida! Tente novamente!")   

    def deletar(self, optodos_esp, opdel):
        if (optodos_esp == 1):
            if (opdel == 1):
                self.elogios.clear()
                print("\nTodos os elogios foram apagados com sucesso!")
            elif(opdel == 2):
                self.reclamacoes.clear()
                print("\nTodas as reclamações foram apagadas com sucesso!")
            elif(opdel == 3):
                self.sugestoes.clear()
                print("\nTodas as sugestoes foram apagadas com sucesso!")
            else:
                print("Opção inválida!")
        elif (optodos_esp == 2):
            if(opdel == 1):   
                self.listar(opdel)
                especifico = int(input("\nDigite o número referente ao elogio que deseja apagar: ")) - 1
                if (especifico <= len(self.elogios)):
                    del self.elogios[especifico]
                    print("Elogio apagado com sucesso!")
                else:
                    print("Elogio não encontrado. Tente novamente!")
            elif(opdel == 2):
                self.listar(opdel)
                especifico = int(input("\nDigite o número referente à reclamação que deseja apagar: ")) - 1
                if (especifico <= len(self.reclamacoes)):
                    del self.reclamacoes[especifico]
                    print("Reclamação apagada com sucesso!")
                else:
                    print("Reclamação não encontrada. Tente novamente!")
            elif(opdel == 3):
                self.listar(opdel)
                especifico = int(input("\nDigite o número referente à sugestão que deseja apagar: ")) - 1
                if (especifico <= len(self.sugestoes)):
                    del self.sugestoes[especifico]
                    print("Sugestão apagada com sucesso!")
                else:
                    print("Sugestão não encontrada. Tente novamente!")   