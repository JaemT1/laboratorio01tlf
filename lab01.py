from matplotlib import pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn3



def unionConjuntos(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in resultado:
            resultado.append(elemento)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def unionConjuntosListaC(conjuntosLista):
    resultado = []
    for conjunto in conjuntosLista:
        for elemento in conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
    return resultado


def interseccionConjuntos(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento in conjunto2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado


def interseccionConjuntosLista(conjuntosLista):
    conjuntoIntersecion = list (conjuntosLista[0])
    resultado = []
    for u in range (len(conjuntoIntersecion)):
        elemento = conjuntoIntersecion[u]
        verdad = True
        for p in range(1, len(conjuntosLista)):
            if elemento not in conjuntosLista[p]:
                verdad = False
                break

        if verdad:
            resultado.append(elemento)
    return resultado


def diferenciaConjuntos(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

def diferenciaSimetricaConjuntos(conjuntosLista):
    # Crear un diccionario para contar las ocurrencias de cada elemento
    conteo_elementos = {}

    # Contar cuántas veces aparece cada elemento en todos los conjuntos
    for conjunto in conjuntosLista:
        for elemento in conjunto:
            if elemento in conteo_elementos:
                conteo_elementos[elemento] += 1
            else:
                conteo_elementos[elemento] = 1

    # Crear la lista de diferencia simétrica (elementos que aparecen un número impar de veces)
    diferencia_simetrica = []
    for elemento, conteo in conteo_elementos.items():
        if  conteo == 1 :
            diferencia_simetrica.append(elemento)

    return diferencia_simetrica


def pertenecerConjunto(conjunto1, conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

def serSuperConjunto(conjunto1, conjunto2):
    return pertenecerConjunto(conjunto1, conjunto2)

# Conjuntos de prueba
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 1}
conjunto_c = {5, 6, 7, 8}

conjuntosLista = [conjunto_a, conjunto_b, conjunto_c]

# Unión de tres conjuntos
union_ab = unionConjuntos(conjunto_a, conjunto_b)
union_ac = unionConjuntos(conjunto_a, conjunto_c)
union_bc = unionConjuntos(conjunto_b, conjunto_c)
union_abc = unionConjuntos(union_ab, conjunto_c)

print("La unión de A y B es: ", union_ab)
print("La unión de A y C es: ", union_ac)
print("La unión de B y C es: ", union_bc)
print("La unión de A, B y C es: ", union_abc)
print("----------------------------------------------")

# Intersección de tres conjuntos
interseccion_ab = interseccionConjuntos(conjunto_a, conjunto_b)
interseccion_ac = interseccionConjuntos(conjunto_a, conjunto_c)
interseccion_bc = interseccionConjuntos(conjunto_b, conjunto_c)
interseccion_abc = interseccionConjuntos(interseccion_ab, conjunto_c)
print("La inteseccion de A y B es: ", interseccion_ab)
print("La inteseccion de A y C es: ", interseccion_ac)
print("La inteseccion de B, C es: ", interseccion_bc)
print("La intersección de A, B y C es: ", interseccion_abc)
print("----------------------------------------------")

# Diferencia entre tres conjuntos
diferencia_ab = diferenciaConjuntos(conjunto_a, conjunto_b)
diferencia_ac = diferenciaConjuntos(conjunto_a, conjunto_c)
diferencia_bc = diferenciaConjuntos(conjunto_b, conjunto_c)
diferencia_abc = diferenciaConjuntos(diferencia_ab, conjunto_c)
print("La diferencia de A, B es: ", diferencia_ab)
print("La diferencia de A, C es: ", diferencia_ac)
print("La diferencia de B, C es: ", diferencia_bc)
print("La diferencia de A - B - C es:", diferencia_abc)
print("----------------------------------------------")

# Diferencia simétrica entre tres conjuntos
#diferencia_sim_ab = diferenciaSimetricaConjuntos(conjunto_a, conjunto_b)
#diferencia_sim_ac = diferenciaSimetricaConjuntos(conjunto_a, conjunto_c)
#diferencia_sim_bc = diferenciaSimetricaConjuntos(conjunto_b, conjunto_c)
diferencia_sim_abc = diferenciaSimetricaConjuntos(conjuntosLista)
#print("La diferencia de A, B es: ", diferencia_ab)
#print("La diferencia de A, C es: ", diferencia_ac)
#print("La diferencia de B, C es: ", diferencia_bc)
print("La diferencia simétrica de A, B y C es:", diferencia_sim_abc)
print("----------------------------------------------")

# Subconjunto y Superconjunto
print("¿A es subconjunto de B?", pertenecerConjunto(conjunto_a, conjunto_b))
print("¿B es superconjunto de A?", serSuperConjunto(conjunto_a, conjunto_b))
print("----------------------------------------------")



diagram = venn3( subsets = (len(conjunto_a), len(conjunto_b), len(conjunto_c), len(interseccion_ab), len(interseccion_ac), len(interseccion_bc), len(interseccion_abc)), set_labels = ('A', 'B', 'C'))
plt.title("Diagrama de Venn")
plt.show()
