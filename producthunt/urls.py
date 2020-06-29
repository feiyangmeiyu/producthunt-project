from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
	path('', views.home, name='home'),
	path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
