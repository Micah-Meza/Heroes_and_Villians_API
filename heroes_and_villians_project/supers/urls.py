from django.urls import path
from . import views
# from .views import SuperList


urlpatterns = [
    path('', views.super_list),
    # path('super/', views.super_list),
    # path('villian/', views.super_list),
    path('<int:pk>/', views.super_detail),
    # path('', views.SuperList.as_view()),
]