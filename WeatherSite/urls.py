from django.urls import path, include

urlpatterns = [
    path('', include('main_app.urls', namespace='main_app')),
]
