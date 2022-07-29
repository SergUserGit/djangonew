from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Company

# Create your views here.
def index(request):
    return render(request,"learnproject/index.html",
        {"companies":Company.objects.all()})

def company(request,company_id):
    company = Company.objects.get(pk=company_id)
    return render(request,"learnproject/company.html",
    {"company":company,"non_companies":Company.objects.exclude(companies=company).all()})

def recordcompany(request,company_id):
    if request.method == "POST":
        company = Company.objects.get(pk=company_id)
        company_element = Company.objects.get(pk=int(request.POST["company"]))
        company_element.add(company)
        return HttpResponseRedirect(reverse("company",args=(company.id,)))
