from django.conf.urls import url


from ..views import (CompanyCreate, CompanyDelete, CompanyDetail, CompanyList,
                     CompanyUpdate, CompanyNoteCreate,
                     ProcessCreate, ProcessDelete, ProcessDetail,
                     ProcessUpdate, ProcessNoteCreate)

urlpatterns = [

    ###############
    # COMPANY
    ###############
    url(
        r'^$',
        CompanyList.as_view(),
        name='crm_company_list'
    ),
    url(
        r'^create/$',
        CompanyCreate.as_view(),
        name='crm_company_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        CompanyDetail.as_view(),
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

    ###############
    # JOB
    ###############
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'process/'
        r'create/$',
        ProcessCreate.as_view(),
        name='crm_process_create'
    ),
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'(?P<process_slug>[\w\-]+)/$',
        ProcessDetail.as_view(),
        name='crm_process_detail'
    ),
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'(?P<process_slug>[\w\-]+)/'
        r'delete/$',
        ProcessDelete.as_view(),
        name='crm_process_delete'
    ),
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'(?P<process_slug>[\w\-]+)/'
        r'update/$',
        ProcessUpdate.as_view(),
        name='crm_process_update'
    ),
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'(?P<process_slug>[\w\-]+)/'
        r'action/'
        r'create/$',
        ProcessNoteCreate.as_view(),
        name='crm_process_note_create'
    ),
]