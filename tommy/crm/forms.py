from django import forms
from django.forms.widgets import HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout

from .models import Company, CompanyAction, Contact, Job, JobAction, Skill
from .utils import CreatedByMixin, CrispyMixin, SlugCleanMixin


class CompanyForm(CreatedByMixin, CrispyMixin, SlugCleanMixin,
                  forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Fieldset(
                'General Info',
                'name',
                'industry',
                'skills',
                'status',
                'slug',
                'owner',
                'assigned_to',
            ),
            Fieldset(
                'Location',
                'city',
                'address',
                'zip_code',
            ),
            Fieldset(
                'Company Details',
                'website',
                'description',

            ),
            Fieldset(
                'Other Info',
                'legal_name',
                'cif',
                'fee',
            ),
            Fieldset(
                'Nubelo',
                'nubelo_id',
                'nubelo_url',
                'official_company',
            ),
        )

    class Meta:
        model = Company
        exclude = ('created_by',)


class CompanyActionForm(CreatedByMixin, CrispyMixin, forms.ModelForm):
    class Meta:
        model = CompanyAction
        exclude = ('created_by', )
        widgets = {'company': HiddenInput()}


class ContactForm(
    CreatedByMixin, CrispyMixin, SlugCleanMixin, forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('created_by',)
        widgets = {'company': HiddenInput()}


class ContactFormGeneral(
    CreatedByMixin, CrispyMixin, SlugCleanMixin, forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('created_by',)


class JobForm(
    CreatedByMixin, CrispyMixin, SlugCleanMixin, forms.ModelForm):

    class Meta:
        model = Job
        exclude = ('created_by',)
        widgets = {'company': HiddenInput()}


class JobFormGeneral(
    CreatedByMixin, CrispyMixin, SlugCleanMixin, forms.ModelForm):

    class Meta:
        model = Job
        exclude = ('created_by',)


class JobActionForm(CreatedByMixin, CrispyMixin, forms.ModelForm):

    class Meta:
        model = JobAction
        exclude = ('created_by',)
        widgets = {'job': HiddenInput()}


class SkillForm(SlugCleanMixin, CrispyMixin, forms.ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'
