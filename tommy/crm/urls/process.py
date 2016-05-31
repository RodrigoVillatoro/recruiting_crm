from django.conf.urls import url

from ..views import ProcessCreateGeneral, ProcessList, ProcessNoteCreate


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
        r'^note/create/$',
        ProcessNoteCreate.as_view(),
        name='crm_process_note_create'
    ),
]
