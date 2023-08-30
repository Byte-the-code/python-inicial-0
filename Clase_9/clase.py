

print('<---------------------------------->\n\n\n')


# ahora_si = 'esta VEZ NO ME equivoCO'
# print(ahora_si.capitalize())
# print(ahora_si.upper().split(' '))

# data_dict = {}
# data = 'data[0]=info' 
# info_procesada = data.replace('data[','').replace(']', '').split('=')
# data_dict[info_procesada[0]] = info_procesada[1]
# print(data_dict)

# print('hola, lucas'.replace('lucas', 'luca'))

# frutas = ['banana', 'naranja']
# frutas.insert(1, 'uva')
# print(frutas)


# lista = [1, 2, 3]

# segunda_lista = lista.copy()

# lista.append(4)

# print(segunda_lista)

# {1,2,3}
# {'numero_1':1, 'numero_2':2, 'numero_3':3}



# colores = {'verde':'green', 'azul':'blue'}
# print(colores.get('rojo', 'No la tengo pa'))

# asistencias = {
#     'gabriela': 'p',
#     'jhoel': 'p',
#     'lisandro': 'p',
#     'carlos': 'a'
# }

# with open('test.txt', 'a') as archivo:
#     for key, value in asistencias.items():
#         archivo.write(f'{key} - {value}\n')
#     archivo.write('-------------------\n')


# with open('data_to_read.txt', 'r') as data:
#     print('Las columnas son: \n')
#     print(data.readline(),'\n\n')
#     print('Los datos son:\n')
#     for line in data.readlines():
#         print(line)


# with open('data_to_read.txt', 'r') as data:
#     data.seek(60)
#     print('Los datos son:\n')
#     for line in data.readlines():
#         print(line)

# with open('data_to_read2.txt', 'r') as data:    
#     data.seek(11)
#     print(data.readline())

# new_data = {}

# with open('test.txt', 'r') as data:
#     for line in data.readlines():
#         alumno, asistencias = line.split(' - ')
#         asistencias = asistencias.replace('\n', '')
        
#         asistencia = input(f'El alumno {alumno} asistio?: ')
#         new_data[alumno] = f'{asistencias} - {asistencia}'

# with open('test.txt', 'w') as archivo:
#     for key, value in new_data.items():
#         archivo.write(f'{key} - {value}\n')


print('\n\n\n<---------------------------------->')
