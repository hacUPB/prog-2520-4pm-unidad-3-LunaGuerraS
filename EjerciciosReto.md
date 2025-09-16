## 1. Simulación de consumo de combustible:
Un avión inicia su vuelo con una cantidad determinada de combustible (en litros). El consumo de combustible por hora puede variar según la fase del vuelo (despegue, crucero, aterrizaje).
Solicita al usuario la cantidad inicial de combustible y el número total de horas de vuelo. Para cada hora, pide el consumo correspondiente y muestra cuánto combustible queda después de cada hora. Si el combustible restante es menor a un umbral de seguridad (por ejemplo, 500 litros), alerta al usuario y pregunta si desea realizar un aterrizaje de emergencia.

### Tabla de Análisis:
| Variable de entrada | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Combustible | La cantidad inicial de combustible en litros | Variable tipo int |
| Gasto | La cantidad de combustible que se consume cada hora | Variable tipo int |
| Duración | Las horas que dura el vuelo | Variable tipo int |

| Variable de salida | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Restante | La cantidad de combustible que queda en el avión durante el vuelo, en litros | Variable tipo int |
| Alerta | Mensaje de alerta si el combustible está bajo el umbral de seguridad | Variable tipo str |

| Variable de control | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| umbral_seguridad | Umbral de seguridad para el combustible restante | Variable tipo float/int |

Nota: Se uso la IA para pedirle que de redactara el enunciado en base a lo que yo le dije que queria (Un ejercicio que se pudiera hacer con bucle en python sobre ingenieria aeronautica y fuera control de combustible). Y para que me ayudara a sacar la formula para el umbral de seguridad con solo el peso total y el combustible.

### Rúbrica:
|Requisito	|Cumple (2) Cumple Parcialmente (1) No cumple (0) |	Evidencia (página/tabla/figura/sección) |
|-----------|-------------------------------------------------|-----------------------------------------|
|Contexto aeronáutico claro y relevante | 2 | - |
|Clara definición y clasificación de las variables de entrada, salida, de control e intermedias	|  2  | - |
|Clara definición de las constantes que se utilizan en el problema	|  2 | - |
|Ecuación que relaciona adecuadamente las variables del problema	|  1  | - |
|No es solo cálculo directo	|  2  | - |
|Al menos un bucle (variable de control, condición de parada)	|  2  | - |
|Al menos una sentencia condicional significativa |	2 | - |
|Menú repetitivo hasta “Salir”		| 2 | - |
|Sin listas, diccionarios, tuplas ni sets |	2   | - |
|Declaración de uso de IA (si aplica) |	 2   |-|

---

## 2. Calcula el centro de gravedad de un avión de carga:
Un avión tiene varias zonas de carga distribuidas a lo largo de su fuselaje. Con el número de zonas de carga, la posición de cada zona respecto al punto de referencia (en metros) y el peso cargado en cada zona (en kilogramos). Calcula el centro de gravedad (CG) de la aeronave con la fórmula:    CG = (Σ (peso × posición)) / Σ peso
Al final, muestra el valor del CG y alerta si está fuera del rango permitido para la operación segura del avión.

### Tabla de Análisis:

| Variable de entrada | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Zonas | Número de zonas de carga del avión | Variable tipo int |
| Posición | Posición de cada zona respecto al punto de referencia | Variable tipo int |
| Peso | Peso cargado en cada zona | Variable tipo int |

| Variable de salida | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| CG | Centro de gravedad calculado de la aeronave | Variable tipo float |
| Alerta | Mensaje si el CG está fuera del rango permitido | Variable tipo str |

| Variable de control | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| CG | Centro de gravedad calculado de la aeronave | Variable tipo float |
| Alerta | Mensaje si el CG está fuera del rango permitido | Variable tipo str |

| Constantes | Descrición | 
|---------------------|------------|
| rango_min| Rango minimo del centro de gravedad |
| rango_max | Rango maximo del CG |

Nota: Se uso la IA para pedirle que de redactara el enunciado en base a lo que yo le dije que queria (Un ejercicio que se pudiera hacer con bucle en python sobre ingenieria aeronautica y fuera sobre el centro de gravedad de una aeronave).

### Rúbrica:
|Requisito	|Cumple (2) Cumple Parcialmente (1) No cumple (0) |	Evidencia (página/tabla/figura/sección) |
|-----------|-------------------------------------------------|-----------------------------------------|
|Contexto aeronáutico claro y relevante | 2 | - |
|Clara definición y clasificación de las variables de entrada, salida, de control e intermedias	|  2  | - |
|Clara definición de las constantes que se utilizan en el problema	|  1 | - |
|Ecuación que relaciona adecuadamente las variables del problema	|  2  | - |
|No es solo cálculo directo	|  1  | - |
|Al menos un bucle (variable de control, condición de parada)	|  2  | - |
|Al menos una sentencia condicional significativa |	1 | - |
|Menú repetitivo hasta “Salir”		| 2 | - |
|Sin listas, diccionarios, tuplas ni sets |	2   | - |
|Declaración de uso de IA (si aplica) |	 2   |-|




