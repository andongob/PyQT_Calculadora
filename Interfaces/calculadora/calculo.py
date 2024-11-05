# Definición de funciones para operaciones matemáticas básicas
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: División por cero"  # Manejo de error para evitar división por cero
    return num1 / num2

def porcentaje(num1, num2):
    return num1 * num2 / 100

# Diccionario que mapea nombres de operaciones a funciones
operaciones = {
    "sumar": suma,
    "restar": resta,
    "dividir": divide,
    "multiplicar": multiplica,
    "porcentaje": porcentaje
}

# Función principal para realizar el cálculo
def calculo(operando1, operacion, operando2):
    # Convertir los operandos a float para asegurar operaciones decimales precisas
    num1 = float(operando1)
    num2 = float(operando2)
    
    # Verificar que la operación exista en el diccionario
    if operacion not in operaciones:
        return "Error: Operación desconocida"
    
    # Realizar la operación llamando a la función correspondiente en el diccionario
    resultado = operaciones[operacion](num1, num2)
    
    # Manejo adicional en caso de error en la operación (ej. división por cero)
    if isinstance(resultado, str):  # Esto captura mensajes de error como el de división por cero
        return resultado
    
    # Redondear el resultado a 9 decimales y convertir a int si es un entero exacto
    resultado = round(resultado, 9)
    if resultado == int(resultado):
        resultado = int(resultado)
    
    # Convertir a cadena para limitar la longitud a 9 caracteres
    return str(resultado)[:9]
