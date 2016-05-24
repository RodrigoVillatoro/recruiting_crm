from django.core.exceptions import ValidationError
from django.shortcuts import render


class ObjectListMixin:
    model = None
    template_name = ''

    def get(self, request):
        objects = self.model.objects.all()
        context_name = '{}_list'.format(self.model.__name__.lower())
        context = {context_name: objects}
        return render(request, self.template_name, context)


class SlugCleanMixin:
    """
        Mixin class for slug cleaning method.
    """

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug