from django.urls import path
from . import views
app_name='productos'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:producto_id>', views.detalle,name='detalle'),
    path('formulario',views.formulario,name='formulario'),
    path('<int:producto_id>/editar/',views.editar,name='editar'),
    path('<int:producto_id>/eliminar/',views.eliminar,name='eliminar'),
]