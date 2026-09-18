# Tu carpeta de trabajo — TP02

Todo lo que programes va **acá adentro**.

| Archivo | Para qué |
|---|---|
| `mi_tp02.py` | Acá escribís tu controlador. Es lo que entregás. |
| `misiones.py` | Te lo damos hecho: las misiones de prueba. |
| `robot.py` | No lo toques. Conecta tu programa con el simulador. |

## Cómo lo ejecutás

1. Abrí `INICIAR_SIMULADOR` (carpeta de arriba) y elegí el robot.
2. Esperá la ventana.
3. Doble clic en `EJECUTAR_MI_CODIGO`, o `python3 mi_desarrollo/mi_tp02.py`.

## Podés crear más archivos

Si querés partir tu programa, creá archivos acá adentro e importalos:

```python
from mis_validaciones import es_numero
```

## Métodos del robot

La clase que importás con `from robot import Robot` está definida en
[`entorno/sim/robot.py`](../entorno/sim/robot.py). Para crear el robot, usá
`robot = Robot()` y luego llamá a `robot.conectar()`.

| Método | Qué hace |
|---|---|
| `conectar()` | Conecta con el simulador o robot. |
| `desconectar()` | Detiene el robot y cierra la conexión. |
| `verificar_estado()` | Consulta posición, orientación, acción y batería. |
| `avanzar(velocidad=0.2, tiempo=1.0)` | Avanza a la velocidad indicada en m/s durante el tiempo en segundos. |
| `girar(velocidad=0.5, tiempo=1.0)` | Gira en rad/s: positivo hacia la izquierda, negativo hacia la derecha. |
| `mover(vx=0.0, vy=0.0, vyaw=0.0, tiempo=1.0)` | Combina avance, desplazamiento lateral y giro durante el tiempo en segundos. `vx` y `vy` se expresan en m/s; `vyaw`, en rad/s. |
| `detenerse()` | Pone la velocidad en cero. |
| `saludar()` | Ejecuta el gesto de saludo. |
| `dar_la_mano()` | Extiende la mano; pensado para el G1. |
| `movmineto(*a, **k)` | Alias de `avanzar()`; está escrito así en el código. |
| `detener()` | Alias de `detenerse()`. |
| `parar()` | Alias de `detenerse()`. |

Todos estos métodos devuelven un `EstadoRobot`, excepto `desconectar()`, que
devuelve `None`. El estado contiene `x`, `y`, `z`, `yaw`, `accion` y `bateria`.

También tiene los métodos internos `_conectar_local`, `_conectar_sdk`,
`_anunciar`, `_verificar_servicio`, `_sostener` y `_exigir_conexion`, además del
constructor `__init__`.
