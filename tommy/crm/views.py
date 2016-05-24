from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  UpdateView, View)

from .forms import (CompanyForm, CompanyNoteForm, ContactForm, ProcessForm,
                    ProcessNoteForm, SkillForm)
from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
from .utils import ObjectListMixin


class CompanyCreate(CreateView):
    form_class = CompanyForm
    model = Company


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('crm_company_list')


class CompanyDetail(DetailView):
    model = Company


class CompanyList(ObjectListMixin, View):
    model = Company
    template_name = 'crm/company_list.html'


class CompanyUpdate(UpdateView):
    form_class = CompanyForm
    model = Company
    template_name = 'crm/company_form_update.html'


class CompanyNoteCreate(CreateView):
    form_class = CompanyNoteForm
    model = CompanyNote


class ContactCreate(CreateView):
    form_class = ContactForm
    model = Contact


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('crm_contact_list')


class ContactDetail(DetailView):
    model = Contact


class ContactList(ObjectListMixin, View):
    model = Contact
    template_name = 'crm/contact_list.html'


class ContactUpdate(UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = 'crm/contact_form_update.html'


class ProcessCreate(CreateView):
    form_class = ProcessForm
    model = Process


class ProcessDelete(DeleteView):
    model = Process
    success_url = reverse_lazy('crm_process_list')


class ProcessDetail(DetailView):
    model = Process


class ProcessList(ObjectListMixin, View):
    model = Process
    template_name = 'crm/process_list.html'


class ProcessUpdate(UpdateView):
    form_class = ProcessForm
    model = Process
    template_name = 'crm/process_form_update.html'


class ProcessNoteCreate(CreateView):
    form_class = ProcessNoteForm
    model = ProcessNote


class SkillCreate(CreateView):
    form_class = SkillForm
    model = Skill


class SkillDetail(DetailView):
    model = Skill


class SkillList(ObjectListMixin, View):
    model = Skill
    template_name = 'crm/skill_list.html'

