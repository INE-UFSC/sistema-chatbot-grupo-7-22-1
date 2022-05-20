from wsgiref.handlers import format_date_time
from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {"Bom Dia": self.boas_vindas(), "Qual seu Nome?": self.r_nome(), "Por que você está depressivo?":self.pergunta()}

    #nao esquecer o decorator
    def r_nome(self):
        MensagemNome = "Eu sou ... o bot {} .. desculpa".format(self.__nome)
        return MensagemNome

    #nao esquecer o decorator
    def set_nome(self,nome):
        self.__nome = nome
    
    nome = property(r_nome,set_nome)

    def apresentacao(self):
        MensagemApresenta = "Você não devia ter me escolhido, eu sou inutil :c"
        return MensagemApresenta
    def mostra_comandos(self):
        pass


    def executa_comando(self,cmd):
        return self.__comandos.get(cmd)


    def boas_vindas(self):
        MensagemBom = "O Dia ta tão chuvoso hoje, ainda bem que você chegou :c, eu tava muito sozinho ...\n Você não vai embora né?"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "Por favor não vai embora, ninguem mais ficar comigo ... Eu vou ficar com frio aqui fora :c"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "Ah, eu não sei, acho que é por que ninguêm gosta de mim \n Mas você me deixou melhor :3 \n Sabe... Não consigo ficar bem comigo mesmo, as vezes penso coisas estranhas"
        return MensagemPergunta

    