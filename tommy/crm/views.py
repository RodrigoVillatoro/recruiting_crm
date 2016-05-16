from django.shortcuts import get_object_or_404, render


from .models import Company, Contact, Process, Skill


def company_list(request):
    return render(
        request,
        'crm/company_list.html',
        {'company_list': Company.objects.all()})


def company_detail(request, slug):
    company = get_object_or_404(Company, slug__iexact=slug)
    return render(request, 'crm/company_detail.html', {'company': company})


def contact_list(request):
    return render(
        request,
        'crm/contact_list.html',
        {'contact_list': Contact.objects.all()})


def contact_detail(request, slug):
    contact = get_object_or_404(Contact, slug__iexact=slug)
    return render(request, 'crm/contact_detail.html', {'contact': contact})


def skill_list(request):
    return render(
        request,
        'crm/skill_list.html',
        {'skill_list': Skill.objects.all()})


def skill_detail(request, slug):
    skill = get_object_or_404(Skill, slug__iexact=slug)
    return render(request, 'crm/skill_detail.html', {'skill': skill})


def process_list(request):
    return render(
        request,
        'crm/process_list.html',
        {'process_list': Process.objects.all()})


def process_detail(request, slug):
    process = get_object_or_404(Process, slug__iexact=slug)
    return render(request, 'crm/process_detail.html', {'process': process})