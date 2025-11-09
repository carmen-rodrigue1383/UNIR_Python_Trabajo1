"""
Funciones para mostrar mensajes al usuario, opcionalmente algunos mensajes reciben parámetros para personalizar el mensaje.
"""
mensaje_materia_invalida = lambda: print ("No ha introducido un nombre para la materia")
mensaje_calificacion_invalida = lambda calificacion: print(f"Por favor, ingrese una calificación válida (número entre 0 y 10). Ha introducido '{calificacion}'")
mensaje_sin_calificaciones_para_funcionalidad = lambda funcionalidad: print(f"No se han aportado calificaciones para {funcionalidad}")
mensaje_materia_duplicada = lambda materia: print(f"La materia '{materia}' ya ha sido ingresada. Por favor, ingrese una materia diferente.")
mensaje_error_calculo_promedio = lambda: print("Ha ocurrido un error al calcular el promedio de las calificaciones, se considera 0")