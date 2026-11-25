"""
URL configuration for MinFit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from gym_app.views import MemberCreateListView, MemberDetailView,MemberSearchView,MembershipDetailView,MembershipCreateListView,PaymentCreateListView,PaymentDetailView,DashboardView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('members/', MemberCreateListView.as_view()),

    path('members/<int:id>/', MemberDetailView.as_view()),

    path('members/search/', MemberSearchView.as_view()),

    path('memberships/', MembershipCreateListView.as_view()),

    path('memberships/<int:id>/', MembershipDetailView.as_view()),

    path('payments/', PaymentCreateListView.as_view()),

    path('payments/<int:id>/', PaymentDetailView.as_view()),

    path('dashboard/', DashboardView.as_view()),
]
