from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from .forms import (CompanyForm, CompanyNoteForm, ContactForm, ProcessForm,
                    ProcessNoteForm, SkillForm)
from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
from .utils import (CompanyContextMixin, ContactGetObjectMixin, PageLinksMixin,
                    ProcessGetObjectMixin)


class CompanyCreate(CreateView):
    form_class = CompanyForm
    model = Company


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('crm_company_list')


class CompanyDetail(DetailView):
    model = Company


class CompanyList(PageLinksMixin, ListView):
    model = Company


class CompanyUpdate(UpdateView):
    form_class = CompanyForm
    model = Company
    template_name = 'crm/company_form_update.html'


class CompanyNoteCreate(CompanyContextMixin, CreateView):
    form_class = CompanyNoteForm
    model = CompanyNote
    template_name = 'crm/company_note_form.html'


class ContactCreate(CompanyContextMixin, CreateView):
    form_class = ContactForm
    model = Contact


class ContactCreateGeneral(CreateView):
    form_class = ContactForm
    model = Contact


class ContactDelete(CompanyContextMixin, ContactGetObjectMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('crm_contact_list')
    slug_url_kwarg = 'contact_slug'


class ContactDetail(CompanyContextMixin, ContactGetObjectMixin, DetailView):
    model = Contact
    slug_url_kwarg = 'contact_slug'


class ContactList(PageLinksMixin, ListView):
    model = Contact


class ContactUpdate(CompanyContextMixin, ContactGetObjectMixin, UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = 'crm/contact_form_update.html'
    slug_url_kwarg = 'contact_slug'


class ProcessCreate(CompanyContextMixin, CreateView):
    form_class = ProcessForm
    model = Process


class ProcessCreateGeneral(CreateView):
    form_class = ProcessForm
    model = Process


class ProcessDelete(CompanyContextMixin, ProcessGetObjectMixin, DeleteView):
    model = Process
    success_url = reverse_lazy('crm_process_list')
    slug_url_kwarg = 'process_slug'


class ProcessDetail(CompanyContextMixin, ProcessGetObjectMixin, DetailView):
    model = Process
    slug_url_kwarg = 'process_slug'


class ProcessList(PageLinksMixin, ListView):
    model = Process


class ProcessUpdate(CompanyContextMixin, ProcessGetObjectMixin, UpdateView):
    form_class = ProcessForm
    model = Process
    template_name = 'crm/process_form_update.html'
    slug_url_kwarg = 'process_slug'


class ProcessNoteCreate(CreateView):
    form_class = ProcessNoteForm
    model = ProcessNote
    template_name = 'crm/process_note_form.html'


class SkillCreate(CreateView):
    form_class = SkillForm
    model = Skill


class SkillDetail(DetailView):
    model = Skill


class SkillList(PageLinksMixin, ListView):
    model = Skill

