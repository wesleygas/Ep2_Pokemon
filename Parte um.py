#import battle_function
import json
import random
from time import sleep

def batalha(player, wild):
	VidaJogador = player["vida"]
	PoderJogador = player["poder"]
	DefesaJogador = player["defesa"]
	VidaWild = wild["vida"]
	PoderWild = wild["poder"]
	DefesaWild = wild["defesa"]
	fugir = False
	opFugir = "x"

	while(VidaJogador > 0 and VidaWild > 0 and fugir == 0):
		VidaWild =  VidaWild - ( PoderJogador - DefesaWild )
		if (VidaWild <= 0):
			print("Parabéns, você saudou a mandioca!")

			return 1

		VidaJogador = VidaJogador - (  PoderWild - DefesaJogador )

		if (VidaJogador <= 0):
			print("YOU HAVE FAILED THIS COUNTRY")

			return 0
		
		print("Resumo da rodada:\nSua vida: {0}\nVida do oponente:{1}\n".format(VidaJogador,VidaWild))
		
		while(opFugir != "s" and opFugir != "n"):
			opFugir = input("Quer tentar fugir? (s/n)")
			if(opFugir == "s"):
				
				fugir = random.getrandbits(1)
				if(fugir == 1):
					print ("Você se salvou dessa vez, mas lembre-se:\nQuem nasceu pra Magikarp nunca vai ser Gyarados")
					return 'fuga'

				else:
					print("Ninguém vai fugir não...Volte para a batalha, soldado!")
			elif(opFugir == "n"):
				
				break
			else:
				print("Opção inválida, tente novamente")
		opFugir = "x"


with open('ReassaDEX.json') as arquivo:
	inspermons = json.load(arquivo)
with open('save.json') as arquivo:
	save = json.load(arquivo)

if(save[0]["primeira_jogada"] == 1):
	print("Escolha um dos reassamons para jogar com ou digite 'r' para selecionar randomicamente")
	sleep(2)
	for i in inspermons:
		print(i['nome'])
	escolha = input("\nDigite o nome do reassamon ou 'r' para selecionar aleatoriamente: ")

	if(escolha == 'r'):
		save.append(random.choice(inspermons))
		save[0]["primeira_jogada"] = 0
	else:

		for i in inspermons:
			if(i["nome"] == escolha):
				save.append(i)
				print("Parabains, escolhestes o {}, estes são os atributos\n".format(escolha))
				print(i)
				save[0]["primeira_jogada"] = 0
				break
		if(save[0]["primeira_jogada"] == 1):	
			print("Não entendi o que você escreveu...Se ferrou! Vai vir qualquer um mesmo")
			save.append(random.choice(inspermons))
			save[0]["primeira_jogada"] = 0
		
	with open('save.json','w') as arquivo:
		json.dump(save,arquivo)

while True:
	action = input("Você quer 'passear', abrir a 'insperdex' ou 'dormir'? \n").lower()
	if( "dormir" == action): #Condição inicial para começar o jogo: O jogador não quer dormir
		print("Okay então. Sem mais aventuras por hoje :'( ")
		print(". \n. \n.\n.\nZZZZzzzzzzzz'")
		break
	elif(action == "insperdex"):
		print("Abrindo a sua insperdex!")
		


	else:
		print("Então bora batalhar!")
		batalha(save[1],random.choice(inspermons))



with open('save.json','w') as arquivo:
	json.dump(save,arquivo)

