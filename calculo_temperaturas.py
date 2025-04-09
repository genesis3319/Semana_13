def calcular_temperatura_promedio(temperaturas):
    """
    Calculamos la temperatura promedio de varias ciudades.

    Parámetros:
    temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades
                         y los valores son listas de temperaturas (en grados Celsius)
                         para cada semana.

    Retorna:
    dict: Un diccionario con las ciudades y sus respectivas temperaturas promedio.
    """
    promedios = {}

    for ciudad, temps in temperaturas.items():
        if temps:  # Verifica que la lista de temperaturas no esté vacía
            promedio = sum(temps) / len(temps)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None  # Si no hay datos, asigna None

    return promedios


# Ejemplo de uso
if __name__ == "__main__":
    temperaturas_ciudades = {
        "Ciudad Arajuno": [20, 22, 21, 19],
        "Ciudad Puyo": [25, 27, 26, 24],
        "Ciudad Macas": [15, 16, 14, 15]
    }

    promedios = calcular_temperatura_promedio(temperaturas_ciudades)
    print(promedios)  # Salida esperada: {'Ciudad Arajuno': 20.5, 'Ciudad Puyo': 25.5, 'Ciudad Macas': 15.0}