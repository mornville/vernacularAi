
from django.contrib import admin
from django.conf.urls import url
from assignment import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^finite_entity/', views.Api1.as_view()),
    url(r'^numeric_entity/', views.Api2.as_view()),

    url(r'', views.LandingPage.index)
]
