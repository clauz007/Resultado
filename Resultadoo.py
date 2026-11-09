import math
import random

def pedir_numero(mensaje, entero=False):
    """Pide un número positivo al usuario y realiza su entrada"""
    while True:
        try:
            valor = int(input(mensaje)) if entero else float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor que 0")
                continue
            return valor
        except ValueError:
            print("Intente de nuevo")

def en_elipse(x, y, a, b):
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1

def en_hiperbola(x, y, c, d):
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1

def main():
    print("---Montecarlo: Elipse e Hipérbola")
    a = pedir_numero("Ingrese a (elipse): ")
    b = pedir_numero("Ingrese b (elipse): ")
    c = pedir_numero("Ingrese c (hipérbola): ")
    d = pedir_numero("Ingrese d (hipérbola): ")
    n = pedir_numero("Cantidad de puntos aleatorios: ", entero=True)

    dentro_elipse = 0
    dentro_interseccion = 0

    for _ in range(n):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        if en_elipse(x, y, a, b):
            dentro_elipse += 1
            if en_hiperbola(x, y, c, d):
                dentro_interseccion += 1

    area_elipse = math.pi * a * b

    if dentro_elipse > 0:
        area_interseccion = (dentro_interseccion / dentro_elipse) * area_elipse
    else:
        area_interseccion = 0.0

    print("\n=== RESULTADOS ===")
    print(f"Puntos generados totales: {n}")
    print(f"Puntos que cayeron dentro de la elipse: {dentro_elipse}")
    print(f"Puntos que cayeron en la intersección hipérbola-elipse: {dentro_interseccion}")
    print(f"Área de la elipse (pi*a*b): {area_elipse:.4f}")
    print(f"Área aproximada de la intersección: {area_interseccion:.4f}")


if __name__ == "__main__":
    main()