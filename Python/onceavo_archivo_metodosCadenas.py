""" upper() -------> Pasa un string a mayusculas
    lower() ------> Pasa un strig a minusculas
    capitalize() -> Pone la primera letra en mayusculas
    count() ------> Cuenta cuantas veces esta un caracter o un grupo de letras en un String
    find() -------> Devuelve en que posicion se encuentra un caracter o un grupo de caracteres obviamente en un string
    isdigit() ----> Devuelve True o False si el valor ingresado es un digito o no
    isalum() -----> Si son alfa numericos
    isalpha ------> Si hay solo letras
    split() ------> Separa por palabras utilizando espacios
    strip() ------> elimina los espacios al principio y al final
    replace()-----> Cambia una palabra por otra dentro de un string
    rfind() ------> Hace lo mismo que find pero de atras para adelante

    http://pyspanishdoc.sourceforge.net/lib/string-methods.html
"""

print(" ----------------------- Verificacion sencilla de email ----------------------- ")
email = input("\nIngrese su correo electronico: ")
email = email.strip()

while(email.count("@") !=1 or email.endswith("@") or email.endswith("@",0,1)):
    print("\nEl correo electronico es erroneo...")
    email = input("\nIngrese su correo electronico: ")
    email = email.strip()

print("\nEl correo a sido registrado exitosamente...")
