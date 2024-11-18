from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_account/', views.create_account_view, name='create_acc'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='../templates/pages-recoverpw.html'),
         name='forgot_pass'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='../templates/pages-recoverpw-done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='../templates/pages-recoverpw-confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='../templates/pages-recoverpw-complete.html'),
         name='password_reset_complete'),

    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='../templates/pages-changepw.html'),
         name='change_password'),
    path('change_password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='../templates/pages-changepw-done.html'),
         name='password_change_done'),

    path('create-profile/', views.create_user_profile, name='create_user_profile'),
    path('switch-profile/<int:profile_id>/', views.switch_profile, name='switch_profile'),

    path('change-language/<str:language_code>/', views.change_language, name='change_language'),
]
