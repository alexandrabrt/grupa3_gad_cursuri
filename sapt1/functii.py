# def my_function(a: str, b: int, c: int = 2) -> str:
#     """
#     :param a: primul string in concatenare
#     :param b: al doilea string in concatenare
#     :param c: al treilea string in concetenare
#     :return: concateneaza
#     """
#     # blocul functiei
#     # pass
#     # return str(a) + str(b) + str(c), a - b - c
#     return str(a) + str(b) + str(c)


# variabila = my_function(1, 2)
# variabila = my_function(1, 2, c=2)
# # variabila, scadere = my_function('1', 3, 4)
# variabila = my_function('1', 3, 4)
# print(variabila)

# my_var = input("Numar intreg: ")
# # my_int = None
# try:
#     my_int = int(my_var)
#     # print(variabila)
# except ValueError:
#     print('eroare de valoare')
# except NameError:
#     print('eroare de denumire variabila')
# except Exception as e:
#     # my_int = 'test'
#     print("Exceptie generica", e)
# else:
#     print("Daca nu apare exceptie", my_int)
# finally:
#     print("Afiseaza in orice caz")
# print(my_int)


# def nume_functie(param_1, param_2, *args):
#     suma = int(param_1) + int(param_2)
#     for iter in args:
#         suma += int(iter)
#     return suma

# lista = [1, 3, 4]
# rezultat = nume_functie(1, 2, 3, 4)
# print(rezultat)
#
# def my_function(param_1, param_2, **kwargs):
#     print(kwargs)
#     suma = param_1 + param_2
#     for i in kwargs.values():
#         suma += int(i)
#     return suma
#
#
# rezultat = my_function(2, 3, b=3, a=5)
# print(rezultat)

# lista = [1, 2]

#
# def suma_functie(*args):
#     # suma = []
#     # for item in args:
#     #     suma.append(item)
#     suma = [item for item in args if item > 2]
#     return suma
#
#
# rezultat = suma_functie(1, 2, 3, 4)
# print(rezultat)
# a = 1
# b = 2
# if a < b:
#     min = a
# else:
#     min = b
#
# variabila = "a este valaorea minima" if a < b else "b este valaore minima"
# print(variabila)

lista = [x**2 for x in range(10)]
# print(lista)
# lista_duplicat = []
# for x in lista:
#     if x < 36:
#         x += 1
#     else:
#         x *= 1000
#     lista_duplicat.append(x)
#
# lista_duplicat = [x+1 if x < 35 else x * 1000 for x in lista]
#
# print(lista_duplicat)

# lista_duplicat = [y if int(y) > 2 else int(y)+1 for x in lista for y in str(x)]
# print(lista_duplicat)
# lista_x = []
# for x in lista:
#     for y in str(x):
#         if x < 5:
#             lista_x.append(int(y) - 1)

# lista_x = [int(y) - 1 for x in lista for y in str(x) if x < 5]
#
# print(lista_x)

#
# def functie_lambda(x, y):
#     return x - y


# functie_lambda = lambda x, y: x if x < y else y
# print(functie_lambda(2, 3))

jucatori = [{'nume': 'Ion', "prenume": "Vasile", "nivel": 1, "varsta": 24},
            {'nume': 'Maria', "prenume": "Gheorghe", "nivel": 3, 'varsta': 23},
            {'nume': 'Ionut', "prenume": "Vladescu", "nivel": 1, 'varsta': 22}]

# sortati = sorted(jucatori, key=lambda jucatori: jucatori['nivel'])

s = sorted(jucatori, key=lambda x: (x['nivel'], x['varsta']))
print(s)
