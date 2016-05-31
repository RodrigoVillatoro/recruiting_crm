from django.core.exceptions import ValidationError


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