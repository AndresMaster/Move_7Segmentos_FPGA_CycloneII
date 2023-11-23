n = int(input("¿Cuántos digitos tiene tú número?"))

def decimal_a_binario(numero, num_bits):
    # Convierte el número decimal a binario con el formato deseado
    formato_binario = '{:0' + str(num_bits) + 'b}'
    return formato_binario.format(numero)

# Solicitar al usuario la cantidad de bits
num_bits = int(input("Ingresa la cantidad de bits de tus entradas: "))

# Inicializar una lista para almacenar las representaciones binarias
binarios_lista = []

# Almacenar los números del 0 al 9 en binario con la cantidad de bits especificada
for decimal in range (n):
    binario = decimal_a_binario(decimal, num_bits)
    binarios_lista.append(binario)


Num = []
Entradas=input("¿Cómo se llama tu variable de entrada?")
# Obtener la entrada del usuario como una cadena
numero_str = input("Por favor, ingresa tú número: ")
# Crear una lista para almacenar cada dígito
lista_digitos = []
# Agregar cada dígito a la lista
for digito in numero_str:
    if digito.isdigit():
        lista_digitos.append(int(digito))
    else: 
        lista_digitos.append((digito))
    

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
    elif lista_digitos[i]=='P':
        print("”	1111111	”	 when "+	Entradas	+"=	”"+ binarios_lista[i] +"”	 else --_")
    else: 
        "0000000"
        

print("HEX_2 <= ")
for k in range (n-1):
    if lista_digitos[k+1]==0:
        print("”1000000”	when 	"+Entradas+"=”"+ binarios_lista[k+1] +"”else --0")
    elif lista_digitos[k+1]==1:
        print("”	1111001	”	 when "+	Entradas	+"=	” "+ binarios_lista[k+1] +"	”	 else --1")
    elif lista_digitos[k+1]==2:
        print("”	0100100	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"	”	 else --2")
    elif lista_digitos[k+1]==3:
        print("”	0110000	”	 when "+    Entradas	+"=	”	"+ binarios_lista[k+1] +"	”	 else --3")
    elif lista_digitos[k+1]==4:
        print("”	0011001	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"”	 else --4")
    elif lista_digitos[k+1]==5:
        print("”	0010010	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"”	 else --5")
    elif lista_digitos[k+1]==6:
        print("”	0000010	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"”	 else --6")
    elif lista_digitos[k+1]==7:
        print("”	1111000	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"”	 else --7")
    elif lista_digitos[k+1]==8:
        print("”	0000000	”	 when "+	Entradas	+"=	”	"+ binarios_lista[k+1] +"	”	 else --8")
    elif lista_digitos[k+1]==9:
        print("”	0011000	”	 when "+	Entradas	+"=	”"+ binarios_lista[k+1] +"”	 else --9")
    else: 
        "0000000"


print("HEX_1 <= ")
for p in range (n-2):
    if lista_digitos[p+2]==0:
        print("”1000000”	when 	"+Entradas+"=”"+ binarios_lista[p+2] +"”else --0")
    elif lista_digitos[p+2]==1:
        print("”	1111001	”	 when "+	Entradas	+"=	” "+ binarios_lista[p+2] +"	”	 else --1")
    elif lista_digitos[p+2]==2:
        print("”	0100100	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"	”	 else --2")
    elif lista_digitos[p+2]==3:
        print("”	0110000	”	 when "+    Entradas	+"=	”	"+ binarios_lista[p+2] +"	”	 else --3")
    elif lista_digitos[p+2]==4:
        print("”	0011001	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"”	 else --4")
    elif lista_digitos[p+2]==5:
        print("”	0010010	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"”	 else --5")
    elif lista_digitos[p+2]==6:
        print("”	0000010	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"”	 else --6")
    elif lista_digitos[p+2]==7:
        print("”	1111000	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"”	 else --7")
    elif lista_digitos[p+2]==8:
        print("”	0000000	”	 when "+	Entradas	+"=	”	"+ binarios_lista[p+2] +"	”	 else --8")
    elif lista_digitos[p+2]==9:
        print("”	0011000	”	 when "+	Entradas	+"=	”"+ binarios_lista[p+2] +"”	 else --9")
    else: 
        "0000000"
        


print("HEX_0 <= ")
for w in range (n-3):
    if lista_digitos[w+3]==0:
        print("”1000000”	when 	"+Entradas+"=”"+ binarios_lista[w+3] +"”else --0")
    elif lista_digitos[w+3]==1:
        print("”	1111001	”	 when "+	Entradas	+"=	” "+ binarios_lista[w+3] +"	”	 else --1")
    elif lista_digitos[w+3]==2:
        print("”	0100100	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"	”	 else --2")
    elif lista_digitos[w+3]==3:
        print("”	0110000	”	 when "+    Entradas	+"=	”	"+ binarios_lista[w+3] +"	”	 else --3")
    elif lista_digitos[w+3]==4:
        print("”	0011001	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"”	 else --4")
    elif lista_digitos[w+3]==5:
        print("”	0010010	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"”	 else --5")
    elif lista_digitos[w+3]==6:
        print("”	0000010	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"”	 else --6")
    elif lista_digitos[w+3]==7:
        print("”	1111000	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"”	 else --7")
    elif lista_digitos[w+3]==8:
        print("”	0000000	”	 when "+	Entradas	+"=	”	"+ binarios_lista[w+3] +"	”	 else --8")
    elif lista_digitos[w+2]==9:
        print("”	0011000	”	 when "+	Entradas	+"=	”"+ binarios_lista[w+3] +"”	 else --9")
    else: 
        "0000000"
        

