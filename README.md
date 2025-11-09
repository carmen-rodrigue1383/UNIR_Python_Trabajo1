# Calculadora de Promedios

## Descripción
Este proyecto es una calculadora de promedios académicos desarrollada como parte del Trabajo 1 del "Curso de Programación en Python" en UNIR.

- [Enunciado del ejercicio](./enunciado.md) 
- [Solución](./solucion.md)

## Estructura
```
src/
├── calculadora_promedios.py  # Módulo principal
├── constantes.py            # Constantes 
├── mensajes_usuario.py      # Mensajes para el usuario
├── prompts.py              # Funciones de entrada
└── reports.py              # Generación de reportes
```

## 🚀 Cómo empezar desde cero

### 1. Instala Anaconda (recomendado para principiantes)

🔗 [Descargar Anaconda](https://www.anaconda.com/products/distribution)

Anaconda incluye Python, Jupyter y muchas librerías útiles. Es la forma más fácil de empezar sin complicaciones.

### 2. Clona o descarga el repositorio

Desde Anaconda Prompt o tu terminal:

```cmd
git clone https://github.com/carmen-rodrigue1383/UNIR_Python_Trabajo1.git
cd UNIR_Python_Trabajo1
```
O descarga el ZIP desde GitHub y extrae la carpeta.

### 3. (Opcional) Crea un entorno virtual
```cmd
conda create -n unir_trabajo1 python=3.10
conda activate unir_trabajo1
```

### 4. Instala las dependencias
```cmd
pip install pytest pytest-cov pytest-mock
```

## Ejecutar la calculadora
```cmd
python src/calculadora_promedios.py
```
## Ejecutar los test
```cmd
pytest tests/
```
**Test con report de cobertura**
```cmd
pytest --cov=src --cov-report=html tests/
```