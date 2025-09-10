## 1. Simulación de consumo de combustible:
Pide al usuario la cantidad inicial de combustible (litros) y el consumo por hora (litros/hora). Usa un bucle para mostrar cuánto combustible queda después de cada hora de vuelo hasta que se acabe.

### Tabla de Análisis:
| Variable de entrada | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Combustible | La cantidad inicial de combustible en litros | Variable tipo int |
| Gasto | La cantidad de combustible que se consume por hora | Variable tipo int |
| Duración | Las horas que dura el vuelo | Variable tipo int |

| Variable de salida | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Resta | La cantidad de combustible que queda en el avión durante el vuelo, en litros | Variable tipo float |

| Variable de control | Descrición | Tipo de variable |
|---------------------|------------|------------------|
| Hora | Las horas del vuelo | Variable tipo int |


## 2. Calcula el centro de gravedad de un avión de carga:
Un avión tiene varias zonas de carga distribuidas a lo largo de su fuselaje. Con el número de zonas de carga, la posición de cada zona respecto al punto de referencia (en metros) y el peso cargado en cada zona (en kilogramos). Calcula el centro de gravedad (CG) de la aeronave con la fórmula:    CG = (Σ (peso × posición)) / Σ peso
Al final, muestra el valor del CG y alerta si está fuera del rango permitido para la operación segura del avión.

| Variable de salida | Descrición | Tipo de variable |
|--------------------|------------|------------------|
| Zonas | Numero de zonas de carga del avión | Variable tipo int |
| Posicion | Posición de cada zona con respecto al punto de referencia | Variable tipo float |
| Peso | Peso cargado en cada zona | Variable tipo float |

