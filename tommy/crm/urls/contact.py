from django.conf.urls import url


from ..views import (ContactCreate, ContactDelete, ContactUpdate,
                     contact_detail, contact_list)


urlpatterns = [
    url(
        r'^$',
        contact_list,
        name='crm_contact_list'
    ),
    url(
        r'^create/$',
        ContactCreate.as_view(),
        name='crm_contact_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        contact_detail,
        name='crm_contact_detail'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/delete/$',
        ContactDelete.as_view(),
        name='crm_contact_delete'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/upgrade/$',
        ContactUpdate.as_view(),
        name='crm_contact_update'
    ),
]