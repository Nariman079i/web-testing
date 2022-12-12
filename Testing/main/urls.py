from django.urls import path
from main.views import *
urlpatterns = [
    path('test/',TestApi.as_view()),
    path('test/<int:pk>/', QuetionApi.as_view()),
    path('tests/', TestView),
    path('tests/<int:id>/', QuestionView , name='quetions')
]