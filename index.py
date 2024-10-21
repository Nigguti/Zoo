class Animal:
    def __init__(self, nome, habito_alimentar, comportamento):
        self.nome = nome
        self.habito_alimentar = habito_alimentar
        self.comportamento = comportamento

animais = [
    Animal(nome='Tigre', habito_alimentar='Carnívoro', comportamento='Selvagem'),
    Animal(nome='Leão', habito_alimentar='Carnívoro', comportamento='Selvagem'),
    Animal(nome='Urso', habito_alimentar='Carnívoro', comportamento='Selvagem'),

    Animal(nome='Girafa', habito_alimentar='Herbívoro', comportamento='Selvagem'),
    Animal(nome='Elefante', habito_alimentar='Herbívoro', comportamento='Selvagem'),
    Animal(nome='Zebra', habito_alimentar='Herbívoro', comportamento='Selvagem')
]

#regras
def habitoAlimentarHerbivoro():
    for animal in animais:
        if animal.habito_alimentar == 'Herbívoro':
            print(f'\t{animal.nome} come plantas')

def listaSelvagem():
    for animal in animais:
        if animal.comportamento == 'Selvagem':
            print(f'\t{animal.nome} são {animal.comportamento}')

def verificarCarnivoro():
    for animal in animais:
        if  animal.habito_alimentar == 'Carnívoro' and animal.comportamento == 'Selvagem':
            print(f'\t{animal.nome} é {animal.comportamento}')
            

print('\n\t1.Existe animais que comem plantas na lista?\n')
habitoAlimentarHerbivoro()
print('===================================================')

print('\t2.Listar os selvagens\n')
listaSelvagem()
print('===================================================')

print('\t3.Verificar se todos os carnívoros são selvagens\n')
verificarCarnivoro()
