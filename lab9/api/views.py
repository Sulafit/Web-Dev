from django.shortcuts import render


# Create your views here.
from django.http import JsonResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = {'companies': list(companies.values())}
    return JsonResponse(data)

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
        data = {'company': {
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address,
            
        }}
    except Company.DoesNotExist:
        data = {'error': 'Company not found'}
    return JsonResponse(data)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        data = {'vacancy': {
            'name': vacancy.name,
        }}
    except Vacancy.DoesNotExist:
        data = {'error': 'Vacancy not found'}
    return JsonResponse(data)

def company_vacancies(request, id):
    # try:
        company = Company.objects.get(id=id)
        vacancies = Company.product_set.all()
        data = {'vacancies': list(vacancies.values())}
    # except Company.DoesNotExist:
        # data = {'error': 'Company not found'}
        return JsonResponse(data)




def top_10_vacancies(request):
    try:
        # company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.order_by('-salary')[:10]

        data = {'vacancies': list(vacancies.values())}
    except Vacancy.DoesNotExist:
        data = {'error': 'Company not found'}
    return JsonResponse(data)


