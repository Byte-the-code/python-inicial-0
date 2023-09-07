from typing import final


print('<---------------------------------->\n\n\n')

# resultados = []
# while True:
#     try:
#         numero = int(input('Ingrese un numero para divir a 100: '))
#         resultado = 100/numero
#     except ZeroDivisionError:
#         print('No se puede divir por 0')
#     except TypeError:
#         print('Solo se puede operar con numeros!!!')
#     except:
#         print('Algo malio sal')
#     else:
#         resultados.append(resultado)
#         break



# numero = input('Ingrese un numero para divir a 100: ')
# try:
#     if numero not in [0,1,2,3,4,5,6,7,8,9]:
#         numero = int(numero)
#         if numero != 0:
#             print(100/numero)
#         else:
#             print('No se puede divir por 0')s
# except:
#     print('Ocurrio algo inesperado')


# try:
#     numero = int(input('Ingrese un numero para divir a 100: '))
#     print(100/numero)
# except:
#     print('No se puede divir por 0')



# resultados = []
# try:
#     numero = int(input('Ingrese un numero para divir a 100: '))
#     resultado = 100/numero
# except ZeroDivisionError:
#     print('No se puede divir por 0')
# except TypeError:
#     print('Solo se puede operar con numeros!!!')
# except:
#     print('Algo malio sal')
# else: #Si todo salio bien
#     resultados.append(resultado)
# finally: #Se ejecuta siempre
#     print('holassss')

# print(resultados)





# try:
#     numero = int(input('Ingrese un numero para divir a 100: '))
#     print(100/numero)
# except ValueError:
#     print('Tenes que ingresar un numero')

# except ZeroDivisionError:
#     print('No se puede divir por 0')

# except Exception as e:
#     print(e)
#     print(type(e).__name__)

try:
    numero = int(input('Ingrese un numero para divir a 100: '))
    if numero == 0:
        raise ZeroDivisionError('Que no podes divir por 0!!!')
    print(100/numero)
except Exception as e:
    print(e)

try:
    numero = int(input('Ingrese un numero para divir a 100: '))
    if not numero == 0:
        print(100/numero)
    else:
        print('Que no podes divir por 0!!!')
except Exception as e:
    print(e)



print('\n\n\n<---------------------------------->')
