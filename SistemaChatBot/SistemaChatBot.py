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
        for i, bot in enumerate(self.lista_bots()):
            print(i, "- Bot:", bot.nome, ":", bot.boas_vindas)

    
    def escolhe_bot(self):
        pass
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        i = int(input("Digite com qual chat bot deseja conversar:"))
        self.bot(self.lista_bots[i])

    def mostra_comandos_bot(self):
        self.bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
