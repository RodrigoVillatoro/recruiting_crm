from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from user.decorators import class_login_required
from .forms import (CompanyForm, CompanyActionForm, ContactForm,
                    ContactFormGeneral, JobForm, JobFormGeneral,
                    JobActionForm, SkillForm)
from .models import Company, CompanyAction, Contact, Job, JobAction, Skill
from .utils import (CompanyContextMixin, CompanyInitialMixin,
                    ContactGetObjectMixin, CreatedByFormValidMixin,
                    JobContextMixin, JobInitialMixin,
                    JobGetObjectMixin, PageLinksMixin)


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
class CompanyActionCreate(CreatedByFormValidMixin, CompanyContextMixin,
                          CompanyInitialMixin, CreateView):
    form_class = CompanyActionForm
    model = CompanyAction
    template_name = 'crm/company_action_form.html'


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
class JobCreate(CreatedByFormValidMixin, CompanyContextMixin,
                CompanyInitialMixin, CreateView):
    form_class = JobForm
    model = Job


@class_login_required
class JobCreateGeneral(CreatedByFormValidMixin, CreateView):
    form_class = JobFormGeneral
    model = Job


@class_login_required
class JobDelete(CompanyContextMixin, JobGetObjectMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('crm_job_list')
    slug_url_kwarg = 'job_slug'


@class_login_required
class JobDetail(CompanyContextMixin, JobGetObjectMixin, DetailView):
    model = Job
    slug_url_kwarg = 'job_slug'


@class_login_required
class JobList(PageLinksMixin, ListView):
    model = Job


@class_login_required
class JobUpdate(CreatedByFormValidMixin, CompanyContextMixin,
                JobGetObjectMixin, UpdateView):
    form_class = JobForm
    model = Job
    template_name = 'crm/job_form_update.html'
    slug_url_kwarg = 'job_slug'


@class_login_required
class JobActionCreate(CreatedByFormValidMixin, JobContextMixin,
                      JobInitialMixin, CreateView):
    form_class = JobActionForm
    model = JobAction
    template_name = 'crm/job_action_form.html'


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

