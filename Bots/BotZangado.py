from wsgiref.handlers import format_date_time
from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        super().__init__(nome)
        self.comandos = {'1':("Bom Dia! bot!!!", self.boas_vindas()), 
                         '2':("Qual seu Nome, meu querido?", self.r_nome()), 
                         '3':("Por que você está tão zangado?",self.pergunta())}


    def r_nome(self):
        MensagemNome = "Eu sou o bot {} >:( ".format(self.__nome)
        return MensagemNome

    def apresentacao(self):
        MensagemApresenta = "\nAcho que eu sou obrigado a te ajudar >:(\n"
        return MensagemApresenta

    def boas_vindas(self):
        MensagemBom = "\nQue bom dia o que ta na disney porra \n Você vai embora né não aguenta a pressão?\n"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "\nAté que enfim, não aguntava mais a sua presença\n"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "\nNão te interessa!!! pergunta pra tua mãee \n espero que você nunca mais apareça por aqui\n"
        return MensagemPergunta

    