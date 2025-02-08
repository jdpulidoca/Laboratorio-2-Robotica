from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # funciones matemáticas
import math
import numpy as np


# conexión con RoboDK
RDK = Robolink()

# elegir un robot
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# cargar frame (ya existente)
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# asignar frame al robot
robot.setPoseFrame(frame)
# seleccionar herramienta activa
robot.setPoseTool(robot.PoseTool())

# ajustes de velocidad
robot.setSpeed(100)   # mm/s
robot.setRounding(5)  # blending

# parámetros de la figura (curva cardioide)
num_points = 720       # número de puntos
A = 120                # escala
z_surface = 0          # z = 0 en el plano del frame
z_safe = -50           # altura segura


# punto de inicio de la figura en coordenadas polares
r_0 = A*(1 - math.cos(0)*sin(0))

# punto de inicio de la figura en coordenadas cartesianas
x_0 = r_0*math.cos(0)
y_0 = r_0*math.sin(0)

# instrucción para mover el robot al punto de inicio de la figura
robot.MoveJ(transl(x_0, y_0, z_surface + z_safe))

# bajar a la superficie de trabajo (z = 0)
robot.MoveL(transl(x_0, y_0, z_surface))

# dibujar la curva polar

# la curva irá de 0 a 2pi
full_turn = 2*math.pi

for i in range(num_points+1):
    # fracción entre 0 y 1
    t = i / num_points
    # ángulo actual
    theta = full_turn * t

    # calcular r
    r = A*(1 - math.cos(theta)*sin(3*theta))

    # conversión de coordenadas polares a cartesianas
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # mover linealmente (MoveL) en el plano del frame
    robot.MoveL(transl(x, y, z_surface))

# al terminar, subir de nuevo a la zona segura
robot.MoveL(transl(x_0, y_0, z_surface + z_safe))

print(f"Figura completada.")
