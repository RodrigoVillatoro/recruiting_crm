from django import forms

from .models import Company, CompanyNote, Contact, Process, ProcessNote, Skill
from .utils import SlugCleanMixin


class CompanyForm(SlugCleanMixin, forms.ModelForm):
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