from time import sleep

def temporizador(tempo):
    while tempo >= 0:
        print(tempo)
        tempo -= 1
        sleep(1)
    print('O tempo acabou!')


tempo = int(input('Digite o tempo em segundos: '))
temporizador(tempo)
