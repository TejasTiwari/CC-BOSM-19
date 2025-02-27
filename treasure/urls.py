from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('googlesignin/', views.renderLogin, name='render-login'),
    path('profile/', views.renderToken, name='render-token'),
    # path('team_register', views.team_register, name='team_register'),
    path('create_team/', views.create_team, name='create_team'),
    path('join_team/', views.join_team, name='join_team'),
    path('question_details/', views.question_details, name='question_details'),
    path('check_question_answer/', views.check_question_answer, name='check_question_answer'),
]
