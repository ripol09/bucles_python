# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']

print ( "la lista completa " , colores )

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...

for color in colores :
    print ( "los elementos de la lista " , color )

# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...

for i in range ( len ( colores )):
    print ( "indice : " , i , " color " , colores [ i ] )

print("terminamos!")