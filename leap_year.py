def leap_year():
    año = int(input("ingrese un año: "))
    if año%4 == 0 and año%400 == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
       

