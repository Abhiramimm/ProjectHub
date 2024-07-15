"""
URL configuration for ProjectHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from codestore import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

     path("register/",views.RegistrationView.as_view(),name="register"),

    path("",views.LoginView.as_view(),name="signin"),

    path("projects/add/",views.ProjectCreateView.as_view(),name="project-add"),

    path("projects/all/",views.ProjectListView.as_view(),name="project-list"),
    
    path("projects/<int:pk>/",views.ProjectDetailView.as_view(),name="project-detail"),

    path("projects/<int:pk>/edit/",views.ProjectUpdateView.as_view(),name="project-edit"),

    path("projects/<int:pk>/delete/",views.ProjectDeleteView.as_view(),name="project-delete"),

    path("signout/",views.SignOutView.as_view(),name="signout"),

    path("userhome/",views.UserHomeView.as_view(),name="user-home"),

    path("wishlist/<int:pk>/add/",views.AddtoWishListView.as_view(),name="addtowish"),

    path("wishlist/all/",views.WishListView.as_view(),name="wish-list"),

    path("wishlist/<int:pk>/remove/",views.RemoveWishlistItem.as_view(),name="remove-wish"),



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

