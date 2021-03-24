from django.urls import path, re_path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('alterar-dados', views.update_user, name='update_user'),
    path('alterar-senha', views.update_password, name='update_password'),
    path('registro', views.register, name='register'),
    path('entrar/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
    path('recuperar-senha/', views.password_reset_request, name='password_reset'),
    #path('accounts/', include('django.contrib.auth.urls')),
    # recuper senha
    # path('recuperar-senha/', views.PasswordResetView.as_view(
    #     template_name='accounts/password_reset.html'),
    #     name='password_reset'
    # ),
    path('recuperar-senha-ok/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password/password_reset_done.html'),
        name='password_reset_done',
    ),
    path('recuperar-senha-completo/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password/password_reset_complete.html'),
        name='password_reset_complete',
    ),
    path('recuperar-senha-confirmar/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_confirm.html',
        success_url=reverse_lazy("accounts:password_reset_complete")),
        name='password_reset_confirm'
    ),
    path('password_reset_confirm', views.password_reset_request, name="password_reset")
    
]
