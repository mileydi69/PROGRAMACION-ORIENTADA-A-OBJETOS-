import threading

# Creamos una variable global
contador_global = 0

# Creamos un objeto Lock (Mutex)
mutex = threading.Lock()

# Definimos una función que será ejecutada por varios hilos
def incrementar_contador():
    global contador_global

    for _ in range(100000):
# Bloqueamos el acceso al recurso compartido
        mutex.acquire()
        contador_global += 1
# Liberamos el mutex después de actualizar el contador
        mutex.release()

# Creamos una lista de hilos
hilos = []

# Creamos y lanzamos 10 hilos
for i in range(10):
    hilo = threading.Thread(target=incrementar_contador)
    hilos.append(hilo)
    hilo.start()

# Esperamos a que todos los hilos terminen su ejecución
for hilo in hilos:
    hilo.join()

# Imprimimos el valor final del contador
print(f"Valor final del contador global: {contador_global}")

def incrementar_contador_sin_mutex():
    global contador_global

    for _ in range(100000):
        contador_global += 1  # Sin bloqueo de mutex

# El resto del código sigue igual, pero llamamos a incrementar_contador_sin_mutex() en lugar de incrementar_contador()
import threading
import time
import random

# Definimos una barrera para 3 hilos
barrera = threading.Barrier(3)


# Definimos una función que simula trabajo de hilos antes y después de la barrera
def tarea_hilo(id_hilo):
    print(f"Hilo {id_hilo} está trabajando antes de la barrera...")

# Simulamos que el hilo realiza alguna tarea antes de alcanzar la barrera
    time.sleep(random.randint(1, 3))

    print(f"Hilo {id_hilo} ha llegado a la barrera.")

# Los hilos esperan en la barrera
    barrera.wait()

# Simulamos trabajo después de que todos los hilos hayan llegado a la barrera
    print(f"Hilo {id_hilo} continúa trabajando después de la barrera...")

# Creamos y lanzamos 3 hilos
hilos = []
for i in range(3):
    hilo = threading.Thread(target=tarea_hilo, args=(i,))
    hilos.append(hilo)
    hilo.start()

# Esperamos a que todos los hilos terminen su ejecución
for hilo in hilos:
    hilo.join()

    print("Todos los hilos han terminado.")
    print('Hilo 0 está trabajando antes de la barrera')
    print('Hilo 1 está trabajando antes de la barrera')
    print('Hilo 2 está trabajando antes de la barrera')
    print('Hilo 1 ha llegado a la barrera')
    print('Hilo 2 ha llegado a la barrera')
    print('Hilo 0 ha llegado a la barrera')
    print('Hilo 1 continúa trabajando después de la barrera')
    print('Hilo 2 continúa trabajando después de la barrera')
    print('Hilo 0 continúa trabajando después de la barrera')
    print('Todos los hilos han terminado')
    import threading
    import time

# Creamos un objeto Event
    evento = threading.Event()

# Función que simula una tarea que depende de un evento
    def tarea_que_espera_evento():
        print("Hilo está esperando el evento...")
        evento.wait()  # El hilo se bloquea aquí esperando el evento
        print("El evento fue activado, el hilo continúa trabajando.")

# Función que activa el evento después de unos segundos
    def activar_evento():
        print("Hilo activador: Realizando una tarea previa antes de activar el evento...")
        time.sleep(5)
        print("Hilo activador: Activando el evento.")
        evento.set()  # Activamos el evento, permitiendo que los hilos continúen

 # Creamos un hilo que espera el evento
    hilo_espera = threading.Thread(target=tarea_que_espera_evento)
    hilo_espera.start()

# Creamos un hilo que activará el evento
    hilo_activador = threading.Thread(target=activar_evento)
    hilo_activador.start()

# Esperamos que ambos hilos terminen
    hilo_espera.join()
    hilo_activador.join()

    print("Todos los hilos han terminado.")

    print('Hilo está esperando el evento')
    print('Hilo activador: Realizando una tarea previa antes de activar el evento')
    print('Hilo activador: Activando el evento')
    print('El evento fue activado, el hilo continúa trabajando')

    print('Todos los hilos han terminado')
