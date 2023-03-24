import urllib.request
import os
os.system("cls")

url = "https://www.frcon.utn.edu.ar/galileo/downld02.txt"

# Abre la URL y lee el contenido como una cadena de texto
with urllib.request.urlopen(url) as response:
    content = response.read().decode("utf-8")

# Divide la cadena de texto en líneas y encuentra la última línea
lines = content.splitlines()
last_line = lines[-1]
first_line = lines[0]
second_line = lines[1]

words_fl = first_line.split()
words_sl = second_line.split()
words_ll = last_line.split()

# for word_sl in words_sl:
#     print(word_sl)
# for word_fl in words_fl:
#     print(word_fl)
for word_ll in words_ll[0:3]:
    print(word_ll)


# print(first_line)
# print(second_line)
# print(last_line)




