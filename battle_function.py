#A função receberá os dois reassamons a lutarem e assumirá o controle dos turnos até que o usuário fuja
#Cada pokémon tem um número na lista de reassamons, teremos que trabalhar com esse número para conseguir
#as specs do pokemon. Ou seja, "wild" é o número do pokémon na lista "ReassaDEX". No caso do "player",
#A lista de specs será puxada do arquivo de save, separada da ReassaDEX(que é só um balde de pokemons)
#Na qual o  index 0 é o nome do jogador(Se ele quiser colocar), e o 1 é o pokémon dele
def batalha(player, wild):
	VidaJogador = save[1]["vida"]
	PoderJogador = save[1]["poder"]
	DefesaJogador = save[1]["defesa"]
	VidaWild = Reassadex[wild]["vida"]
	PoderWild = Reassadex[wild]["poder"]
	DefesaWild = Reassadex[wild]["defesa"]
	fugir = False
	opFugir = "x"

	while(VidaJogador > 0 and VidaWild > 0 and fugir = False):
 		 VidaWild =  VidaWild – ( PoderJogador –  DefesaWild)
 		if (VidaWild <= 0):
 			return "Parabéns, você saudou a mandioca!"

 		VidaJogador = VidaJogador – (  PoderWild – DefesaJogador )

 		if (VidaJogador <= 0):

 			return "YOU HAVE FAILED THIS COUNTRY"
 		
 		Print("Resumo da rodada:\nSua vida: {0}\nVida do oponente:{1}\n".format(VidaJogador,VidaWild))
 		
 		while(opFugir != "s" and != "n"):
 			opFugir = input("Quer tentar fugir? (s/n)")
 			if(opFugir == "s"):
 				fugir = run()
 			elif(opFugir == "n"):
 				break
 			else:
 				print("Opção inválida, tente novamente")