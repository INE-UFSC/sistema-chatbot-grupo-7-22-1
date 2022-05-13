from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        if all(isinstance(x, Bot) for x in lista_bots):
            self.__lista_bots=lista_bots
        self.__bot = None
    
    @property
    def empresa(self):
        return self.__empresa
    
    @empresa.setter
    def empresa(self, nomeEmpresa):
        self.__empresa = nomeEmpresa

    @property
    def lista_bots(self):
        return self.__lista_bots
    
    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    def boas_vindas(self):
        print("Bem vindo ao sistema da empresa", self.empresa)

    def mostra_menu(self):
        print("Os chatbots disponíveis são:")
        for i, bot in enumerate(self.lista_bots):
            print(i, "- Bot:", bot.nome)

    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        i = int(input("Digite com qual chat bot deseja conversar:"))
        self.bot(self.lista_bots[i])

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        self.bot.mostra_comandos()

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        cmd = input("Digite o comando desejado (-1 para sair):")
        if cmd=="-1":
            return True 
        self.bot.executa_comando(cmd)

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot
        self.escolhe_bot()    
        ##mostra mensagens de boas-vindas do bot escolhido
        self.bot.apresentacao()
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            if self.le_envia_comando()==True:
                break
        ##ao sair mostrar a mensagem de despedida do bot
        self.bot.despedida()
