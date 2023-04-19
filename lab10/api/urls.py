from django.urls import path
from .views import CompanyList, CompanyDetail, CompanyVacanciesList, VacancyList, VacancyDetail, TopTenVacanciesList

urlpatterns = [
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacanciesList.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetail.as_view()),
    path('vacancies/top_ten/', TopTenVacanciesList.as_view()),
]