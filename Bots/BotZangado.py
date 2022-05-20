from wsgiref.handlers import format_date_time
from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {"Bom Dia! bot!!!": self.boas_vindas(), "Qual seu Nome, meu querido?": self.r_nome(), "Por que você está tão zangado?":self.pergunta()}


    def r_nome(self):
        MensagemNome = "Eu sou o bot {} >:( ".format(self.__nome)
        return MensagemNome

    def set_nome(self,nome):
        self.__nome = nome
    
    nome = property(r_nome,set_nome)

    def apresentacao(self):
        MensagemApresenta = "Acho que eu sou obrigado a te ajudar >:("
        return MensagemApresenta

    def executa_comando(self,cmd):
        return self.__comandos.get(cmd)

    def boas_vindas(self):
        MensagemBom = "Que bom dia o que ta na disney porra \n Você vai embora né não aguenta a pressão?"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "Até que enfim, não aguntava mais a sua presença"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "Não te interessa!!! pergunta pra tua mãee \n espero que você nunca mais apareça por aqui"
        return MensagemPergunta

    