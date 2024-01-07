


from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Quotes, name="home"),
    path('Author_search_results',views.Authors, name="Author"),
]
