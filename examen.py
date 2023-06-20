import csv

#Ej 1
def mediana(diccionario):
    valores = list(diccionario.values())
    ordenados = sorted(valores)
    num_vals = len(valores)

    if num_vals % 2 == 0:
        val1 = int(num_vals / 2)
        val2 = int(num_vals / 2) - 1

        nval1 = ordenados[val1]
        nval2 = ordenados[val2]
        mediana = (nval1 + nval2) / 2
        return mediana
    else:
        mediana = ordenados[num_vals // 2]
        return mediana

diccionario = {'valor0': 5, 'valor1': 3, 'valor2': 8, 'valor3': 1, 'valor4': 6}
res = mediana(diccionario)

if res is not None:
    print("La mediana es:", res)
else:
    print("No se puede calcular la mediana.")

#Ej 3
def combinar(diccionario_nombres_edades, diccionario_nombres_profesiones, diccionario_nombres_sueldos):
    diccionario_final = {}

    nombres = set(diccionario_nombres_edades.keys()) | set(diccionario_nombres_profesiones.keys()) | set(diccionario_nombres_sueldos.keys())

    for nombre in nombres:
        edad = diccionario_nombres_edades.get(nombre)
        profesion = diccionario_nombres_profesiones.get(nombre)
        sueldo = diccionario_nombres_sueldos.get(nombre)
        diccionario_final[nombre] = {'edad': edad, 'profesión': profesion, 'sueldo': sueldo}

    return diccionario_final

# Llamada
diccionario_nombres_edades = {'Ana': 25, 'Juan': 30, 'María': 28}
diccionario_nombres_profesiones = {'Ana': 'Ingeniera', 'Juan': 'Doctor', 'María': 'Abogada'}
diccionario_nombres_sueldos = {'Ana': 5000, 'Juan': 7000, 'María': 6000}

diccionario_final = combinar(diccionario_nombres_edades, diccionario_nombres_profesiones, diccionario_nombres_sueldos)
print(diccionario_final)


#Ej4
def palabra_repetida(fichero):
    contador={}
    p_mas_repetida= None   
    max_repeticiones = 0
    
    with open(fichero, 'r') as archivo:
        for linea in archivo:
            palabra = linea.strip().lower()             
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
                
            if contador[palabra] > max_repeticiones:
                max_repeticiones = contador[palabra]
                p_mas_repetida = palabra
    
    return p_mas_repetida

fichero = "palabras.txt"
p_mas_repetida = palabra_repetida(fichero)
print("La palabra más repetida es:", p_mas_repetida)

#Ej2
def procesar (datos,n_curso):
 estudiantes = []

 with open(datos,'r') as archivo:
     csv_read=csv.reader(archivo)
     next(csv_read)

     for linea in csv_read:
         nombre=linea[0]
         apellido=linea[1]
         edad=linea[2]
         curso=linea[3]

         if curso == str(n_curso):
             estudiantes.append(nombre,apellido,edad,curso)

       if len(estudiantes)==0:
         raise ValueError("No hay estudiantes")
     return estudiantes
             