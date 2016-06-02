from django.core.exceptions import ValidationError
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


class FetchCompanyMixin:
    def get_initial(self):
        company_slug = self.kwargs.get(self.company_slug_url_kwarg)
        self.company = get_object_or_404(Company, slug__iexact=company_slug)
        initial = {self.company_context_object_name: self.company}
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