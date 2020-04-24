from django.urls import path
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .CRUD import company_list, company_detail, vacancy_detail, vacancy_list, company_vacancies
from .CRUD import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
from .fbv import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail
from .cbv import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
# urlpatterns = [
#     path('companies/', views.company_list),
#     path('companies/<int:id>/', views.company_detail),
#     path('companies/<int:id>/vacancies/', views.vacancy_by_company),
#     path('vacancies/', views.vacancy_list),
#     path('vacancies/<int:id>/', views.vacancy_detail),
#     path('vacancies/top_ten/', views.top_ten)
# ]

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetails.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view())
]