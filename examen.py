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


    
    
