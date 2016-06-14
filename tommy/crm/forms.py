from django import forms
from django.forms.widgets import HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, MultiField, Layout, Submit
from crispy_forms.bootstrap import TabHolder, Tab

from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
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
                'country',
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
                'is_canonical_company',
            ),
        )

    class Meta:
        model = Company
        exclude = ('created_by', 'assigned_to', 'owner')


class CompanyNoteForm(CreatedByMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyNoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = CompanyNote
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


class ProcessForm(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = Process
        exclude = ('created_by',)
        widgets = {'company': HiddenInput()}


class ProcessFormGeneral(CreatedByMixin, SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Process
        exclude = ('created_by',)


class ProcessNoteForm(CreatedByMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProcessNoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-7'

    class Meta:
        model = ProcessNote
        exclude = ('created_by',)
        widgets = {'process': HiddenInput()}


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
