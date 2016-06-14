from django.contrib.auth import get_user
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Company, Contact, Process


class CompanyContextMixin:
    company_slug_url_kwarg = 'company_slug'
    company_context_object_name = 'company'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'company'):
            context = {self.company_context_object_name: self.company}
        else:
            company_slug = self.kwargs.get(self.company_slug_url_kwarg)
            company = get_object_or_404(Company, slug__iexact=company_slug)
            context = {
                self.company_context_object_name: company
            }
        context.update(kwargs)
        return super().get_context_data(**context)


class ContactGetObjectMixin:
    def get_object(self, queryset=None):
        company_slug = self.kwargs.get(self.company_slug_url_kwarg)
        contact_slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(
            Contact,
            slug__iexact=contact_slug,
            company__slug__iexact=company_slug)


class CompanyInitialMixin:
    def get_initial(self):
        company_slug = self.kwargs.get(self.company_slug_url_kwarg)
        self.company = get_object_or_404(Company, slug__iexact=company_slug)
        initial = {self.company_context_object_name: self.company}
        initial.update(self.initial)
        return initial


class ProcessContextMixin:
    process_slug_url_kwarg = 'process_slug'
    process_context_object_name = 'process'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'process'):
            context = {self.process_context_object_name: self.process}
        else:
            process_slug = self.kwargs.get(self.process_slug_url_kwarg)
            process = get_object_or_404(Process, slug__iexact=process_slug)
            context = {self.process_context_object_name: process}
        context.update(kwargs)
        return super().get_context_data(**context)


class ProcessInitialMixin:
    def get_initial(self):
        process_slug = self.kwargs.get(self.process_slug_url_kwarg)
        self.process = get_object_or_404(Process, slug__iexact=process_slug)
        initial = {self.process_context_object_name: self.process}
        initial.update(self.initial)
        return initial


class ProcessGetObjectMixin:
    def get_object(self, queryset=None):
        company_slug = self.kwargs.get(self.company_slug_url_kwarg)
        process_slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(
            Process,
            slug__iexact=process_slug,
            company__slug__iexact=company_slug)


class PageLinksMixin:
    page_kwarg = 'page'
    paginate_by = 20

    def _page_urls(self, page_number):
        return '?{pkw}={n}'.format(pkw=self.page_kwarg, n=page_number)

    def previous_page(self, page):
        if page.has_previous():
            return self._page_urls(page.previous_page_number())
        return None

    def next_page(self, page):
        if page.has_next():
            return self._page_urls(page.next_page_number())
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context.get('page_obj')
        if page is not None:
            context.update({
                'previous_page_url': self.previous_page(page),
                'next_page_url': self.next_page(page),
            })
        return context


class SlugCleanMixin:
    """
    Mixin class for slug cleaning method.
    """

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create' or new_slug == 'update':
            raise ValidationError('Slug may not be "{}".'.format(new_slug))
        return new_slug


class CreatedByMixin:
    """
    Mixin class to register the user that made a specific action.
    To be used in Forms.
    """
    def save(self, request, commit=True):
        obj = super().save(commit=False)
        if not obj.pk:
            current_user = get_user(request)
            obj.created_by = current_user
            if hasattr(obj.__class__, 'owner'):
                obj.owner = current_user
            if hasattr(obj.__class__, 'assigned_to'):
                obj.assigned_to = current_user
        if commit:
            obj.save()
            self.save_m2m()
        return obj


class CreatedByFormValidMixin:
    def form_valid(self, form):
        self.object = form.save(self.request)
        return HttpResponseRedirect(self.get_success_url())