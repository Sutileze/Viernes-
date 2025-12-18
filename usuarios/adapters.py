# usuarios/adapters.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def is_auto_signup_allowed(self, request, sociallogin):
        """
        SIEMPRE permitir signup automático.
        """
        return True
    
    def populate_user(self, request, sociallogin, data):
        """
        Poblar datos del usuario desde la cuenta social.
        """
        user = super().populate_user(request, sociallogin, data)
        
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            user.email = extra_data.get('email', '')
            user.nombre_apellido = extra_data.get('name', '')
            user.first_name = extra_data.get('given_name', '')
            user.last_name = extra_data.get('family_name', '')
        
        return user
    
    def save_user(self, request, sociallogin, form=None):
        """
        Guardar usuario sin requerir formulario.
        """
        user = sociallogin.user
        user.set_unusable_password()
        user.save()
        return user