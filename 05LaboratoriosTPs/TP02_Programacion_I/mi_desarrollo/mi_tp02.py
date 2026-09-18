# =====================================================================
#  TP02 - Programación I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBÍS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abrí INICIAR_SIMULADOR (elegí G1 o Go2)
#    2. Esperá a que aparezca la ventana con el robot
#    3. Recién ahí ejecutá este archivo
#
#  Nombre y apellido:  .....................................
#  Comisión:           .....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando: object) -> bool:
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice qué hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no esté vacía
      - que el nombre del comando sea uno de los cuatro válidos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean números de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CÓDIGO ACÁ
    pass


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot: Robot, comando: tuple[object, ...]) -> str:
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que pasó.

    Órdenes que podés usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca válido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el límite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CÓDIGO ACÁ
    pass


# =====================================================================
#  PARTE 3 - Recorrer la misión entera
# =====================================================================
def ejecutar_mision(
    robot: Robot, mision: list[tuple[object, ...]], historial: list[str]
) -> None:
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es válido, lo rechaza y sigue con el siguiente
      - si es válido, lo ejecutá
      - en los dos casos, guarda en 'historial' qué fue lo que pasó

    Un comando inválido NO tiene que cortar la misión.
    """
    # Prueba simple de movimiento. Por ahora no recorremos la lista misión.
    print("El perro avanza 40 centímetros...")
    robot.avanzar(velocidad=0.2, tiempo=2.0)

    print("Gira 90 grados a la derecha...")
    robot.girar(velocidad=-0.5, tiempo=3.14)

    print("Avanza otros 40 centímetros...")
    robot.avanzar(velocidad=0.2, tiempo=2.0)

    print("Saludando")
    robot.saludar()
    print("Recorrido terminado.")

    for accion in mision:
        metodo = getattr(robot, accion[0])
        metodo(*accion[1:])


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial: list[str]) -> None:
    """Muestra por pantalla un resumen de la misión.

    Tiene que decir, como mínimo:
      - cuántos comandos se ejecutaron bien
      - cuántos se rechazaron
      - cuál fue el motivo de cada rechazo
    """
    # TU CÓDIGO ACÁ
    pass


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main() -> None:
    robot = Robot()
    robot.conectar()

    historial: list[str] = []

    try:
        # Empezá probando con MISION_BASICA.
        # Cuando funcione, probá con MISION_CON_ERRORES: esa tiene
        # comandos inválidos a propósito.
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
