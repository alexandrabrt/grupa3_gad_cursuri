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

my_var = input("Numar intreg: ")
# my_int = None
try:
    my_int = int(my_var)
    # print(variabila)
except ValueError:
    print('eroare de valoare')
except NameError:
    print('eroare de denumire variabila')
except Exception as e:
    # my_int = 'test'
    print("Exceptie generica", e)
else:
    print("Daca nu apare exceptie", my_int)
finally:
    print("Afiseaza in orice caz")
# print(my_int)

