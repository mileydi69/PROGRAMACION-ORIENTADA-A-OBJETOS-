import threading
import time

evento = threading.Event()


def esperar_evento():
 print("Esperando al evento...")
 # Esperamos a que el evento se active
 evento.wait()
 print("El evento ha sido activado!")

def activar_evento():
  print("Esperando 5 segundos antes de activar el evento...")
  time.sleep(5)
  # Activamos el evento
  evento.set()
  print("El evento ha sido activado después de 5 segundos")
hilo1 = threading.Thread(target=esperar_evento)
hilo2 = threading.Thread(target=activar_evento)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("Programa terminado")
print("Esperando al evento...")
print("Esperando 5 segundos antes de activar el evento...")
print("El evento ha sido activado después de 5 segundos")
print("El evento ha sido activado!")
print("Programa terminado")
































