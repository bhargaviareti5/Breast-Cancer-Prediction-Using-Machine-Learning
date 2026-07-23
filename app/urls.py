from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('cancer', views.cancer_dataset, name='cancer'),
    path('cancer_model', views.cancer_model, name='cancer_model'),
    path('cancer_predict', views.cancer_prediction, name='cancer_predict'),
    path('diabetes', views.diabetes_dataset, name='diabetes'),
    path('diabetes_model', views.diabetes_model, name='diabetes_model'),
    path('diabetes_predict', views.diabetes_prediction, name='diabetes_predict'),
    
]