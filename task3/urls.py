from django.urls import path
from.import views

urlpatterns = [
    path('country/', views.form, name="country"),
]