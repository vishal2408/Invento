from django.conf.urls import url
from django.contrib import admin
from . import views
from home.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', HomeView.as_view()),
    url(r'^dashboard/', views.dashboard, name='dashboard')
]