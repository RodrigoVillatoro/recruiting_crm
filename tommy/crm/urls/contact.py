from django.conf.urls import url


from ..views import (ContactCreate, ContactDelete, ContactDetail, ContactList,
                     ContactModal, ContactUpdate)


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
        r'^modal/(?P<slug>[\w\-]+)/$',
        ContactModal.as_view(),
        name='crm_contact_modal'
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
        r'^(?P<slug>[\w\-]+)/update/$',
        ContactUpdate.as_view(),
        name='crm_contact_update'
    ),
]