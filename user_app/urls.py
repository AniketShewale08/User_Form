from django.urls import re_path
from . import views

    
app_name = 'user_app'

urlpatterns = [
    re_path(r'',views.UserCreateView.as_view(),name='new')
]
