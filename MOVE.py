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

print("library ieee;")
print("use ieee.std_logic_1164.all;")
print("use ieee.numeric_std.all;")

print("entity MEF_MyName is")
print("    port ")
print("    (")
print("	 Clk_i, X1, X0 : in std_logic;")
print("	 HEX_3, HEX_2, HEX_1, HEX_0 : out std_logic_vector(6 downto 0)")
print("    );")
print("end MEF_MyName;")

print("architecture Behavioral of MEF_MyName is")
print("component FFJK is")
print("    port ")
print("    (")
print("	 J, K, Clk_i : in std_logic;")
print("	 Q_o          : out std_logic")
print("    );")
print("end component;")

print("signal A, B, C, D, E, F, JsA, KsA, JsB, KsB, JsC, KsC, JsD, KsD, JSE, KSE, JSF, KSF, clk_div : std_logic := '0';")
print("signal Entradas : std_logic_vector(4 downto 0);")

print("begin")

print("clock_div : entity work.clk_div generic map")
print("	(")
print("		DIV_TICKS => 10e6")
print("	)")
print("	port map")
print("	(")
print("		 clk_i 	=> Clk_i,")
print("		 clk_o	=> clk_div")
print("	);")


# Conexiones de los componentes FFJK

# Configuración de FFJKF
print("FFJKF: FFJK port map ")
print("    (")
print("    Clk_i => clk_div ,")
print("    J => JsF,")
print("    K => KsF ,")
print("    Q_o => F")
print("    );")

# Configuración de FFJKE
print("FFJKE: FFJK port map ")
print("    (")
print("    Clk_i => F ,")
print("    J => JsE,")
print("    K => KsE ,")
print("    Q_o => E")
print("    );")

# Configuración de FFJKD
print("FFJKD: FFJK port map ")
print("    (")
print("    Clk_i => E ,")
print("    J => JsD,")
print("    K => KsD ,")
print("    Q_o => D")
print("    );")

# Configuración de FFJKC
print("FFJKC: FFJK port map ")
print("    (")
print("    Clk_i => D ,")
print("    J => JsC,")
print("    K => KsC,")
print("    Q_o => C")
print("    );")

# Configuración de FFJKB
print("FFJKB: FFJK port map ")
print("    (")
print("    Clk_i => C ,")
print("    J => Jsb,")
print("    K => Ksb ,")
print("    Q_o => B")
print("    );")

# Configuración de FFJKA
print("FFJKA: FFJK port map ")
print("    (")
print("    Clk_i => B,")
print("    J => Jsa,")
print("    K => KsA,")
print("    Q_o => A")
print("    );")

# Asignaciones de las señales JSA, JSB, JSC, JSD, JSE, JSF, KSA, KSB, KSC, KSD, KSE, KSF

# Asignación de JSA
print("JSA    <=    (not A and not B and not C and not D and not E and not F and X1 and not X0) or (A and not B and not C and F) or (A and not B and not C and E) or (A and not B and not C and D) or (A and not B and C and not D and not E and not F) or (A and not B and not D and not E and not F and not X1 and X0);")

# Asignación de JSB
print("JSB    <=    (not A and B and not X1 and X0) or (not A and B and F) or (not A and B and E) or (not A and B and D) or (not A and B and C) or (A and not B and not C and not D and not E and not F) or (A and not B and not C and not D and not E and X1 and not X0);")

# Asignación de JSC
print("JSC    <=    (not A and not B and D and E and F and not X1 and X0) or (not A and not B and C) or (not A and B and not C and not D and not E and not F) or (not A and C and F) or (not A and C and E) or (not A and C and D) or (A and not B and not C and not D and not E and not F) or (A and not B and not C and not D and not E and X1 and not X0) or (not A and B and not C and not D and not E and X1 and not X0) or (not A and B and not D and not E and not F and not X1 and X0);")

# Asignación de JSD
print("JSD    <=    (not A and not B and E and F and not X1 and X0) or (not A and not B and D) or (not A and B and not D and not E and not F) or (not A and D and F) or (not A and D and E) or (A and not B and not D and not E and not F) or (not B and not C and D and F) or (not B and not C and D and E) or (not A and not B and not E and not F and X1 and not X0) or (not A and B and not D and not E and X1 and not X0) or (not A and B and not E and not F and not X1 and X0) or (A and not B and not C and not D and not E and X1 and not X0) or (A and not B and not C and not E and not F and not X1 and X0);")

# Asignación de JSE
print("JSE    <=    (not A and not B and not C and F and not X1 and X0) or (not A and not B and not C and E) or (not A and not B and not D and F and not X1 and X0) or (not A and not B and not D and E) or (not A and not E and not F and X1 and not X0) or (not A and E and not X1 and X0) or (not A and E and F) or (not A and B and not E and not F) or (not B and not C and E and F) or (A and not B and not C and not E and not F) or (A and not B and not D and not E and not F) or (not A and B and not E and X1 and not X0) or (A and not B and not C and not E and X1 and not X0) or (A and not B and not C and not F and not X1 and X0);")

# Asignación de JSF
print("JSF    <=    (not A and not B and not C and F) or (not A and not X1 and X0) or (not A and X1 and not X0) or (not A and not B and not D and F) or (not A and not B and not E and F) or (not A and C and D and E and not F) or (not A and B and not F) or (not B and not C and not X1 and X0) or (not B and not C and X1 and not X0) or (A and not B and not C and not F) or (A and not B and not D and not E and not F);")

# Asignación de KSA
print("KSA    <=    (not A) or (not B and not C and not D and not E and not F) or (not B and not C and not D and not E and X1) or (not B and not C and X1 and X0) or (not B and not D and not E and not F and X0);")

# Asignación de KSB
print("KSB    <=    (not A and not B) or (not A and not C and not D and not E and not F) or (not A and not C and not D and not E and X1) or (not A and X1 and X0) or (not B and not C and F) or (not B and not C and E) or (not B and not C and D) or (not B and C and not D and not E and not F) or (not B and not D and not E and not F and X0);")

# Asignación de KSC
print("KSC    <=    (not A and not B and not C) or (not A and X1 and X0) or (not A and not C and F) or (not A and not C and E) or (not A and not C and D) or (not A and B and C and not D and not E and not F) or (not B and not C and F) or (not B and not C and E) or (not B and not C and D) or (A and not B and C and not D and not E and not F) or (not A and not B and not D and not E and not F and X1) or (not A and B and not D and not E and not F and X0) or (not A and B and not D and not E and F and X1) or (A and not B and not D and not E and not F and X0);")

# Asignación de KSD
print("KSD    <=    (not A and not B and not D) or (not A and not B and not C and E and F and X0) or (not A and X1 and X0) or (not A and not D and F) or (not A and not D and E) or (not A and B and D and not E and not F) or (not B and not C and not D and F) or (not B and not C and not D and E) or (A and not B and not C and D and not E and not F) or (not B and not C and X1 and X0) or (not B and not D and not E and not F and X0) or (not A and not B and not E and not F and X1) or (not A and B and not E and not F and X0) or (not A and B and not E and F and X1) or (A and not B and not C and not E and F and X1);")

# Asignación de KSE
print("KSE    <=    (not A and not B and not E) or (not A and not B and not C and F and X0) or (not A and not B and not D and F and X0) or (not A and not E and F) or (not A and B and E and not F) or (not B and not C and not E and F) or (A and not B and not C and E and not F) or (not B and not D and not E and not F and X0) or (not A and not B and not F and X1) or (not A and not B and C and D and not F) or (not A and not B and C and D and X1) or (not A and B and not F and X0) or (not A and B and F and X1) or (A and not B and not C and F and X1) or (A and not B and not C and not F and X0);")

# Asignación de KSF
print("KSF    <=    (not A and not B and not C and not F) or (not A and not D and X0) or (not A and not B and not D and not F) or (not A and not B and not E and not F) or (not A and C and D and E and F) or (not A and B and F) or (not A and B and X1) or (A and not B and not C and F) or (not B and not C and X0) or (not B and not C and X1) or (not B and not D and not E and not F and X0) or (not B and not D and not E and not F and X1) or (not A and F and X1) or (not A and not F and X0);")


print("Entradas <= B & C & D & E & F;")







print("HEX_3 <= ")
for i in range (n):
    if lista_digitos[i]==0:
        print('"1000000"	when 	'+Entradas+'="'+ binarios_lista[i] +'" else --0')
    elif lista_digitos[i]==1:
        print('"1111001"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --1')
    elif lista_digitos[i]==2:
        print('"0100100"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --2')
    elif lista_digitos[i]==3:
        print('"0110000"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --3')
    elif lista_digitos[i]==4:
        print('"0011001"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --4')
    elif lista_digitos[i]==5:
        print('"0010010"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --5')
    elif lista_digitos[i]==6:
        print('"0000010"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --6')
    elif lista_digitos[i]==7:
        print('"1111000"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --7')
    elif lista_digitos[i]==8:
        print('"0000000"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --8')
    elif lista_digitos[i]==9:
        print('"0011000"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --9')
    elif lista_digitos[i]=='P':
        print('"1111111"	when    '+Entradas+'="'+ binarios_lista[i] +'" else --_')
    else: 
        "0000000"
print('"1111111";')          

print("HEX_2 <= ")
for k in range (n-1):
    if lista_digitos[k+1]==0:
        print('"1000000"	when 	'+Entradas+'="'+ binarios_lista[k+1] +'" else --0')
    elif lista_digitos[k+1]==1:
        print('"1111001"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --1')
    elif lista_digitos[k+1]==2:
        print('"0100100"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --2')
    elif lista_digitos[k+1]==3:
        print('"0110000"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --3')
    elif lista_digitos[k+1]==4:
        print('"0011001"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --4')
    elif lista_digitos[k+1]==5:
        print('"0010010"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --5')
    elif lista_digitos[k+1]==6:
        print('"0000010"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --6')
    elif lista_digitos[k+1]==7:
        print('"1111000"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --7')
    elif lista_digitos[k+1]==8:
        print('"0000000"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --8')
    elif lista_digitos[k+1]==9:
        print('"0011000"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --9')
    elif lista_digitos[k+1]=='P':
        print('"1111111"	when    '+Entradas+'="'+ binarios_lista[k+1] +'" else --_')
    else: 
        "0000000"
print('"1111111";')      

print("HEX_1 <= ")
for p in range (n-2):
    if lista_digitos[p+2]==0:
        print('"1000000"	when 	'+Entradas+'="'+ binarios_lista[p+2] +'" else --0')
    elif lista_digitos[p+2]==1:
        print('"1111001"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --1')
    elif lista_digitos[p+2]==2:
        print('"0100100"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --2')
    elif lista_digitos[p+2]==3:
        print('"0110000"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --3')
    elif lista_digitos[p+2]==4:
        print('"0011001"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --4')
    elif lista_digitos[p+2]==5:
        print('"0010010"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --5')
    elif lista_digitos[p+2]==6:
        print('"0000010"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --6')
    elif lista_digitos[p+2]==7:
        print('"1111000"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --7')
    elif lista_digitos[p+2]==8:
        print('"0000000"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --8')
    elif lista_digitos[p+2]==9:
        print('"0011000"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --9')
    elif lista_digitos[p+2]=='P':
        print('"1111111"	when    '+Entradas+'="'+ binarios_lista[p+2] +'" else --_')
    else: 
        "0000000"
print('"1111111";')           


print("HEX_0 <= ")
for w in range (n-3):
    if lista_digitos[w+3]==0:
        print('"1000000"	when 	'+Entradas+'="'+ binarios_lista[w+3] +'" else --0')
    elif lista_digitos[w+3]==1:
        print('"1111001"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --1')
    elif lista_digitos[w+3]==2:
        print('"0100100"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --2')
    elif lista_digitos[w+3]==3:
        print('"0110000"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --3')
    elif lista_digitos[w+3]==4:
        print('"0011001"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --4')
    elif lista_digitos[w+3]==5:
        print('"0010010"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --5')
    elif lista_digitos[w+3]==6:
        print('"0000010"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --6')
    elif lista_digitos[w+3]==7:
        print('"1111000"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --7')
    elif lista_digitos[w+3]==8:
        print('"0000000"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --8')
    elif lista_digitos[w+3]==9:
        print('"0011000"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --9')
    elif lista_digitos[w+3]=='P':
        print('"1111111"	when    '+Entradas+'="'+ binarios_lista[w+3] +'" else --_')
    else: 
        "0000000"
print('"1111111";')         

print("end Behavioral;")