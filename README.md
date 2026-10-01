# Fundamentos de IA — Laboratorio

Repositorio de prácticas de la materia **Fundamentos de Inteligencia Artificial**. Contiene tres componentes independientes: un pipeline de series temporales, modelos de IA que corren de forma local y una comparativa de *vibe coding*.

## Estructura del proyecto

```
fundamentos-ia-lab/
├── modelos_locales/          # Consumo de APIs de LLMs locales
│   ├── ollama_test.py        # Ollama (puerto 11434) — /api/generate
│   └── lmstudio_test.py      # LM Studio (puerto 1234) — API estilo OpenAI
├── serie_temporal/           # Pipeline completo de forecasting
│   ├── api_client.py         # 1. Extracción de datos (CoinGecko)
│   ├── preprocessing.py      # 2. Transformación (features + train/test split)
│   ├── model.py              # 3. Modelado (baseline vs. regresión lineal)
│   ├── evaluation.py         # 4. Evaluación (MAE/RMSE + gráfico)
│   └── app.py                # Orquestador del pipeline
├── vibe_coding/
│   └── comparativo.md        # Análisis local vs. cloud
├── requerimientos.txt
└── README.md
```

## Requisitos

- **Python 3.13** (probado en 3.13.14, Windows)
- Para el componente de modelos locales: **Ollama** o **LM Studio** con un modelo cargado y su servidor local activo.
- Para el pipeline de series temporales: conexión a internet (API pública de CoinGecko).

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requerimientos.txt
```

## Uso

### 1. Pipeline de series temporales

Analiza el precio de Bitcoin de los últimos 365 días y compara un modelo de regresión lineal contra un *baseline* ingenuo (*naive*: el precio de hoy es igual al de ayer).

```bash
python serie_temporal/app.py
```

El pipeline se ejecuta en cuatro etapas, cada una en su propio módulo:

1. **Extracción** — `api_client.py` descarga los precios diarios desde CoinGecko y devuelve la lista `prices`.
2. **Transformación** — `preprocessing.py` construye un `DataFrame` indexado por fecha, crea la variable de rezago `precio_ayer` (`shift(1)`) y divide el conjunto 80/20 de forma cronológica, sin barajar.
3. **Modelado** — `model.py` entrena un `LinearRegression` y genera la predicción del modelo junto con la predicción *naive* de referencia.
4. **Evaluación** — `evaluation.py` calcula **MAE** y **RMSE** para ambas estrategias y muestra una gráfica con la serie real, el baseline y la regresión.

> La comparación con el *baseline* es intencional: en series temporales el valor de un modelo solo es interpretable si supera la trivial de "repetir el último valor conocido".

**Salida esperada:**

```
--- RESULTADOS DE LAS MÉTRICAS ---
BASELINE (Naive) -> MAE: $... | RMSE: $...
MODELO (Regresión) -> MAE: $... | RMSE: $...
```

### 2. Modelos locales

Los dos scripts son intercambiables en propósito: ambos miden tiempo de respuesta y devuelven un "registro técnico" como evidencia de ejecución.

**Ollama** — requiere los modelos descargados con `ollama pull <modelo>`:

```bash
python modelos_locales/ollama_test.py
```

Ejecuta dos pruebas: un modelo generalista (`gemma4:latest`) y uno especializado en código (`qwen2.5-coder:1.5b`). Endpoint: `http://localhost:11434/api/generate`.

**LM Studio** — requiere el *Local Server* encendido en el puerto 1234:

```bash
python modelos_locales/lmstudio_test.py
```

Endpoint: `http://localhost:1234/v1/chat/completions`, con formato de mensajes estilo OpenAI y parametrización por `temperature`.

### 3. Vibe coding: comparativa local vs. cloud

`vibe_coding/comparativo.md` documenta el mismo reto de programación (validador y clasificador de clases de red IPv4) resuelto con un modelo local pequeño y con un modelo en la nube. Incluye el prompt utilizado, el código generado por cada modelo, una tabla comparativa por criterio (velocidad, lógica, calidad de código, manejo de errores) y las conclusiones.

## Dependencias

Ver [`requerimientos.txt`](requerimientos.txt):

| Paquete | Uso |
| :--- | :--- |
| `pandas` | Manipulación del `DataFrame` de la serie temporal |
| `numpy` | Cálculo de RMSE |
| `scikit-learn` | `LinearRegression` y métricas (`mean_absolute_error`, `mean_squared_error`) |
| `matplotlib` | Visualización de la serie y las predicciones |
| `requests` | Cliente HTTP para CoinGecko, Ollama y LM Studio |

## Notas

- Los módulos usan **imports absolutos** (`from api_client import ...`), por lo que los scripts deben ejecutarse desde dentro de su propia carpeta o con esa carpeta en el `PYTHONPATH`.
- El modelo del *pipeline* usa una sola variable predictora. Es una base deliberadamente sencilla para contrastar con el *baseline*, no una estrategia de producción.