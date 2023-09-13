print('<---------------------------------->\n\n\n')

class Ram:
    def __init__(self, fabricante, marca, memoria):
        self.fabricante = fabricante
        self.marca = marca
        self.memoria = memoria

    def __str__(self):
        return f'Soy una ram de {self.memoria}'


class PlacaVideo:
    def __init__(self, fabricante, marca, Vram):
        self.fabricante = fabricante
        self.marca = marca
        self.Vram = Vram

    def __hacer_render(self):
        return ('Generando render 3D... Listo!')

    def renderizar(self):
        return self.__hacer_render()


class PlacaMadre:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

    def __str__(self):
        return f'Soy una placa madre modelo {self.modelo}'

    def sumar(self, num_1, num_2):
        return(num_1 + num_2)


class Computadora:
    necesita_corriente = True

    def __init__(self, color, marca, placa_madre, placa_de_video, ram, contraseña):
        self.color = color
        self.marca = marca
        self.placa_madre = placa_madre
        self.placa_de_video = placa_de_video
        self.ram = ram
        self.__contraseña = contraseña

    def __str__(self):
        return f'Soy una computadora de la marca {self.marca}'

    def prender(self):
        print('La computadora se esta encendiendo!')

    def sumar(self, num_1, num_2):
        return self.placa_madre.sumar(num_1, num_2)

    def hacer_render(self):
        return self.placa_de_video.renderizar()

    def cantidad_de_ram(self):
        count = 0
        for ram in self.ram:
            count += ram.memoria
        return count

    def validar_contraseña(self, contraseña_a_validar):
        return self.__contraseña == contraseña_a_validar

mi_placa_madre = PlacaMadre('Microsoft', 'EX227A')

mi_placa_de_video = PlacaVideo('Nvidia', 'Nvidia GTX', '2GB')

mi_ram_1 = Ram('Microsoft', 'XH772', 2)
mi_ram_2 = Ram('Microsoft', 'XH772', 2)

mi_computadora = Computadora('plateado', 'Microsoft', mi_placa_madre, mi_placa_de_video, [mi_ram_1, mi_ram_2], 'Segura 123')


# contraseña = input('Por favor, ingrese su contraseña: ')


# if mi_computadora.validar_contraseña(contraseña):
#     print('Es la correcta')
# else:
#     print('Acceso bloqueado')

print(mi_computadora.hacer_render())



print('\n\n\n<---------------------------------->')
