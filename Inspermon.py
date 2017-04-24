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
	fugir = 0
	opFugir = "x"
	exp = ((VidaWild*PoderWild*DefesaWild)/(VidaJogador*PoderJogador*DefesaJogador))*10 #Clacula a experiência em jogo nesta rodada
	dado = input("Escolha um número para jogar na sorte ou 'n' para cancelar: (digite 'wtf' para saber mais) ")
	if(dado == "wtf"):
		print("O dado funciona assim: Você escolhe o número de lados do seu dado\
e, caso tire da metade para cima, seu ataque e vida serão multiplicados pelo valor\
que tirastes no dado. Mas, se for da metade para baixo, estes serão DIVIDIDOS pelo valor tirado")
		dado = input("E aí, vai jogar ou 'n'? Qual o número? ")


	if not dado == 'n':
		dado = int(dado)
		print("Hehehe, vamos lá então! Você escolheu um dado de {} faces".format(dado))
		opFugir = "n"
		sleep(1)
		print("Sorteando",end = ' ')
		for i in range(3):
			print('.', end=' ')
			sleep(1)
		print('\n')
		resultado = random.randint(0,abs(dado))
		print("Você tirou o número {} !".format(resultado))
		if(resultado > (abs(dado)/2)):
			PoderJogador = PoderJogador * resultado
			DefesaJogador = DefesaJogador * resultado
			print("Seus novos atributos são: {0} de poder de ataque e {1} de defesa".format(PoderJogador,DefesaJogador))
		elif(resultado < (abs(dado)/2)):
			PoderJogador = PoderJogador / resultado
			DefesaJogador = DefesaJogador / resultado
			print("Seus novos atributos são: {0} de poder de ataque e {1} de defesa".format(PoderJogador,DefesaJogador))


	if(PoderJogador < DefesaWild):
		PoderJogador = 0
		DefesaWild = 0
	if(PoderWild < DefesaJogador):
		PoderWild = 0
		DefesaJogador = 0
	print("Iniciando a batalha!\n")
	sleep(1)


	while(VidaJogador > 0 and VidaWild > 0 and fugir == 0):
		VidaWild =  VidaWild - ( PoderJogador - DefesaWild )
		if (VidaWild <= 0):
			save[0]["xp"] += exp
			print("Parabéns, você saudou a mandioca e ganhou {} de experiência!".format(exp))

			return 1

		VidaJogador = VidaJogador - (  PoderWild - DefesaJogador )

		if (VidaJogador <= 0):
			save[0]["xp"] -= exp
			print("YOU HAVE FAILED THIS COUNTRY... Ps: E perdeu {} de experiência".format(exp))

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
		if(dado == "n"): #Se a pessoa não utilizou o dado, renove a opção de fugir
			opFugir = "x"


with open('ReassaDEX.json') as arquivo: #Abre o banco de inspermons
	inspermons = json.load(arquivo)
with open('save.json') as arquivo: #Abre o save 
	save = json.load(arquivo)

if(save[0]["primeira_jogada"] == 1): #Verifica se é a primeira vez do jogador e, se sim, abre a escolha do pokémon do player 
	print("Escolha um dos reassamons para jogar com ou digite 'r' para selecionar randomicamente")
	sleep(2)
	for i in inspermons: 
		print(i['nome'])
	escolha = input("\nDigite o nome do reassamon ou 'r' para selecionar aleatoriamente: ")

	if(escolha == 'r'): #Escolha randômica
		a = random.choice(inspermons)
		print("Ok, {} foi escolhido aleatoriamente, estes são os atributos:\n".format(a["nome"]))
		print(a)
		save.append(a)
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

while True: #Rotina básica do Game
	action = input("Você quer 'passear', abrir a 'insperdex' ou 'dormir'? \n").lower()
	if( "dormir" == action): #Condição inicial para começar o jogo: O jogador não quer dormir
		print("Okay então. Sem mais aventuras por hoje :'( ")
		print(". \n. \n.\n.\nZZZZzzzzzzzz'")
		break
	elif(action == "insperdex"): #Caso o jogador queira abrir a insperdex, abrir 
		print("Abrindo a sua insperdex!")
		sleep(1)
		
		if(len(save) >= 3):
			for i in range(2, len(save)):
				print(save[i])
		else:
			print("Você ainda não encontrou nenhum inspermon, vá batalhar seu preguiçoso!")


	else:
		print("Então bora batalhar!\n\n")
		oponente = random.choice(inspermons)

		if oponente in save:
			print("Você encontrou {0}! Prepare-se para a batalha:\n".format(oponente["nome"]))
			sleep(0.5)
		
		else:
			print("Você encontrou {0} pela primeira vez. Adicionando {0} à sua insperdex!\n".format(oponente["nome"]))
			sleep(0.5)
			save.append(oponente)
			print("Prepare-se para a batalha!\n")
			sleep(0.5)


		batalha(save[1],oponente)

		if(save[0]["xp"] == 0):
			pass
		elif(save[0]["xp"] > (save[1]["poder"] + save[1]["poder"])):
			print('PARABAINS; Seu inspermon evoluiu!')
			print("Os stats de {0} foram de {1} para {2} de poder, e de {3} para {4} de defesa *-* "\
				.format(save[1]["nome"],save[1]["poder"],save[1]["poder"]*2,save[1]["defesa"],save[1]["defesa"]*2))
			save[1]["poder"] += save[1]["poder"]
			save[1]["defesa"] += save[1]["defesa"]





with open('save.json','w') as arquivo: #Guarda o save
	json.dump(save,arquivo)

