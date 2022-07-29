from django.urls import path

from . import views

urlpatterns = [

    path("",views.index, name="index"),
    path("<int:company_id>",views.company, name="company"),
    path("<int:company_id>/recordcompany",views.recordcompany, name="recordcompany")
]

