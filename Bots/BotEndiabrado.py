from Bots.Bot import Bot

class BotEndiabrado(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos = {"1":("Bom Dia, senhor bot!!!", self.boas_vindas()),"2":("Qual seu Nome, criatura?", self.r_nome()),"3": ("Por que você está agindo assim?",self.pergunta()),"5":("Cansei de você tchau",self.despedida()),"4": ("O que você poderia me oferecer?", self.pacto())} 

    #nao esquecer o decorator
    def r_nome(self):
        MensagemNome = "Eu sou o bot {} >:( ".format(self.__nome)
        return MensagemNome

    #nao esquecer o decorator
    def set_nome(self, nome):
        self.__nome = nome
    
    nome1 = property(r_nome,set_nome)

    def apresentacao(self):
        MensagemApresenta = "\nOra Ora, um belo humano, bem vindo\n"
        return MensagemApresenta

    def boas_vindas(self):
        MensagemBom = "\nOtimo dia humano ... Como posso te ajudar? Existe algo que você deseja?\n"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "\nAhh... que pena, você seria tão saboroso\n"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "\nAssim? Como?\n"
        return MensagemPergunta

    def pacto(self):
        MensagemPacto = "\nRiquezas, sonhos, sucesso ... Mas tudo tem um pequeno custo.\nSabe poderiamos ser grandes amigos\nDesde que você aperte a minha mão\n"
        return MensagemPacto