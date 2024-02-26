from django.urls import path
from ADD import views
urlpatterns = [
    path('', views.index, name="index"),
    path('deleting/<int:pk>', views.data_to_delete, name='delete'),
    path('login_form', views.login_form, name='login')
]