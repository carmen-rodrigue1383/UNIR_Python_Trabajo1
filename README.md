# Calculadora de Promedios

## Descripción
Calculadora de promedios para calificaciones académicas.

- [Enunciado](./enunciado.md) 
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

## Uso
```cmd
python src/calculadora_promedios.py
```

## Test
```cmd
pytest tests/
```
**Test con report de cobertura**
```cmd
pytest --cov=src --cov-report=html tests/
```