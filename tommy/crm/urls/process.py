from django.conf.urls import url

from ..views import (ProcessCreate, ProcessDelete, ProcessDetail, ProcessList,
                     ProcessUpdate, ProcessNoteCreate)


urlpatterns = [
    url(
        r'^$',
        ProcessList.as_view(),
        name='crm_process_list'
    ),
    url(
        r'^create/$',
        ProcessCreate.as_view(),
        name='crm_process_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        ProcessDetail.as_view(),
        name='crm_process_detail'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/delete/$',
        ProcessDelete.as_view(),
        name='crm_process_delete'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/update/$',
        ProcessUpdate.as_view(),
        name='crm_process_update'
    ),
    url(
        r'^note/create/$',
        ProcessNoteCreate.as_view(),
        name='crm_process_note_create'
    ),
]