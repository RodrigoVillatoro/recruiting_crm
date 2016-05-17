from django import forms
from django.core.exceptions import ValidationError

from .models import Company, CompanyNote, Process, ProcessNote, Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyNoteForm(forms.ModelForm):
    class Meta:
        model = CompanyNote
        fields = '__all__'


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessNoteForm(forms.ModelForm):
    class Meta:
        model = ProcessNote
        fields = '__all__'
