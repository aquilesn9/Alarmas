import time

# Establecer la hora actual en el reloj
hora_actual = time.strftime('%H:%M:%S')

# Establecer la hora de la alarma
hora_alarma = input("Ingrese la hora de la alarma (formato HH:MM:SS): ")

# Ejecutar el reloj y verificar la hora de la alarma
while hora_actual != hora_alarma:
    print("La hora actual es " + hora_actual)
    hora_actual = time.strftime('%H:%M:%S')
    time.sleep(1)
print("¡Despierta! Es hora de levantarse.")