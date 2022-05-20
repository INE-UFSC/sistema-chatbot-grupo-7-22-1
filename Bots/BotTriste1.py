from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.comandos = {"1": ("Bom dia", "Não tão bom para mim mas espero que o seu esteja indo bem..."), 
                         "2": ("Seu nome", f"Meu nomé é {self.nome}"),
                         "3": ("Quero um conselho", "Quando foi a ultima vez que você chorou? Externalizar os sentimentos é saudável!"),
                         "4": ("Mensagem de despedida", "Mas já? Vais me abandonar também?")}

    def apresentacao(self):
        return f'O-Oi, me chamo {self.nome}. Esse parece um nome triste...?'
    
    def boas_vindas(self):
        return 'Eu... Eu agradeço por me escolher. Estava muito triste e solitario antes de você chegar.'

    def despedida(self):
        return 'No final das contas, todos se vão, não é mesmo...? Será que o problema sou eu? Até mais...'