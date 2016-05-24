from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, View

from .forms import (CompanyForm, CompanyNoteForm, ContactForm, ProcessForm,
                    ProcessNoteForm, SkillForm)
from .models import Company, Contact, Process, Skill
from .utils import (ObjectDeleteMixin, ObjectListMixin,
                    ObjectUpdateMixin)


class CompanyCreate(CreateView):
    form_class = CompanyForm
    template_name = 'crm/company_form.html'


class CompanyDelete(ObjectDeleteMixin, View):
    model = Company
    success_url = reverse_lazy('crm_company_list')
    template_name = 'crm/company_confirm_delete.html'


class CompanyDetail(DetailView):
    model = Company


class CompanyList(ObjectListMixin, View):
    model = Company
    template_name = 'crm/company_list.html'


class CompanyUpdate(ObjectUpdateMixin, View):
    form_class = CompanyForm
    model = Company
    template_name = 'crm/company_form_update.html'


class CompanyNoteCreate(CreateView):
    form_class = CompanyNoteForm
    template_name = 'crm/company_note_form.html'


class ContactCreate(CreateView):
    form_class = ContactForm
    template_name = 'crm/contact_form.html'


class ContactDelete(ObjectDeleteMixin, View):
    model = Contact
    success_url = reverse_lazy('crm_contact_list')
    template_name = 'crm/contact_confirm_delete.html'


class ContactDetail(DetailView):
    model = Contact


class ContactList(ObjectListMixin, View):
    model = Contact
    template_name = 'crm/contact_list.html'


class ContactUpdate(ObjectUpdateMixin, View):
    form_class = ContactForm
    model = Contact
    template_name = 'crm/contact_form_update.html'


class ProcessCreate(CreateView):
    form_class = ProcessForm
    template_name = 'crm/process_form.html'


class ProcessDelete(ObjectDeleteMixin, View):
    model = Process
    success_url = reverse_lazy('crm_process_list')
    template_name = 'crm/process_confirm_delete.html'


class ProcessDetail(DetailView):
    model = Process


class ProcessList(ObjectListMixin, View):
    model = Process
    template_name = 'crm/process_list.html'


class ProcessUpdate(ObjectUpdateMixin, View):
    form_class = ProcessForm
    model = Process
    template_name = 'crm/process_form_update.html'


class ProcessNoteCreate(CreateView):
    form_class = ProcessNoteForm
    template_name = 'crm/process_note_form.html'


class SkillCreate(CreateView):
    form_class = SkillForm
    template_name = 'crm/skill_form.html'


class SkillDetail(DetailView):
    model = Skill


class SkillList(ObjectListMixin, View):
    model = Skill
    template_name = 'crm/skill_list.html'

