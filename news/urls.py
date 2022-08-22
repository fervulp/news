from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'), 
    path('', NewsView.as_view(), name='home'), 

    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    

    # path('news/<int:pk>/', view_news, name='view_news'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='view_news'),

    # path('news/add', add_news, name='add_news')
    path('news/add', CreateNews.as_view(), name='add_news'),

    # path('test/', test, name='test'),

    path('register/', register, name='register'),

    path('login/', user_login, name='login'),
    
    path('logout/', user_logout, name='logout')
]