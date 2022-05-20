from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.comandos = {"1": ("Bom dia", "Bom dia, como está você?"), 
                         "2": ("Seu nome", f"Meu nomé é {self.nome}"),
                         "3": ("Quero um conselho", "Não tenha filho"),
                         "4": ("Mensagem de despedida", "Foi cedo")}

    def apresentacao(self):
        return f'Grrrrrr. Meu nome é {self.nome} e eu te odeio!'
    
    def boas_vindas(self):
        return 'Eu não posso acreditar que você me escolheu, GRRRRRR!'

    def despedida(self):
        return 'FINALMENTE, é o dia mais feliz da minha vida. ADEUS!'