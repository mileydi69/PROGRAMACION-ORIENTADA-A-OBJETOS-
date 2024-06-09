def novelas(personaje_1_,personaje_2_):
    actor = 0
    while personaje_1_() and personaje_2_():
        print("\nactor",actor)
        print(">>> Acción de ", actuar, ":", sep="")
        personaje_1.protagonista(actor_2)
        print(">>> Acción de ", antagonista_2.nombre, ":", sep="")
        actor_2.actuar(actor_1)
        actor = actor + 1
    if personaje_1.esta_vivo():
        print("\nha actuado", personaje_1.nombre)
    elif personaje_2.esta_vivo():
        print("\nha actuado", personaje_2.nombre)
    else:
        print("\nexcelente")


personaje_1 = protagonista("excelente", 10,4,8,11)
personaje_2 = antagonista("excelente", 12,5,6,8,)

personaje_1.atributos()
personaje_2.atributos()

actuan(personaje_1, personaje_2)