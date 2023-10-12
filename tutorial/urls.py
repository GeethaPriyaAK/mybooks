
from django.urls import path, include
from . import views

urlpatterns=[
    path('tutorials',views.Book_list),
    path('tutorial/<int:pk>',views.Book_detail),

]