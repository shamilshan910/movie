from django.urls import path, include
from . import views
app_name="movie_app"
urlpatterns = [

    path('',views.index),
    path('movie/<int:list_id>/', views.detial,name='detials'),
    path('post/',views.post1,name='post1'),
    path('update/<int:form_id>/',views.update1,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('dit',views.sample_list.as_view(),name='dit'),


]