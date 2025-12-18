from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from usuarios.views import get_current_user
from .models import TicketSoporte


# =====================================================
# VALIDADOR DE ROL TECNICO
# =====================================================
def require_tecnico(request):
    user = get_current_user(request)
    return user and user.rol == 'TECNICO'


# =====================================================
# PANEL PRINCIPAL SOPORTE
# =====================================================
def panel_soporte(request):
    if not require_tecnico(request):
        messages.error(request, 'Acceso restringido a soporte técnico.')
        return redirect('registro')

    tecnico = get_current_user(request)
    tickets = TicketSoporte.objects.all().order_by('-creado_en')

    return render(request, 'soporte/panel.html', {
        'tecnico': tecnico,
        'tickets': tickets,
    })


# =====================================================
# DETALLE TICKET (SOLO GET)
# =====================================================
def ticket_detalle(request, ticket_id):
    if not require_tecnico(request):
        messages.error(request, 'Acceso restringido.')
        return redirect('registro')

    tecnico = get_current_user(request)
    ticket = get_object_or_404(TicketSoporte, id=ticket_id)

    return render(request, 'soporte/ticket_detalle.html', {
        'ticket': ticket,
        'tecnico': tecnico,
    })


# =====================================================
# ACCIONES DEL TICKET (POST)
# =====================================================
@require_POST
def ticket_accion(request, ticket_id):
    if not require_tecnico(request):
        messages.error(request, 'Acceso restringido.')
        return redirect('registro')

    tecnico = get_current_user(request)
    ticket = get_object_or_404(TicketSoporte, id=ticket_id)

    accion = request.POST.get('accion')

    if accion == 'tomar':
        ticket.estado = 'EN_PROCESO'
        ticket.tecnico_asignado = tecnico
        messages.success(request, 'Ticket marcado EN PROCESO.')

    elif accion == 'resolver':
        ticket.estado = 'RESUELTO'
        ticket.tecnico_asignado = tecnico
        messages.success(request, 'Ticket marcado como RESUELTO.')

    elif accion == 'cerrar':
        ticket.estado = 'CERRADO'
        ticket.tecnico_asignado = tecnico
        messages.success(request, 'Ticket CERRADO.')

    else:
        messages.error(request, 'Acción no válida.')

    ticket.save()
    return redirect('soporte:ticket_detalle', ticket_id=ticket.id)


# =====================================================
# CIERRE RÁPIDO
# =====================================================
@require_POST
def cerrar_ticket(request, ticket_id):
    if not require_tecnico(request):
        messages.error(request, 'Acceso restringido.')
        return redirect('registro')

    ticket = get_object_or_404(TicketSoporte, id=ticket_id)
    ticket.estado = 'CERRADO'
    ticket.save()

    messages.success(request, 'Ticket cerrado correctamente.')
    return redirect('soporte:panel_soporte')
