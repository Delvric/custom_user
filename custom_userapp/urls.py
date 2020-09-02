from django.urls import path
from custom_userapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.signin),
    path('signup/', views.signup),
    path('logout/', views.signout)

]
