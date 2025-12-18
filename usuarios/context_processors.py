# usuarios/context_processors.py

def comerciante_context(request):
    """
    Context processor que hace disponible el comerciante logueado
    en todos los templates de la app usuarios
    """
    comerciante_id = request.session.get('comerciante_id')
    
    if comerciante_id:
        try:
            from usuarios.models import Comerciante
            comerciante = Comerciante.objects.get(id=comerciante_id)
            return {
                'current_logged_in_comerciante': comerciante,
                'comerciante': comerciante,  # Por compatibilidad
            }
        except Comerciante.DoesNotExist:
            # Limpiar sesión si el comerciante ya no existe
            if 'comerciante_id' in request.session:
                del request.session['comerciante_id']
            return {
                'current_logged_in_comerciante': None,
                'comerciante': None,
            }
    
    return {
        'current_logged_in_comerciante': None,
        'comerciante': None,
    }