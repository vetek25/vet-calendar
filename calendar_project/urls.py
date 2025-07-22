from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ админка работает
    path('', views.home, name='home'),  # ✅ главная страница
    path('login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('wait/', views.wait_screen, name='wait_screen'),
    
    # ❌ Удали эту строку — она вызывает конфликт:
    # path('', include('events.urls')),
]
