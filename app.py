#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotEndiabrado import BotEndiabrado
###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Chorão"), BotEndiabrado("Lulu")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
