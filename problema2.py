#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t = list(input().split())


for i in range(len(t)):
        try: 
            t[i] = int(t[i])
        except:
            pass

rev_t = t[::-1]
tupla = tuple(rev_t)
print(tupla)