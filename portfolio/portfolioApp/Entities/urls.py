from django.urls import path,include
from rest_framework import routers

from . import views
from .views import PersonList, PersonDetail, ExperienceList, ExperienceDetail, get_all_Person, add_person, \
   delete_person, PersonsView
from .views import JustificationList, JustificationDetail, InfoPersList, InfoPersDetail
from .views import retreive_update_or_delete_infopers, retreive_update_or_delete_Person, retreive_update_or_delete_Experience, retreive_update_or_delete_Justification
from .views import delete_Exp, add_Exp, get_all_Exp , add_just, get_all_Just, delete_just, add_InfoPers, delete_InfoPers , get_all_InfoPers, UpdateExperience ,UpdateInfoPers , PersonAdd , UserCoord
from .ViewSet import PersonViewSet, JustificationViewSet, ExperienceViewSet, InfoPersViewSet
from . import views
from django.contrib.auth.views import LoginView , LogoutView
urlpatterns = [
    path('', views.indexView, name="home"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path(r'logout/', LogoutView.as_view(next_page='home'), name="logout"),
    path(r'portfolio/', views.PortfolioAffiche, name="portfolioAffiche"),


    path(r'form/', views.PersonAdd),
    path(r'User/', views.UserCoord, name="AddInfo"),
    path(r'User/Update/<int:pk>/', views.UserUpdate, name="UpdateInfo"),
    path(r'ExperinceForm/', views.UserExperience, name="ExpForm"),
    path(r'JustificationForm/', views.UserJustification, name="JustForm"),
    path(r'Experience/Affiche/',views.ExperienceAffiche , name="AfficherExp"),
    path(r'Justification/Affiche/',views.JustificationAffiche, name ="AfficheJust"),
    path(r'UserAffiche/',views.UserAffiche , name="userAffiche"),

    path(r'Persons/all/', views.get_all_Person),
    path(r'Persons/add/', views.add_person),
    path(r'Persons/delete/<int:id>', views.delete_person),
    path(r'person/<int:id>', views.retreive_update_or_delete_Person),
    
    path(r'Experience/all/', get_all_Exp),
    path(r'Experience/add/', add_Exp),
    path(r'Experience/delete/<int:id>', delete_Exp),
    path(r'Experience/<int:id>', retreive_update_or_delete_Experience),
    path(r'Experience/Update/<int:id>',UpdateExperience),


    path(r'Justification/all/', get_all_Just),
    path(r'Justification/add/', add_just),
    path(r'Justification/delete/<int:id>', delete_just),
    path(r'Justification/<int:id>', retreive_update_or_delete_Justification),


    path(r'InfoPers/all/', get_all_InfoPers),
    path(r'InfoPers/add/', add_InfoPers),
    path(r'InfoPers/delete/<int:id>', delete_InfoPers),
    path(r'infoPers/<int:id>', retreive_update_or_delete_infopers),
    path(r'InfoPers/Update/<int:id>', UpdateInfoPers),


    path('Person/', PersonList.as_view()),
    path('Person/<int:pk>/', PersonDetail.as_view()),
    path('Experience/', ExperienceList.as_view()),
    path('Experience/<int:pk>/', ExperienceDetail.as_view()),
    path('Justification/', JustificationList.as_view()),
    path('Justification/<int:pk>/', JustificationDetail.as_view()),
    path('InfoPers/', InfoPersList.as_view()),
    path('InfoPers/<int:pk>/', InfoPersDetail.as_view()),
]



