from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from usuarios.models import Comerciante, Beneficio, Post
from usuarios.views import get_current_user

from .forms import (
    ComercianteAdminForm,
    BeneficioAdminForm,
    PostAdminForm,
)

# ======================================================
# VERIFICAR SI EL USUARIO ES ADMINISTRADOR
# ======================================================

def require_admin(request):
    user = get_current_user(request)
    return user is not None and user.rol == 'ADMIN'


# ======================================================
# PANEL ADMINISTRADOR
# ======================================================

def panel_admin_view(request):
    if not require_admin(request):
        messages.error(request, 'Debes iniciar sesión como administrador.')
        return redirect('registro')

    admin_user = get_current_user(request)
    comerciantes = Comerciante.objects.all().order_by('-fecha_registro')

    return render(request, 'administrador/panel_admin.html', {
        'comerciantes': comerciantes,
        'admin': admin_user,
    })


# ======================================================
# COMERCIANTES
# ======================================================

def crear_comerciante_view(request):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    if request.method == 'POST':
        form = ComercianteAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comerciante creado correctamente.")
            return redirect('panel_admin')
    else:
        form = ComercianteAdminForm()

    return render(request, "administrador/crear_comerciante.html", {
        "form": form
    })


def editar_comerciante_view(request, comerciante_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    comerciante = get_object_or_404(Comerciante, id=comerciante_id)

    if request.method == 'POST':
        form = ComercianteAdminForm(request.POST, instance=comerciante)
        if form.is_valid():
            form.save()
            messages.success(request, "Comerciante actualizado correctamente.")
            return redirect('panel_admin')
    else:
        form = ComercianteAdminForm(instance=comerciante)

    return render(request, "administrador/editar_comerciante.html", {
        "form": form,
        "comerciante": comerciante,
    })


def eliminar_comerciante_view(request, comerciante_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    comerciante = get_object_or_404(Comerciante, id=comerciante_id)

    if request.method == 'POST':
        comerciante.delete()
        messages.success(request, "Comerciante eliminado correctamente.")
        return redirect('panel_admin')

    return render(request, "administrador/confirmar_eliminar.html", {
        "comerciante": comerciante
    })


# ======================================================
# BENEFICIOS
# ======================================================

def admin_beneficios_list(request):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    admin_user = get_current_user(request)
    beneficios = Beneficio.objects.all().order_by('-fecha_creacion')

    return render(request, 'administrador/beneficios_list.html', {
        'beneficios': beneficios,
        'admin': admin_user,
    })


def crear_beneficio_view(request):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    if request.method == 'POST':
        form = BeneficioAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Beneficio creado correctamente.")
            return redirect('admin_beneficios')
    else:
        form = BeneficioAdminForm()

    return render(request, 'administrador/beneficio_form.html', {
        'form': form,
    })


def editar_beneficio_view(request, beneficio_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    beneficio = get_object_or_404(Beneficio, id=beneficio_id)

    if request.method == 'POST':
        form = BeneficioAdminForm(request.POST, request.FILES, instance=beneficio)
        if form.is_valid():
            form.save()
            messages.success(request, "Beneficio actualizado correctamente.")
            return redirect('admin_beneficios')
    else:
        form = BeneficioAdminForm(instance=beneficio)

    return render(request, 'administrador/beneficio_form.html', {
        'form': form,
        'beneficio': beneficio,
    })


def eliminar_beneficio_view(request, beneficio_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    beneficio = get_object_or_404(Beneficio, id=beneficio_id)

    if request.method == 'POST':
        beneficio.delete()
        messages.success(request, "Beneficio eliminado correctamente.")
        return redirect('admin_beneficios')

    return render(request, 'administrador/beneficio_confirmar_eliminar.html', {
        'beneficio': beneficio
    })


# ======================================================
# POSTS
# ======================================================

def admin_posts_list(request):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    admin_user = get_current_user(request)
    posts = Post.objects.select_related('comerciante').order_by('-fecha_publicacion')

    return render(request, 'administrador/posts_list.html', {
        'posts': posts,
        'admin': admin_user,
    })


def crear_post_admin_view(request):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    admin_user = get_current_user(request)

    if request.method == 'POST':
        form = PostAdminForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.comerciante = admin_user
            post.save()
            messages.success(request, "Post creado correctamente.")
            return redirect('admin_posts')
    else:
        form = PostAdminForm()

    return render(request, 'administrador/post_form.html', {
        'form': form,
    })


def editar_post_admin_view(request, post_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    post = get_object_or_404(Post, id=post_id)
    admin_user = get_current_user(request)

    if post.comerciante != admin_user:
        messages.error(request, "Solo puedes editar tus propias publicaciones.")
        return redirect('admin_posts')

    if request.method == 'POST':
        form = PostAdminForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente.")
            return redirect('admin_posts')
    else:
        form = PostAdminForm(instance=post)

    return render(request, 'administrador/post_form.html', {
        'form': form,
        'post': post,
    })


def eliminar_post_admin_view(request, post_id):
    if not require_admin(request):
        messages.error(request, 'Acceso denegado.')
        return redirect('registro')

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post eliminado correctamente.")
        return redirect('admin_posts')

    return render(request, 'administrador/post_confirmar_eliminar.html', {
        'post': post
    })
