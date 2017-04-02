#A função receberá os dois reassamons a lutarem e assumirá o controle dos turnos até que o usuário fuja
def batalha(player, wild):
	while(player["vida"] > 0 and wild["vida"] > 0):
 		 wild["vida"] =  wild["vida"] – ( PoderJogador –  wild["defesa"] )
 		if (wild["vida"] <= 0):
 			return "Parabéns, você saudou a mandioca!"
 		VidaJogador = VidaJogador – (  wild["poder"] – DefesaJogador )
 		if (player["vida"] <= 0):

 			return "YOU HAVE FAILED THIS COUNTRY"