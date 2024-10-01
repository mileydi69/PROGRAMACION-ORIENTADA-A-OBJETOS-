import threading

# Variable compartida entre hilos
contador_global = 0

# Crear un mutex (bloqueo) para proteger el acceso a la variable compartida
mutex = threading.Lock()

# Función para incrementar el contador global
def incrementar_contador():
    global contador_global
    for _ in range(100000):
        # Sección crítica protegida por el mutex
        mutex.acquire()  # Adquirir el mutex para acceder a la sección crítica
        contador_global += 1  # Modificación del recurso compartido
        mutex.release()  # Liberar el mutex para que otros hilos puedan acceder

# Crear dos hilos que ejecutarán la función de incremento
hilo1 = threading.Thread(target=incrementar_contador)
hilo2 = threading.Thread(target=incrementar_contador)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen su ejecución
hilo1.join()
hilo2.join()

# Imprimir el valor final del contador global
print(f"Valor final del contador global: {contador_global}")
import threading

# Crear una barrera para sincronizar 3 hilos
barrera = threading.Barrier(3)

def tarea_barrera():
    print(f"Hilo {threading.current_thread().name} está esperando en la barrera")
    barrera.wait()  # Esperar a que los otros hilos lleguen a este punto
    print(f"Hilo {threading.current_thread().name} cruzó la barrera")

# Crear e iniciar 3 hilos
hilos = [threading.Thread(target=tarea_barrera) for _ in range(3)]
for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

import threading
import time

# Crear un evento
evento = threading.Event()

def tarea_evento():
    print(f"Hilo {threading.current_thread().name} está esperando el evento")
    evento.wait()  # Esperar a que se establezca el evento
    print(f"Hilo {threading.current_thread().name} ha detectado el evento y continúa")

# Crear e iniciar 3 hilos
hilos = [threading.Thread(target=tarea_evento) for _ in range(3)]
for hilo in hilos:
    hilo.start()

time.sleep(2)  # Simular un retraso antes de establecer el evento
print("Estableciendo el evento")
evento.set()  # Establecer el evento para liberar a los hilos

for hilo in hilos:
    hilo.join()
