#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = list(input().split())
t2 = list(input().split())

def convertirNum(lista):
    for i in range(len(lista)):
        try: 
            lista[i] = int(lista[i])
        except:
            pass
    return lista

lista_t1 = convertirNum(t1)
lista_t2 = convertirNum(t2)

tupla_t1 = tuple(lista_t1)
tupla_t2 = tuple(lista_t2)

output = tupla_t2 + tupla_t1 + tupla_t2

print(output)
