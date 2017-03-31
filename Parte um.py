import json



while True:
	action = input("Você quer 'passear', abrir a 'insperdex' ou 'dormir'? \n").lower()
	if( "dormir" == action): #Condição inicial para começar o jogo: O jogador não quer dormir
		print("Okay então. Sem mais aventuras por hoje :'( ")
		print(". \n. \n.\n.\nZZZZzzzzzzzz'")
		break
	elif(action == "insperdex"):
		print("Abrindo a insperdex!")
		


	else:
		print("Então bora batalhar!")




