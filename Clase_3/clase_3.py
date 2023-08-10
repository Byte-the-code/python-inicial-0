print('<---------------------------------->\n\n\n')

#Listas

profe = ['luca', 'citta', 24, True]
alumno_1 = ['Lisandro', 'ratto', 22 ,True]
alumno_2 = ['Jhunior', 'izarra', 26 ,False]

# print(type(profe))

# print(profe)
# print(alumno_1)
# print(alumno_2)

# print('Mis alumnos son: ')
# print(alumno_1[0] + ' y ' + alumno_2[0])

# print('Hola Byte'[6])
# print('El nombre del alumno 1 es ' + alumno_1[0])


# print(alumno_2[0])
# print(type(alumno_2[0]))
# print(alumno_2[0][3])

# saludo = 'Hola byte'
# saludo[5] = 'B'

# profe[1] = 'Citta Giordano'
# print(profe[1][:5])

# saludo = 'Hola desde Nyte The Code'

# print(saludo[11])
# print(saludo[:11])
# print(saludo[12:])
# print(saludo[:11] + saludo[12:])
# print(saludo[:11] + 'B' + saludo[12:])

# alumno_1 = ['Lisandro', 'ratto', 22 ,True]
# alumno_1 = []
# print(alumno_1)

byte_the_list = ['B', 'Y', 't', 'e', ' ', ' ', 'T', 'h', 'e']
# byte_the_list[1] = 'i'
# print(byte_the_list)

byte_the_list.append(' ')

byte_the_list.extend('Code')


elemento_borrado = byte_the_list.pop(4)
# print(byte_the_list)

# print(elemento_borrado)
# print(byte_the_list)

# print(len(byte_the_list))

# print(byte_the_list.count('e'))
# print(byte_the_list.count(' ') + 1)

# print(byte_the_list.index('Y'))

mi_tupla = (1,2,3,5,2)

# print(mi_tupla)
# print(type(mi_tupla))
# print(mi_tupla[1])
# mi_tupla[1] = 3
# 'hola'[1] = '3'
# print(mi_tupla[:2])
# print(mi_tupla[:-1] + (4,) + (mi_tupla[-1],))

# print(len(mi_tupla))
# print(mi_tupla.count(2))
# print(mi_tupla.index(3))

# str()
# int()
# float()
# complex()
# tuple()
# list()

# print(type(str(5)))
# edad = '24' 
# print('Tengo ' + str(edad) + ' años')

# print(type(int('5')))

# print(int(edad) + 20)

# print(tuple(alumno_2))
# print(list(mi_tupla))
# print(mi_tupla)
# mi_tupla = list(mi_tupla)
# mi_tupla[4] = mi_tupla[3]
# mi_tupla[3] = 4
# mi_tupla = tuple(mi_tupla)
# print(mi_tupla)

tupla_con_anidacion = (
    1, 
    2, 
    [
        1, 
        2, 
        3, 
        (
            'hola',
            True,
            23
        ),
        (
            0,
            []
        )
    ]
)

# print(tupla_con_anidacion[2][4][0])

cursos = [
    [
        'Python',
        [
            'Lisandro',
            'Jhoel',
            'Anthony'
        ]
    ],
    [
        'Desarrollo web',
        [
            'Lorenzo',
            'Pepe',
            'Cachopo'
        ]
    ]
] 

print(cursos[0][0])
print(cursos[0][1])

print(cursos[1][0])
print(cursos[1][1])

print('\n\n\n<---------------------------------->')
