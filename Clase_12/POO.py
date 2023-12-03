print('<---------------------------------->\n\n\n')



class Computadora:
    necesita_corriente = True
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def prender(self):
        print('La computadora se esta encendiendo!')

    def sumar(self, num_1, num_2):
        return(num_1 + num_2)

mi_computadora = Computadora('plateado', 'windows')
mi_segunda_computadora = Computadora('negra', 'mac')
mi_tercer_computadora = Computadora('blanca', 'razer')

class Gato:
    especie = 'Felino' #Atributo de clase

    def __init__(self, color, edad):
        self.color = color #Atributo de instancia
        self.edad = edad #Atributo de instancia

    def rompe_muebles(self):
        print(f'El gato {self.color} esta rompiendo la pata de la mesa')

    def es_viejo(self):
        if self.edad > 4:
            print('El gato es viejo')
        else:
            print('El gato es joven')

cachopo = Gato('gris', 1)
odin = Gato('Negro', 5)

# cachopo.es_viejo()
# odin.sumar(10,5)
resultado = mi_computadora.sumar(10,5)
print(resultado)

test=321

print('\n\n\n<---------------------------------->')
