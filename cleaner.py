import re

def clean_file(register):
    # Patrón regex básico para validar correos (en proceso de mejora)
    # ACTUALIZACIÓN: Se quitó la validación de mayúsculas porque los registros
    # Serán analizados en lowercase
    patron = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    try:
        # Se verifica que exista el registro y que sea un string
        # No se muestra un error para que se sigan recorriendo las demás filas
        if not register or not isinstance(register, str):
            return None
        
        # Se eliminan espacios y se coloca en minúsculas
        email = register.strip().lower()

        # Lee el patrón y lo compara con el email
        if re.match(patron, email):
            # Corrección: Se retorna el email en vez del register, para mantener
            # registros con formato en minúsculas
            return email
        else: 
            return
    except Exception as e:
        print(f"\n❌ Error crítico en archivo: {e}")
        return