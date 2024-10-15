def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    Y1 = A * X1 + B
    Y2 = A * X2 + B
    print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}")
    print(f"\nDados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    print(f"\nLa distancia entre ellos es: {distancia}")
