import pytest
import calculadora_promedios as cp

@pytest.fixture
def test_data():
    """Fixture con datos de prueba comunes"""
    return {
        "materias": [
            "Curso de programación en Python - PER14446", 
            "Visualización Interactiva de la Información - PER14059", 
            "Ingeniería para el Procesado Masivo de Datos - PER14059", 
            "Bases de Datos para el Big Data - PER14059 OCT2025", 
            "fin"],
        "calificaciones": {
            "Curso de programación en Python - PER14446": "4.5", 
            "Visualización Interactiva de la Información - PER14059": "9.5",
            "Ingeniería para el Procesado Masivo de Datos - PER14059": "7.25",
            "Bases de Datos para el Big Data - PER14059 OCT2025": "8"
        },
        "expected_califs": [4.5,9.5,7.25,8]
    }

def test_ingresar_calificaciones(mocker, test_data):
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = test_data["materias"]
    mock_prompts.pedir_calificacion.side_effect = lambda materia: test_data["calificaciones"][materia]    
        
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias, calificaciones = cp.ingresar_calificaciones()
    assert materias == test_data["materias"][:-1]  # Excluir 'fin'
    assert calificaciones == test_data["expected_califs"]

def test_ingresar_calificaciones_con_calificacion_invalida(mocker):
    # Configurar los datos de prueba
    materias = ["Fisica", "fin"]
    calificaciones = ["abc", "9.0"]
    
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = materias
    mock_prompts.pedir_calificacion.side_effect = calificaciones
    
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias, calificaciones = cp.ingresar_calificaciones()
    
    mock_mensajes.mensaje_calificacion_invalida.assert_called_once_with("abc")
    assert materias == ["Fisica"]
    assert calificaciones == [9.0]

def test_ingresar_calificaciones_materia_vacia(mocker):
    # Configurar los datos de prueba
    materias = ["", "fin"]
    confirmacion = "s"
    
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = materias
    mock_prompts.pedir_confirmacion_finalizacion.return_value = confirmacion
    
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias, calificaciones = cp.ingresar_calificaciones()
    
    # Verificar que se muestra el mensaje de materia inválida
    mock_mensajes.mensaje_materia_invalida.assert_called_once()
    # Verificar que se pide confirmación
    mock_prompts.pedir_confirmacion_finalizacion.assert_called_once()
    # Verificar que las listas están vacías
    assert materias == []
    assert calificaciones == []

def test_ingresar_calificaciones_materia_vacia_continuar(mocker):
    # Configurar los datos de prueba
    materias = ["", "Matematicas", "fin"]
    confirmacion = "n"
    calificaciones = ["8.5"]
    
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = materias
    mock_prompts.pedir_confirmacion_finalizacion.return_value = confirmacion
    mock_prompts.pedir_calificacion.side_effect = calificaciones
    
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias_resultado, calificaciones_resultado = cp.ingresar_calificaciones()
    
    # Verificar que se muestra el mensaje de materia inválida
    mock_mensajes.mensaje_materia_invalida.assert_called_once()
    # Verificar que se pide confirmación
    mock_prompts.pedir_confirmacion_finalizacion.assert_called_once()
    # Verificar que se continúa y se guardan los datos de Matematicas
    assert materias_resultado == ["Matematicas"]
    assert calificaciones_resultado == [8.5]

def test_ingresar_calificaciones_calificacion_fuera_rango(mocker):
    # Configurar los datos de prueba
    materias = ["Matematicas", "fin"]
    calificaciones = ["11", "8.5"]  # Primera calificación fuera del rango permitido [0-10]
    
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = materias
    mock_prompts.pedir_calificacion.side_effect = calificaciones
    
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias_resultado, calificaciones_resultado = cp.ingresar_calificaciones()
    
    # Verificar que se muestra el mensaje de calificación inválida
    mock_mensajes.mensaje_calificacion_invalida.assert_called_once_with("11")
    # Verificar que se continúa y se guardan los datos correctos
    assert materias_resultado == ["Matematicas"]
    assert calificaciones_resultado == [8.5]

def test_ingresar_calificaciones_materia_duplicada(mocker):
    # Configurar los datos de prueba
    materias = ["Matematicas", "Matematicas", "Fisica", "fin"]
    calificaciones = ["8.5", "9.0"]  # La segunda materia duplicada no debería pedir calificación
    
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = materias
    mock_prompts.pedir_calificacion.side_effect = calificaciones
    
    mock_mensajes = mocker.MagicMock()
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "mensajes", mock_mensajes)

    materias_resultado, calificaciones_resultado = cp.ingresar_calificaciones()
    
    # Verificar que se muestra el mensaje de materia duplicada
    mock_mensajes.mensaje_materia_duplicada.assert_called_once_with("Matematicas")
    # Verificar que se guardan los datos correctos sin duplicados
    assert materias_resultado == ["Matematicas", "Fisica"]
    assert calificaciones_resultado == [8.5, 9.0]

def test_determinar_estado(mocker):
    calificaciones = [4.5, 9.5, 7.25, 8]
    aprobadas, reprobadas = cp.determinar_estado(calificaciones, umbral=5.0)
    assert aprobadas == [1, 2, 3]
    assert reprobadas == [0]

def test_determinar_estado_sin_calificaciones(mocker):
    # Configurar mocks
    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(cp, "mensajes", mock_mensajes)
    
    aprobadas, reprobadas = cp.determinar_estado([], umbral=5.0)
    assert aprobadas == []
    assert reprobadas == []
    # Verificar que se muestra el mensaje de "no se han introducido calificaciones para esta funcionalidad"
    mock_mensajes.mensaje_sin_calificaciones_para_funcionalidad.assert_called_once_with("calcular aprobadas y reprobadas")

def test_calcular_promedio():
    calificaciones = [4.5, 9.5, 7.25, 8]
    promedio = cp.calcular_promedio(calificaciones)
    assert promedio == 7.3125

def test_calcular_promedio_sin_calificaciones(mocker):
    # Configurar mocks
    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(cp, "mensajes", mock_mensajes)
    
    promedio = cp.calcular_promedio([])
    assert promedio == 0
    # Verificar que se muestra el mensaje de "no se han introducido calificaciones para esta funcionalidad"
    mock_mensajes.mensaje_sin_calificaciones_para_funcionalidad.assert_called_once_with("calcular el promedio")

def test_encontrar_extremos():
    calificaciones = [4.5, 9.5, 7.25, 8]
    extremos = cp.encontrar_extremos(calificaciones)
    assert extremos == {"mayor": 1, "menor": 0}

def test_encontrar_extremos_sin_calificaciones(mocker):
    # Configurar mocks
    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(cp, "mensajes", mock_mensajes)
    
    extremos = cp.encontrar_extremos([])
    assert extremos == {"mayor": 0, "menor": 0}
    # Verificar que se muestra el mensaje de "no se han introducido calificaciones para esta funcionalidad"
    mock_mensajes.mensaje_sin_calificaciones_para_funcionalidad.assert_called_once_with("encontrar extremos")

def test_main_sin_datos(mocker):
    # Configurar mocks
    mocker.patch.object(cp, "ingresar_calificaciones", return_value=([], []))
    mock_mensajes = mocker.MagicMock()
    mock_reports = mocker.MagicMock()
    
    mocker.patch.object(cp, "mensajes", mock_mensajes)
    mocker.patch.object(cp, "reports", mock_reports)
    
    cp.main()

    # Verificar que se muestra el mensaje de "no se han introducido calificaciones para esta funcionalidad"
    mock_mensajes.mensaje_sin_calificaciones_para_funcionalidad.assert_called_once_with("generar reporte")
    mock_reports.materias.assert_not_called()

def test_main(mocker, test_data):
    # Configurar mocks
    mock_prompts = mocker.MagicMock()
    mock_prompts.pedir_materia.side_effect = test_data["materias"]
    mock_prompts.pedir_calificacion.side_effect = lambda materia: test_data["calificaciones"][materia]
        
    mock_reports = mocker.MagicMock()
    parametros_para_reports = {}
    def fake_reports_materias(payload):
        parametros_para_reports.update(payload)
    mock_reports.materias = fake_reports_materias
    
    mocker.patch.object(cp, "prompts", mock_prompts)
    mocker.patch.object(cp, "reports", mock_reports)
    
    cp.main()
    
    # Calcula el promedio usando comprensión de diccionarios
    calificaciones = [float(nota) for nota in test_data["calificaciones"].values()]
    promedio_esperado = sum(calificaciones) / len(calificaciones)

    assert parametros_para_reports["promedio"] == promedio_esperado
    assert parametros_para_reports["mejor_materia"] == "Visualización Interactiva de la Información - PER14059"
    assert parametros_para_reports["peor_materia"] == "Curso de programación en Python - PER14446"