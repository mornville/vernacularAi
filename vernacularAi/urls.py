
from django.conf.urls import url
from assignment import views

urlpatterns = [
    url(r'^finite_entity/', views.finite_entity, name = 'finite_entity'),
    url(r'^numeric_entity/', views.numeric_entity, name='numeric_entity'),

    url(r'', views.index, name='landing')
]
