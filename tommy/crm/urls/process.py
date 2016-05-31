from django.conf.urls import url

from ..views import ProcessCreateGeneral, ProcessList


urlpatterns = [
    url(
        r'^$',
        ProcessList.as_view(),
        name='crm_process_list'
    ),
    url(
        r'process/create/$',
        ProcessCreateGeneral.as_view(),
        name='crm_process_create_general'
    ),
]
