# proveedor/decorators.py (o al inicio de views.py)

from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from proveedor.models import Proveedor

def proveedor_login_required(view_func):
    """
    Decorador que verifica si hay un proveedor logueado usando SESIONES.
    Reemplaza la verificación de variable global.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        proveedor_id = request.session.get('proveedor_id')
        
        if not proveedor_id:
            messages.warning(request, 'Debes iniciar sesión como proveedor.')
            return redirect('proveedores:login_proveedor')
        
        # Verificar que el proveedor existe en la BD
        try:
            proveedor = Proveedor.objects.get(id=proveedor_id)
        except Proveedor.DoesNotExist:
            request.session.flush()
            messages.error(request, 'Sesión inválida.')
            return redirect('proveedores:login_proveedor')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view