from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from user.decorators import class_login_required
from .forms import (CompanyForm, CompanyNoteForm, ContactForm,
                    ContactFormGeneral, ProcessForm, ProcessFormGeneral,
                    ProcessNoteForm, SkillForm)
from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
from .utils import (CompanyContextMixin, CompanyInitialMixin,
                    ContactGetObjectMixin, CreatedByFormValidMixin,
                    ProcessContextMixin, ProcessInitialMixin,
                    ProcessGetObjectMixin, PageLinksMixin)


@class_login_required
class CompanyCreate(CreatedByFormValidMixin, CreateView):
    form_class = CompanyForm
    model = Company


@class_login_required
class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('crm_company_list')


@class_login_required
class CompanyDetail(DetailView):
    model = Company


@class_login_required
class CompanyList(PageLinksMixin, ListView):
    model = Company


@class_login_required
class CompanyUpdate(CreatedByFormValidMixin, UpdateView):
    form_class = CompanyForm
    model = Company
    template_name = 'crm/company_form_update.html'


@class_login_required
class CompanyNoteCreate(CreatedByFormValidMixin, CompanyContextMixin,
                        CompanyInitialMixin, CreateView):
    form_class = CompanyNoteForm
    model = CompanyNote
    template_name = 'crm/company_note_form.html'


@class_login_required
class ContactCreate(CreatedByFormValidMixin, CompanyContextMixin,
                    CompanyInitialMixin, CreateView):
    form_class = ContactForm
    model = Contact


@class_login_required
class ContactCreateGeneral(CreatedByFormValidMixin, CreateView):
    form_class = ContactFormGeneral
    model = Contact


@class_login_required
class ContactDelete(CompanyContextMixin, ContactGetObjectMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('crm_contact_list')
    slug_url_kwarg = 'contact_slug'


@class_login_required
class ContactDetail(CompanyContextMixin, ContactGetObjectMixin, DetailView):
    model = Contact
    slug_url_kwarg = 'contact_slug'


@class_login_required
class ContactList(PageLinksMixin, ListView):
    model = Contact


@class_login_required
class ContactUpdate(CreatedByFormValidMixin, CompanyContextMixin,
                    ContactGetObjectMixin, UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = 'crm/contact_form_update.html'
    slug_url_kwarg = 'contact_slug'


@class_login_required
class ProcessCreate(CreatedByFormValidMixin, CompanyContextMixin,
                    CompanyInitialMixin, CreateView):
    form_class = ProcessForm
    model = Process


@class_login_required
class ProcessCreateGeneral(CreatedByFormValidMixin, CreateView):
    form_class = ProcessFormGeneral
    model = Process


@class_login_required
class ProcessDelete(CompanyContextMixin, ProcessGetObjectMixin, DeleteView):
    model = Process
    success_url = reverse_lazy('crm_process_list')
    slug_url_kwarg = 'process_slug'


@class_login_required
class ProcessDetail(CompanyContextMixin, ProcessGetObjectMixin, DetailView):
    model = Process
    slug_url_kwarg = 'process_slug'


@class_login_required
class ProcessList(PageLinksMixin, ListView):
    model = Process


@class_login_required
class ProcessUpdate(CreatedByFormValidMixin, CompanyContextMixin,
                    ProcessGetObjectMixin, UpdateView):
    form_class = ProcessForm
    model = Process
    template_name = 'crm/process_form_update.html'
    slug_url_kwarg = 'process_slug'


@class_login_required
class ProcessNoteCreate(CreatedByFormValidMixin, ProcessContextMixin,
                        ProcessInitialMixin, CreateView):
    form_class = ProcessNoteForm
    model = ProcessNote
    template_name = 'crm/process_note_form.html'


@class_login_required
class SkillCreate(CreateView):
    form_class = SkillForm
    model = Skill


@class_login_required
class SkillDetail(DetailView):
    model = Skill


@class_login_required
class SkillList(PageLinksMixin, ListView):
    model = Skill

