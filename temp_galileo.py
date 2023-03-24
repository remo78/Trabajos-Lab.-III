import urllib.request
import datetime 
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


lista_fecha_hora_temp_web=[]
for word_ll in words_ll[0:3]:
    lista_fecha_hora_temp_web.append(word_ll)
print("Fecha: ",lista_fecha_hora_temp_web[0],"\nHora: ",lista_fecha_hora_temp_web[1],"\nTemperatura: ",lista_fecha_hora_temp_web[2],"\n")


lista_fecha_hora_web=[]
for word_ll in words_ll[0:2]:
    lista_fecha_hora_web.append(word_ll)


# Obtener la fecha y hora actual del sistema
fecha_hora_actual = datetime.datetime.now()

# Formatear la fecha y hora en el formato deseado
fecha_actual = fecha_hora_actual.strftime('%d/%m/%y')
hora_actual = fecha_hora_actual.strftime('%H:%M')

# Crear una lista con la información de la fecha y hora actual
lista_fecha_hora_act = [fecha_actual, hora_actual]

# Imprimir la lista
print("La hora actual del sistema es: ",lista_fecha_hora_act[1],"\n")

# Convertir los elementos de lista_fecha_hora_temp_web y lista_fecha_hora_act en datetime
fecha_hora_web = datetime.datetime.strptime(' '.join(lista_fecha_hora_web), '%d/%m/%y %H:%M')
fecha_hora_act = datetime.datetime.strptime(' '.join(lista_fecha_hora_act), '%d/%m/%y %H:%M')

# Calcular la diferencia entre las fechas y horas
diferencia = fecha_hora_web - fecha_hora_act

# Convertir la diferencia a formato horario deseado
segundos = abs(diferencia.total_seconds())
horas = int(segundos // 3600)
minutos = int((segundos % 3600) // 60)
segundos_restantes = int(segundos % 60)

# Crear una lista con la diferencia en formato horario
diferencia_horario = [str(horas).zfill(2) + ':' + str(minutos).zfill(2) + ':' + str(segundos_restantes).zfill(2)]

# Imprimir la lista de diferencia horaria
print("La última medición fue tomada hace:",horas,"hs,",minutos,"minutos.")







