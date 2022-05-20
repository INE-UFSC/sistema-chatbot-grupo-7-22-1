#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotEndiabrado import BotEndiabrado
from Bots.BotCachorro import BotCachorro
###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Chorão"), BotEndiabrado("Lulu"), BotCachorro("Adolf")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
