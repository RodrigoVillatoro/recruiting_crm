from django import forms
from django.forms.widgets import HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, MultiField, Layout, Submit
from crispy_forms.bootstrap import TabHolder, Tab

from .models import Company, CompanyAction, Contact, Job, JobAction, Skill
from .utils import CreatedByMixin, SlugCleanMixin


class CompanyForm(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'
        self.helper.layout = Layout(
            Fieldset(
                'General Info',
                'name',
                'industry',
                'skills',
                'status',
                'slug',
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
        exclude = ('created_by', 'assigned_to', 'owner')


class CompanyActionForm(CreatedByMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyActionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = CompanyAction
        exclude = ('created_by', )
        widgets = {'company': HiddenInput()}


class ContactForm(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = Contact
        exclude = ('created_by',)
        widgets = {'company': HiddenInput()}


class ContactFormGeneral(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_by',)


class JobForm(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = Job
        exclude = ('created_by',)
        widgets = {'company': HiddenInput()}


class JobFormGeneral(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('created_by',)


class JobActionForm(CreatedByMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobActionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = JobAction
        exclude = ('created_by',)
        widgets = {'job': HiddenInput()}


class SkillForm(SlugCleanMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = Skill
        fields = '__all__'
