def proveedor_context(request):
    """
    Context processor que hace disponible el proveedor logueado
    en todos los templates de la app proveedor
    """
    proveedor_id = request.session.get('proveedor_id')
    
    if proveedor_id:
        try:
            from proveedor.models import Proveedor
            proveedor = Proveedor.objects.get(id=proveedor_id)
            return {
                'current_logged_in_proveedor': proveedor,
                'proveedor': proveedor,  # Por compatibilidad
            }
        except Proveedor.DoesNotExist:
            # Limpiar sesión si el proveedor ya no existe
            if 'proveedor_id' in request.session:
                del request.session['proveedor_id']
            return {
                'current_logged_in_proveedor': None,
                'proveedor': None,
            }
    
    return {
        'current_logged_in_proveedor': None,
        'proveedor': None,
    }