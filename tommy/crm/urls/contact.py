from django.conf.urls import url


from ..views import (ContactCreate, ContactDelete, ContactDetail, ContactList,
                     ContactUpdate)


urlpatterns = [
    url(
        r'^$',
        ContactList.as_view(),
        name='crm_contact_list'
    ),
    url(
        r'^create/$',
        ContactCreate.as_view(),
        name='crm_contact_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        ContactDetail.as_view(),
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