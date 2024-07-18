def calcular_area_circulo(radio):
    area = 'math'.pi * radio ** 2
    return area


def main():
    # Pedir al usuario que ingrese el radio del círculo
    try:
        radio = float(input("Ingresa el radio del círculo: "))

        # Calcular el área del círculo
        area = calcular_area_circulo(radio)

        # Mostrar el resultado
        print(f"El área del círculo con radio {radio} es: {area:.2f}")

    except ValueError:
        print("Error: Debes ingresar un número válido para el radio.")


if __name__ == "__main__":
    main()


    # Programa para calcular el salario semanal de un empleado
    # utilizando su salario por hora y las horas trabajadas.

    def calcular_salario_semanal(salario_por_hora, horas_trabajadas):
        """
        Calcula el salario semanal multiplicando el salario por hora
        por las horas trabajadas.

        Args:
        - salario_por_hora (float): Salario que se paga por cada hora trabajada.
        - horas_trabajadas (float): Número de horas trabajadas en una semana.

        Returns:
        - float: Salario semanal calculado.
        """
        salario_semanal = salario_por_hora * horas_trabajadas
        return salario_semanal


    def main():
        # Solicitar al usuario que ingrese el salario por hora y las horas trabajadas
        try:
            salario_por_hora = float(input("Ingresa el salario por hora: "))
            horas_trabajadas = float(input("Ingresa las horas trabajadas en la semana: "))

            # Calcular el salario semanal utilizando la función definida
            salario_semanal = calcular_salario_semanal(salario_por_hora, horas_trabajadas)

            # Mostrar el resultado al usuario
            print(f"El salario semanal es: ${salario_semanal:.2f}")

        except ValueError:
            print("Error: Debes ingresar valores numéricos para el salario por hora y las horas trabajadas.")


    if __name__ == "__main__":
        main()