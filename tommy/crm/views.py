from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from .forms import (CompanyForm, CompanyNoteForm, ContactForm, ProcessForm,
                    ProcessNoteForm, SkillForm)
from .models import Company, Contact, Process, Skill
from .utils import ObjectCreateMixin, ObjectUpdateMixin


class CompanyCreate(ObjectCreateMixin, View):
    form_class = CompanyForm
    template_name = 'crm/company_form.html'


class CompanyUpdate(ObjectUpdateMixin, View):
    form_class = CompanyForm
    model = Company
    template_name = 'crm/company_form_update.html'


class CompanyNoteCreate(ObjectCreateMixin, View):
    form_class = CompanyNoteForm
    template_name = 'crm/company_note_form.html'


class ContactCreate(ObjectCreateMixin, View):
    form_class = ContactForm
    template_name = 'crm/contact_form.html'


class ContactUpdate(ObjectUpdateMixin, View):
    form_class = ContactForm
    model = Contact
    template_name = 'crm/contact_form_update.html'


class ProcessCreate(ObjectCreateMixin, View):
    form_class = ProcessForm
    template_name = 'crm/process_form.html'


class ProcessUpdate(ObjectUpdateMixin, View):
    form_class = ProcessForm
    model = Process
    template_name = 'crm/process_form_update.html'


class ProcessNoteCreate(ObjectCreateMixin, View):
    form_class = ProcessNoteForm
    template_name = 'crm/process_note_form.html'


class SkillCreate(ObjectCreateMixin, View):
    form_class = SkillForm
    template_name = 'crm/skill_form.html'


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