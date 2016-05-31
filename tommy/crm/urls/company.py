from django.conf.urls import url


from ..views import (CompanyCreate, CompanyDelete, CompanyDetail, CompanyList,
                     CompanyUpdate, CompanyNoteCreate,
                     )

urlpatterns = [

    #################
    # COMPANY
    #################
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

    ##################
    # COMPANY ACTION
    ##################
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'add-action/$',
        CompanyNoteCreate.as_view(),
        name='crm_company_note_create'
    ),

    #################
    # JOB
    #################


]