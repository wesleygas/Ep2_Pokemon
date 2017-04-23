#A função receberá os dois reassamons a lutarem e assumirá o controle dos turnos até que o usuário fuja
#Cada pokémon tem um número na lista de reassamons, teremos que trabalhar com esse número para conseguir
#as specs do pokemon. Ou seja, "wild" é o número do pokémon na lista "ReassaDEX". No caso do "player",
#A lista de specs será puxada do arquivo de save, separada da ReassaDEX(que é só um balde de pokemons)
#Na qual o  index 0 é o nome do jogador(Se ele quiser colocar), e o 1 é o pokémon dele
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