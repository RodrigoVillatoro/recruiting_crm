from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, MultiField, Layout, Submit
from crispy_forms.bootstrap import TabHolder, Tab

from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
from .utils import SlugCleanMixin


class CompanyForm(SlugCleanMixin, forms.ModelForm):
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
                'nubelo_id',
                'nubelo_url',
                'status',
            ),
            Fieldset(
                'Other Info',
                'legal_name',
                'cif',
                'fee',
                'is_canonical_company'
            ),
        )

    class Meta:
        model = Company
        fields = '__all__'


class CompanyNoteForm(forms.ModelForm):
    class Meta:
        model = CompanyNote
        fields = '__all__'


class ContactForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProcessForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessNoteForm(forms.ModelForm):
    class Meta:
        model = ProcessNote
        fields = '__all__'


class SkillForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'