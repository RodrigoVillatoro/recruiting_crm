from django.conf.urls import url

from ..views import (ProcessCreate, ProcessCreateGeneral, ProcessDelete,
                     ProcessDetail, ProcessList, ProcessNoteCreate,
                     ProcessUpdate)


urlpatterns = [
    url(
        r'^$',
        ProcessList.as_view(),
        name='crm_process_list'
    ),
    url(
        r'^create/$',
        ProcessCreateGeneral.as_view(),
        name='crm_process_create_general'
    ),
    url(
        r'^(?P<company_slug>[\w\-]+)/'
        r'add-job/$',
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
        r'add-action/$',
        ProcessNoteCreate.as_view(),
        name='crm_process_note_create'
    ),

]
