# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */




def is_anagrama(palabra1,palabra2):

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    arr_palabra1 = list(palabra1)
    arr_palabra2 = list(palabra2)

    arr_palabra1.sort()
    arr_palabra2.sort()

    palabra1 = "".join(arr_palabra1)
    palabra2 = "".join(arr_palabra2)

    if palabra1 == palabra2:
        return True
    else:
        return False
   


resultado = is_anagrama("Nacionalistsa","Altisonancia")

if resultado:
    print("Es anagrama")
else:
    print("No es anagrama")