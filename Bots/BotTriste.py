from wsgiref.handlers import format_date_time
from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome
        self.comandos = {"1":("Bom Dia", self.boas_vindas()),"2":( "Qual seu Nome?", self.r_nome()),"3":("Por que você está depressivo?",self.pergunta())}

    #nao esquecer o decorator
    def r_nome(self):
        MensagemNome = "Eu sou ... o bot {} .. desculpa".format(self.__nome)
        return MensagemNome

    #nao esquecer o decorator
    def set_nome(self,nome):
        self.__nome = nome
    
    nome1 = property(r_nome,set_nome)

    def apresentacao(self):
        MensagemApresenta = "\nVocê não devia ter me escolhido, eu sou inutil :c\n"
        return MensagemApresenta

    def boas_vindas(self):
        MensagemBom = "\nO Dia ta tão chuvoso hoje, ainda bem que você chegou :c, eu tava muito sozinho ...\n Você não vai embora né?\n"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "\nPor favor não vai embora, ninguem mais ficar comigo ... Eu vou ficar com frio aqui fora :c\n"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "\nAh, eu não sei, acho que é por que ninguêm gosta de mim \n Mas você me deixou melhor :3 \n Sabe... Não consigo ficar bem comigo mesmo, as vezes penso coisas estranhas\n"
        return MensagemPergunta

    