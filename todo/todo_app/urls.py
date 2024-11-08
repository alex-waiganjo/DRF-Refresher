from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('todos/',views.TodosView.as_view(),name='todos'),
    path('todo/<int:id>',views.TodoView.as_view(),name='todo'),
    path('api/v1/get-token',TokenObtainPairView.as_view(),name='get_token'),
    path('api/v1/refresh-token',TokenRefreshView.as_view(),name='refresh_token'),  
]