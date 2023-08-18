

print('<---------------------------------->\n\n\n')

# valor = 7
# valor_2 = 10
# valor_3 = 20

# print('Valor es igual a', valor, 'pero valor 2 es igual a', valor_2, 'y valor 3 es', valor_3)
# print('Valor es igual a {}, pero valor 2 es igual a {}'.format(valor, valor_2))
# print(f'valor es igual a {valor} pero valor 2 es igual a {valor_2} y valor 3 es {valor_3}')


# contador = 10
# while contador > 0:
#     contador -= 1
#     print('Esto no se termina massss, como tus clases Luca', contador)

# asistencia = []
# hay_algun_alumno_mas = input('Hay algun alumno? (si/no): ')

# while hay_algun_alumno_mas == 'si':
#     alumno = input('Ingrese el nombre del alumno: ')
#     asistencia.append(alumno)
#     hay_algun_alumno_mas = input('Hay algun otro alumno? (si/no): ')

# if asistencia:
#     print(f'los alumnos que asistieron hoy son: {asistencia}')
# else:
#     print('No vino nadie, se hicieron la chupina')


# contador = 10
# while contador > 0:
#     contador -= 1
#     if contador == 2:
#         continue
#     print('El contador es impar y su valor es ',contador)


# asistencia = []
# hay_alguien_mas = 'si'

# while hay_alguien_mas == 'si':
#     nombre = input('Ingrese el nombre : ')
#     horario = 2
#     edad = int(input('Ingresa tu edad'))
#     if edad > 18:
#         if horario == 2:
#             pass
#         elif horario == 4:
#             pass
#         elif horario > 5:
#             pass
#     else:
#         print('sos menor')

#     if nombre == 'claudio':
#         continue

#     if nombre == 'policia':
#         break

#     print('cobrale 100 pesos')
#     asistencia.append(nombre)

#     if len(asistencia) == 4:
#         break

#     hay_alguien_mas = input('Hay alguien mas? (si/no): ')

# else:
#     print('Ya no queda mas gente, se termino la noche')


# edad = 20
# if edad > 18:
#     pass
# else:
#     print('sos menor')

# nombres = ['pepe', 'juan', 'martin', 'luca']

# for nombre in nombres:
#     if nombre == 'luca':
#         print('Aca esta el profe')

# numeros = [1,2,3,4,5,6,7]

# for numero in numeros:
#     if numero %2 == 0:
#         print('Este es par', numero)
#     else:
#         print('Este es impar', numero)


# animales = ['gato', 'perro', 'canguro', 'humano', 'Unicornio']

# for animal in animales:
#     if animal in ['gato', 'perro']:
#         print(f'El {animal} camina en 4 patas')

#     elif animal in ['canguro', 'humano']:
#         print(f'El {animal} camina en 2 patas')
    
#     else:
#         print(f'No conozco a {animal}')

# print('Termine de catalogar!')

# nombre = 'Byte The Code'

# for elemento in nombre:
#     print(elemento)


# EJEMPLO DE POR QUE NO HAY QUE MODIFICAR EL ELEMENTO QUE ESTOY ITERANDO
# numeros = [1,2,3,4,5,6,7] 

# contador = 0
# for numero in numeros:
#     print(numero)
#     if numero %2 == 0: #si es par
#         del numeros[contador]
#     contador += 1

# print(numeros)


# for persona in range(10):
#     nombre = input('Ingrese su nombre y pase: ')

# print(type(range(10)))

for persona in range(2):
    nombre = input('Ingrese su nombre y pase: ')
    if nombre == 'policia':
        break
else:
    print('Ya entraron todos')

print('\n\n\n<---------------------------------->')
