from django.shortcuts import get_object_or_404, render


from .models import Company


def homepage(request):
    company_list = Company.objects.all()
    return render(
        request, 'crm/company_list.html', {'company_list': company_list})
