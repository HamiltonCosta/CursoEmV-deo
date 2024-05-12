def main():
    mood = input('Qual é o seu humor hoje ? (feliz/triste) ')
    if mood.lower() == "triste":
        take_break()
        listen_music()
        drink_coffee()
        print('\nNão se preocupe se estiver se sentindo para baixo.\nAté os melhores programadores enfrentam dias difíceis.\nO importante é cuidar de si mesmo e encontrar maneiras de recarregar suas energias. Você vai superar isso!')
    elif mood.lower() == "feliz":
        print("Estou feliz em ver que você está bem! Vamos codificar e fazer coisas incríveis!")

def take_break():
    print('\nTire um tempo para descansar e relaxar.')

def listen_music():
    print('\nEscute sua música favorita para elevar o ânimo.')

def drink_coffee():
    print('\nAproveite uma deliciosa xicará de café para se animar.')

if __name__ == "__main__":
    main()

