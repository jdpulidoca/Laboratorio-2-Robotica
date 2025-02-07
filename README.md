# Laboratorio 2: Análisis y operación del manipulador Motoman MH6: Comparativa y aplicaciones prácticas.

A continuación, se presenta el trabajo realizado para el laboratorio número 2 de la materia Robótica de la Univeridad Nacional de Colombia para el periodo 2024-II.

### Motoman MH6 VS IRB 140
  
|	Característica	|	Motoman MH6	|	IRB 140	|
|	 ---	|	 ---	|	 ---	|
|	Fabricante	|	Yaskawa	|	ABB	|
|	Carga útil máxima	|	6 kg	|	6 kg	|
|	Alcance máximo	|	1,422 mm	|	810 mm	|
|	Repetibilidad	|	±0.08 mm	|	±0.01 mm	|
|	Peso del robot	|	130 kg	|	98 kg	|
|	Número de ejes (Grados de libertad)	|	6	|	6	|
|	Rango de movimiento	|	---	| ---	|
|	Eje 1 (Base)	|	±170°	|	±165°	|
|	Eje 2 (Brazo inferior)	|	+155°/-90°	|	+110°/-110°	|
|	Eje 3 (Brazo superior)	|	+250° /-175°	|	+70° /-160°	|
|	Eje 4 (Muñeca rotación)	|	±190°	|	±200°	|
|	Eje 5 (Muñeca flexión)	|	±135°	|	±115°	|
|	Eje 6 (Muñeca giro)	|	±360°	|	±400°	|
|	Velocidad máxima por eje	| ---	|	---	|
|	Eje 1	|	180°/s	|	150°/s	|
|	Eje 2	|	180°/s	|	120°/s	|
|	Eje 3	|	180°/s	|	140°/s	|
|	Eje 4	|	400°/s	|	280°/s	|
|	Eje 5	|	400°/s	|	280°/s	|
|	Eje 6	|	600°/s	|	280°/s	|
|	Controlador	|	DX100, DX200	|	IRC5 Compact	|
|	Tipo de montaje	|	Piso, pared, techo, invertido	|	Piso, pared, invertido	|
|	Estructura mecánica	|	Brazo articulado	|	Brazo articulado	|
|	Protección ambiental	|	IP54 (cuerpo), IP67 (muñeca)	|	IP67 (cuerpo y muñeca)	|
|	Temperatura de operación	|	0°C - 45°C	|	0°C - 45°C	|
|	Fuente de alimentación	|	200-230V, trifásico	|	200-600V, trifásico	|
|	Consumo de energía	|	Aproximadamente 1.5 kVA	|	Aproximadamente 1.2 kVA	|
|	Compatibilidad con sensores	|	Sí (visión artificial, encoders adicionales)	|	Sí (visión, force control)	|
|	Software de programación	|	MotoSim, RoboDK, INFORM Language	|	RobotStudio, RAPID Language	|
|	Aplicaciones principales	|	Soldadura, manipulación, ensamblaje	|	Ensamblaje, manipulación, soldadura, pick & place	|

<ul>  
<li> Descripcion de las configuraciones home1 y home2 del Motoman MH6, indicando la posicion de cada articulacion, ¿Cual posicion es mejor?, justifique su respuesta
<li> Procedimiento detallado para realizar movimientos manuales, especificando como cambiar entre modos de operacion (articulaciones, cartesiano) y realizar traslaciones y rotaciones en los ejes X, Y, Z.
<li> Explicacion completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre niveles y como identificar el nivel establecido en la interfaz del robot.
<li> Descripcion de las principales funcionalidades de RoboDK, explicando como se comunica con el manipulador Motoman y que procesos realiza para ejecutar movimientos.
<li> Analisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta.
<li> Codigo desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
<li> Video de simulacion en RoboDK mostrando la trayectoria polar y evidencia de su implementaci´on en el manipulador Motoman de forma fısica, controlado desde el PC.
</ul>

# Comparación entre RoboDK y RobotStudio
RoboDK y RobotStudio son dos herramientas potentes de programación fuera de linea y simulación de robots, sin embarbo, cada una responde a necesidades diferentes. RobotStudio está diseñado específicamente para robots ABB, mientras que RoboDK es compatible con múltiples marcas de robots.

| Característica         | RoboDK                          | RobotStudio          |
|------------------------|--------------------------------|----------------------|
| **Fabricante**        | RoboDK (Independiente)         | ABB                  |
| **Compatible con múltiples marcas** | Sí, es compatile con robots ABB, KUKA, FANUC, Yaskawa, UR, entre otros. | No, solo robots ABB  |
| **Facilidad de uso**  | Interfaz intuitiva y fácil de aprender | Más complejo, con herramientas avanzadas |
| **Programación offline** | Sí, para múltiples marcas | Sí, pero solo para ABB |
| **Lenguajes de programación** | Python, G-code, y otros | RAPID (propietario de ABB) |
| **Integración CAD/CAM** | Compatible con SolidWorks, Fusion 360, Mastercam, etc. | Integración limitada con CAD |
| **Precisión de simulación** | Alta precisión para múltiples marcas | Más precisa para robots ABB |
| **Post-Procesadores** | Requiere configuración para cada marca | Preconfigurado para ABB |
| **Precio**           | Pago con prueba gratuita      | Gratuito básico, pago para características avanzadas |
