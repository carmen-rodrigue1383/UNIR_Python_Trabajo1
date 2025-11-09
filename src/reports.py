def materias(parametros):
    """
    Genera un reporte de materias a partir de un diccionario de parámetros.
    Args:
        parametros (dict): Diccionario que contiene los datos necesarios para producir el reporte.
            Claves esperadas y su significado:
                - 'calificaciones_por_materia' (dict): Diccionario con todas las materias y sus calificaciones
                - 'promedio' (float): Promedio global de las calificaciones.
                - 'aprobadas' (dict): Relacion de materias aprobadas con sus calificaciones.
                - 'reprobadas' (dict): Relación de materias reprobadas con sus calificaciones.
                - 'mejor_materia' (str): Nombre de la materia con la mayor calificación.
                - 'mejor_calificacion' (float): Valor de la mayor calificación.
                - 'peor_materia' (str): Nombre de la materia con la menor calificación.
                - 'peor_calificacion' (float): Valor de la menor calificación.
    Raises:
        KeyError: Si falta alguna clave requerida en el diccionario `parametros`.
        TypeError: Si alguno de los valores tiene un tipo diferente al esperado.    
    """    

    print("=============================")
    print("- Resumen Final de Materias -")
    print("=============================")

    calificaciones_por_materia = parametros['calificaciones_por_materia']
    promedio = parametros['promedio']
    aprobadas = parametros['aprobadas']
    reprobadas = parametros['reprobadas']
    mejor_materia = parametros['mejor_materia']
    mejor_calificacion = parametros['mejor_calificacion']
    peor_materia = parametros['peor_materia']
    peor_calificacion = parametros['peor_calificacion']

    print("\nTodas las Materias:")
    for materia, calificacion in parametros['calificaciones_por_materia'].items():
        print(f"- {materia}: {calificacion:.2f}")

    print(f"Promedio General: {promedio:.2f}")    

    if(aprobadas == {}):
        print("\nNo hay materias aprobadas.")
    else:
        print("\nMaterias Aprobadas:")
        for materia, calificacion in aprobadas.items():
            print(f"- {materia}: {calificacion:.2f}")
    
    if(reprobadas == {}):
        print("\nNo hay materias reprobadas.")
    else:
        print("\nMaterias Reprobadas:")
        for materia, calificacion in reprobadas.items():
            print(f"- {materia}: {calificacion:.2f}")
    
    print("\nMateria con Mejor Calificación:")
    print(f"- {mejor_materia}: {mejor_calificacion:.2f}")
    
    print("\nMateria con Peor Calificación:")
    print(f"- {peor_materia}: {peor_calificacion:.2f}")

