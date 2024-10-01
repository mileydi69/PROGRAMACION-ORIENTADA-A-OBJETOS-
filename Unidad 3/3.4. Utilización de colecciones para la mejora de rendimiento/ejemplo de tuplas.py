class Dispositivo:
    def __init__(self, nombre, direccion_ip):
        self.nombre = nombre
        # La dirección IP es una tupla de 4 números (IPx8)
        self.direccion_ip = direccion_ip

    def __str__(self):
        ip_str = ".".join(map(str, self.direccion_ip))  # Convertir la tupla a string para mostrar
        return f"{self.nombre} - IP: {ip_str}"

# Ejemplo de uso
router = Dispositivo("Router Principal", (204, 500, 6, 8))
print(router)

# Intento de modificar la dirección IP directamente resultará en un error
# router.direccion_ip[0] = 10  # Esto causaría un TypeError