from Bots.Bot import Bot

class BotEndiabrado(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.__nome = nome
        self.__comandos = {1:("Bom Dia, senhor bot!!!", self.boas_vindas()),2:("Qual seu Nome, criatura?", self.r_nome()),3: ("Por que você está agindo assim?",self.pergunta()),5:("Cansei de você tchau",self.despedida()),4: ("O que você poderia me oferecer?", self.pacto())} 

    #nao esquecer o decorator
    def r_nome(self):
        MensagemNome = "Eu sou o bot {} >:( ".format(self.__nome)
        return MensagemNome

    #nao esquecer o decorator
    def set_nome(self, nome):
        self.__nome = nome
    
    nome = property(r_nome,set_nome)

    def apresentacao(self):
        MensagemApresenta = "Ora, um belo humano, bem vindo"
        return MensagemApresenta

    def executa_comando(self,cmd):
        return self.__comandos.get(cmd)

    def boas_vindas(self):
        MensagemBom = "Otimo dia humano ... Como posso te ajudar? Existe algo que você deseja?"
        return MensagemBom

    def despedida(self):
        MensagemDespedida = "Ahh... que pena, você seria tão saboroso"
        return MensagemDespedida

    def pergunta(self):
        MensagemPergunta = "Assim? Como?"
        return MensagemPergunta

    def pacto(self):
        MensagemPacto = "Riquezas, sonhos, sucesso ... Mas tudo tem um pequeno custo.\nSabe poderiamos ser grandes amigos\nDesde que você aperte a minha mão"
        return MensagemPacto