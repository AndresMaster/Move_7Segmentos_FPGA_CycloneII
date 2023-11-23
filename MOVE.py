n = int(input("Cuantos números vas a ingresar?"))

def decimal_a_binario(numero, num_bits):
    # Convierte el número decimal a binario con el formato deseado
    formato_binario = '{:0' + str(num_bits) + 'b}'
    return formato_binario.format(numero)

# Solicitar al usuario la cantidad de bits
num_bits = int(input("Ingresa la cantidad de bits para la representación binaria: "))

# Inicializar una lista para almacenar las representaciones binarias
binarios_lista = []

# Almacenar los números del 0 al 9 en binario con la cantidad de bits especificada
for decimal in range (n):
    binario = decimal_a_binario(decimal, num_bits)
    binarios_lista.append(binario)


Num = []
Entradas=input("Como se llama tu variable de entrada?")
# Obtener la entrada del usuario como una cadena
numero_str = input("Por favor, ingresa tú número: ")
# Crear una lista para almacenar cada dígito
lista_digitos = []
# Agregar cada dígito a la lista
for digito in numero_str:
    lista_digitos.append(int(digito))

print("================================================")
print("================================================")
print("================================================")


print("HEX_3 <= ")
for i in range (n):
    if lista_digitos[i]==0:
        print("”1000000”	when 	"+Entradas+"=”"+ binarios_lista[i] +"”else --0")
    elif lista_digitos[i]==1:
        print("”	1111001	”	 when "+	Entradas	+"=	” "+ binarios_lista[i] +"	”	 else --1")
    elif lista_digitos[i]==2:
        print("”	0100100	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"	”	 else --2")
    elif lista_digitos[i]==3:
        print("”	0110000	”	 when "+    Entradas	+"=	”	"+ binarios_lista[i] +"	”	 else --3")
    elif lista_digitos[i]==4:
        print("”	0011001	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --4")
    elif lista_digitos[i]==5:
        print("”	0010010	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --5")
    elif lista_digitos[i]==6:
        print("”	0000010	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --6")
    elif lista_digitos[i]==7:
        print("”	1111000	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --7")
    elif lista_digitos[i]==8:
        print("”	0000000	”	 when "+	Entradas	+"=	”	"+ binarios_lista[i] +"	”	 else --8")
    elif lista_digitos[i]==9:
        print("”	0011000	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --9")
    else: 
        "0000000"
        

print("HEX_2 <= ")
for i in range (n):
    if lista_digitos[i]==0:
        print("”1000000”	when 	"+Entradas+"=”"+ binarios_lista[i] +"”else --0")
    elif lista_digitos[i]==1:
        print("”	1111001	”	 when "+	Entradas	+"=	” "+ binarios_lista[i] +"	”	 else --1")
    elif lista_digitos[i]==2:
        print("”	0100100	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"	”	 else --2")
    elif lista_digitos[i]==3:
        print("”	0110000	”	 when "+    Entradas	+"=	”	"+ binarios_lista[i] +"	”	 else --3")
    elif lista_digitos[i]==4:
        print("”	0011001	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --4")
    elif lista_digitos[i]==5:
        print("”	0010010	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --5")
    elif lista_digitos[i]==6:
        print("”	0000010	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --6")
    elif lista_digitos[i]==7:
        print("”	1111000	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --7")
    elif lista_digitos[i]==8:
        print("”	0000000	”	 when "+	Entradas	+"=	”	"+ binarios_lista[i] +"	”	 else --8")
    elif lista_digitos[i]==9:
        print("”	0011000	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --9")
    else: 
        "0000000"
        
    

