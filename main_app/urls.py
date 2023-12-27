from django.urls import path
import main_app.views as vw

app_name = 'main_app'

urlpatterns = [
    path('', vw.index, name='index'),
    path('city/', vw.city, name='city')
]
