import speedtest
import csv
import time

# Función para realizar la prueba de velocidad
def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000
    ping_speed = st.results.ping

    return [time.time(), download_speed, upload_speed, ping_speed]

# Ciclo infinito para realizar la prueba cada 5 minutos
with open('speedtest_results.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'download_speed', 'upload_speed', 'ping_speed'])
    while True:
        results = test_speed()
        writer.writerow(results)
        file.flush() # Forzar la escritura de datos en el archivo
        time.sleep(300) # Esperar 5 minutos antes de volver a ejecutar el programa
