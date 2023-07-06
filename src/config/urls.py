"""RiseOnlineWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from articles.views import index, SignUpView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('special_admin_page/', admin.site.urls),
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('skills/', include('skills.urls'), name="skills"),
    path('quests/', include('quests.urls'), name="quests"),
    path('zones/', include('zones.urls'), name="zones"),
    path('monsters/', include('monsters.urls'), name="monsters"),
    path('items/', include('items.urls'), name="items"),
    path('contacts/', include('contacts.urls'), name="contacts"),
    path('articles/', include('articles.urls'), name="articles")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
