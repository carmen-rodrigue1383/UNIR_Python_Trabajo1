"""
Funciones para realizar preguntas al usuario, algunas de las cuales requieren parámetros para personalizar la pregunta.
"""
pedir_confirmacion_finalizacion = lambda: input("¿Desea finalizar la introducción de materias y calificaciones? (S/N):")
pedir_materia = lambda: input("Ingrese el nombre de la materia ('fin' para finalizar): ")
pedir_calificacion = lambda materia: input(f'Ingrese la calificación (entre 0 y 10) para la materia \"{materia}": ')