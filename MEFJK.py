n = int(input("¿Hasta que número necesitas contar?"))
binarios_first = []
binarios_future = []
Selectores = []


def decimal_a_binario(numero, num_bits):
    # Convierte el número decimal a binario con el formato deseado
    formato_binario = '{:0' + str(num_bits) + 'b}'
    return formato_binario.format(numero)

# Solicitar al usuario la cantidad de bits
num_first_future = int(input("Ingresa la cantidad de bits de tus entradas: "))
Selec = int(input("Ingresa la cantidad de bits de tus selectores: "))


for first_in in range (n+1):
    first = decimal_a_binario(first_in, num_first_future)
    binarios_first.append(first)

for future_in in range (n+1):
    future = decimal_a_binario(future_in, num_first_future)
    binarios_future.append(future)

for k in range (n):
    for Selectores_in in range (4):
        Sele = decimal_a_binario(Selectores_in, Selec)
        Selectores.append(Sele)
        
print(Selectores)


    