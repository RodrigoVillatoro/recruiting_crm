from django.shortcuts import get_object_or_404, render


from .models import Company, Skill


def company_list(request):
    return render(
        request,
        'crm/company_list.html',
        {'company_list': Company.objects.all()})


def company_detail(request, slug):
    company = get_object_or_404(Company, slug__iexact=slug)
    return render(request, 'crm/company_detail.html', {'company': company})


def skill_list(request):
    return render(
        request,
        'crm/skill_list.html',
        {'skill_list': Skill.objects.all()})


def skill_detail(request, slug):
    skill = get_object_or_404(Skill, slug__iexact=slug)
    return render(request, 'crm/skill_detail.html', {'skill': skill})