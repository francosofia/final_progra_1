# ===============================
# FUNCIONES INCORPORADAS PYTHON
# ===============================

# ---- Matemáticas ----
abs(-5)              # Devuelve valor absoluto
round(3.1416, 2)     # Redondea número
pow(2, 3)            # Potencia (2^3)
divmod(10, 3)        # Devuelve (cociente, resto)
sum([1,2,3])         # Suma elementos
min([1,2,3])         # Devuelve mínimo
max([1,2,3])         # Devuelve máximo

# ---- Longitud / Iterables ----
len([1,2,3])         # Cantidad de elementos
range(5)             # Secuencia 0 a 4
enumerate(["a","b"]) # Devuelve índice y valor
zip([1,2],["a","b"]) # Une listas en pares
sorted([3,1,2])      # Ordena lista
reversed([1,2,3])    # Iterador invertido
all([True, True])    # True si todos son True
any([False, True])   # True si alguno es True
iter([1,2,3])        # Devuelve iterador
next(iter([1,2,3]))  # Devuelve siguiente elemento
filter(lambda x: x>2, [1,2,3]) # Filtra elementos
map(lambda x: x*2, [1,2,3])    # Aplica función

# ---- Conversión de tipos ----
int("5")             # Convierte a entero
float("3.5")         # Convierte a flotante
str(10)              # Convierte a string
bool(1)              # Convierte a booleano
list("abc")          # Convierte a lista
tuple([1,2])         # Convierte a tupla
set([1,1,2])         # Conjunto sin repetidos
dict(a=1,b=2)        # Diccionario
complex(2,3)         # Número complejo
bytes(5)             # Bytes vacíos
bytearray(5)         # Bytearray
memoryview(bytes(5)) # Vista de memoria
frozenset([1,2])     # Conjunto inmutable

# ---- Entrada / Salida ----
print("Hola")        # Muestra por pantalla
input("Nombre: ")    # Lee entrada usuario
open("archivo.txt")  # Abre archivo

# ---- Inspección / Tipos ----
type(10)             # Devuelve tipo
isinstance(10,int)   # Verifica tipo
issubclass(bool,int) # Verifica herencia
id(10)               # Devuelve id en memoria
hash("hola")         # Devuelve hash
callable(print)      # Verifica si es función
"""
# ---- Programación orientada a objetos ----
object()             # Clase base
super()              # Accede a clase padre
property()           # Define propiedad
classmethod()        # Método de clase
staticmethod()       # Método estático
vars()               # Diccionario atributos
dir()                # Lista atributos
getattr(obj,"x")     # Obtiene atributo
setattr(obj,"x",10)  # Asigna atributo
delattr(obj,"x")     # Borra atributo
hasattr(obj,"x")     # Verifica atributo

# ---- Evaluación dinámica ----
eval("2+2")          # Evalúa expresión
exec("x=5")          # Ejecuta código
compile("2+2","","eval") # Compila código
"""
# ---- Utilidades varias ----
help(print)          # Muestra ayuda
format(3.1416,".2f") # Formatea texto
globals()            # Diccionario global
locals()             # Diccionario local
chr(65)              # Código ASCII a carácter
ord("A")             # Carácter a ASCII
bin(10)              # Binario
hex(10)              # Hexadecimal
oct(10)              # Octal
ascii("ñ")           # Representación ASCII
repr("hola")         # Representación formal
slice(0,5)           # Objeto slice
breakpoint()         # Punto de depuración