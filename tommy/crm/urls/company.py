from django.conf.urls import url


from ..views import (CompanyCreate, CompanyDelete, CompanyUpdate,
                     CompanyNoteCreate, company_detail, company_list)

urlpatterns = [
    url(
        r'^$',
        company_list,
        name='crm_company_list'
    ),
    url(
        r'^create/$',
        CompanyCreate.as_view(),
        name='crm_company_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        company_detail,
        name='crm_company_detail'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/delete/$',
        CompanyDelete.as_view(),
        name='crm_company_delete'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/update/$',
        CompanyUpdate.as_view(),
        name='crm_company_update'
    ),
    url(
        r'^note/create/$',
        CompanyNoteCreate.as_view(),
        name='crm_company_note_create'
    ),
]