"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from ohgeez import views

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='index'),
    url(r'^items/category=(?P<category>[0-9]{1,4})/$', views.ItemListView.as_view(), name='item-list'),
    url(r'^items/', views.ItemListView.as_view()),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^item/add/', views.CreateItemView.as_view(), name='add-item'),
    path('<slug:slug>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('admin/', admin.site.urls),
]
