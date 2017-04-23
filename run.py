import random
def run():
    if (bool(random.getrandbits(1))):
        print ("Você se salvou dessa vez, mas lembre-se:\nQuem nasceu pra Magikarp nunca vai ser Gyarados")
        return 1
    else:
    	print("Volte para a batalha, soldado!")
    	return 0
