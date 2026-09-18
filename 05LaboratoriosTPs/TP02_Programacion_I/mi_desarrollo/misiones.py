# =====================================================================
#  Misiones de prueba para el TP02.
#
#  ESTE ARCHIVO TE LO DAMOS HECHO. No hace falta que lo modifiques
#  (podés agregar misiones tuyas al final si querés probar cosas).
#
#  Una MISIÓN es una lista de COMANDOS.
#  Un COMANDO es una tupla, donde el primer elemento dice qué hacer:
#
#      ("avanzar", velocidad, tiempo)
#           velocidad en metros por segundo
#           tiempo    en segundos
#           distancia recorrida = velocidad x tiempo
#
#      ("girar", velocidad, tiempo)
#           velocidad en radianes por segundo
#           POSITIVA gira a la izquierda, NEGATIVA a la derecha
#           ángulo girado = velocidad x tiempo
#
#      ("detenerse",)
#      ("saludar",)
#
#  Recordatorio de radianes:
#      90 grados  = 1.5708 rad
#      180 grados = 3.1416 rad
# =====================================================================

# Una misión corta y sin problemas: sirve para arrancar.
# Avanza 0.4 m, gira 90 grados a la derecha, avanza 0.4 m.
MISION_BASICA: list[tuple[object, ...]] = [
    ("avanzar", 0.2, 2.0),      # 0.2 x 2.0 = 0.4 metros
    ("girar", -0.5, 3.14),      # -0.5 x 3.14 = -1.57 rad = 90 grados a la derecha
    ("avanzar", 0.2, 2.0),
    ("detenerse",),
]

# Un cuadrado. Si tu controlador funciona, el robot vuelve al punto de partida.
MISION_CUADRADO: list[tuple[object, ...]] = [
    ("avanzar", 0.2, 2.0),
    ("girar", -0.5, 3.14),
    ("avanzar", 0.2, 2.0),
    ("girar", -0.5, 3.14),
    ("avanzar", 0.2, 2.0),
    ("girar", -0.5, 3.14),
    ("avanzar", 0.2, 2.0),
    ("girar", -0.5, 3.14),
    ("detenerse",),
]

# OJO: esta misión tiene comandos INVÁLIDOS a propósito.
# Tu controlador tiene que detectarlos, NO ejecutarlos, y seguir con el resto.
# Al final, el reporte tiene que decir cuántos se ejecutaron y cuántos no.
MISION_CON_ERRORES: list[tuple[object, ...]] = [
    ("avanzar", 0.2, 2.0),          # bien
    ("girar", -0.5, 3.14),          # bien
    ("avanzar", 0.9, 2.0),          # MAL: 0.9 m/s supera la velocidad permitida
    ("avanzar", 0.2, 50.0),         # MAL: 50 segundos supera el tiempo permitido
    ("girar", 3.0, 2.0),            # MAL: 3.0 rad/s supera el giro permitido
    ("volar", 0.2, 1.0),            # MAL: ese comando no existe
    ("avanzar", "rápido", 2.0),     # MAL: la velocidad tiene que ser un número
    ("avanzar", 0.2),               # MAL: le falta el tiempo
    ("avanzar", 0.2, -3.0),         # MAL: el tiempo no puede ser negativo
    ("saludar",),                   # bien
    ("detenerse",),                 # bien
]

# Una misión más larga, para probar que el reporte aguanta.
MISION_LARGA: list[tuple[object, ...]] = [
    ("avanzar", 0.15, 2.0),
    ("girar", 0.5, 1.57),           # positiva: a la izquierda
    ("avanzar", 0.15, 2.0),
    ("girar", -0.5, 1.57),          # negativa: a la derecha
    ("saludar",),
    ("avanzar", 0.2, 2.0),
    ("girar", 0.5, 6.28),           # 0.5 x 6.28 = 3.14 rad = media vuelta
    ("avanzar", 0.2, 2.0),
    ("detenerse",),
]

# Todas juntas, por si querés elegir desde un menú.
MISIONES: dict[str, list[tuple[object, ...]]] = {
    "basica": MISION_BASICA,
    "cuadrado": MISION_CUADRADO,
    "errores": MISION_CON_ERRORES,
    "larga": MISION_LARGA,
}
