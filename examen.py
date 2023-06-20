#Ej 1

def medina(diccionario):
    valores=list(diccionario.values())
    num_vals = len(valores)


    if num_vals%2 == 0:
        val1 = num_vals/2
        val2 = (num_vals/2)-1

        nval1=ordenado[val1]
        nval2=ordenado[val2]
        return (val1+val2)/2
    
    
