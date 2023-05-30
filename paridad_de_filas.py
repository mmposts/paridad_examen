cantidad_byts = 8
bytes_a_comprobar = [
    [1,0,0,1,1,1,0,1,1],
    [0,1,1,0,0,1,0,1,0],
    [0,0,1,1,1,0,1,1,1],
    [1,1,0,1,0,1,0,0,0],
    [0,1,1,1,0,0,1,0,0],
    [1,0,1,0,0,1,1,1,1],
    [0,0,1,1,0,0,0,0,1]
]
def parear_numeros(numero_par):
    resto  = numero_par % len(bytes_a_comprobar)

    return bytes_a_comprobar[resto]


