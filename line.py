def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print(f"\nPara la siguiente ecuación:")
    ecuacion = f"Y = {A}X + {B}"
    print(f"\t{ecuacion}")

    print(f"\nDados los siguientes puntos:")
    y1 = A*X1 + B
    y2 = A*X2 + B
    print(f"\tP1 ({X1}, {y1})")
    print(f"\tP2 ({X2}, {y2})")

    Distancia = (((X2-X1)**2 + (y2-y1)**2)**0.5)
    print(f"\nLa distancia entre ellos es: {Distancia}")    
    
    
