from django.contrib import admin
from django.urls import path
from CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id_persona>/', views.detalles, name='detalles')
]
