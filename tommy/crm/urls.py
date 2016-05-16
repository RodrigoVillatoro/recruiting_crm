from django.conf.urls import url

from .views import (company_detail, company_list, contact_detail, contact_list,
                    process_detail, process_list, skill_detail, skill_list)


urlpatterns = [
    url(r'^company/$',
        company_list,
        name='crm_company_list'),
    url(r'^company/(?P<slug>[\w\-]+)/$',
        company_detail,
        name='crm_company_detail'),
    url(r'^contact/$',
        contact_list,
        name='crm_contact_list'),
    url(r'^contact/(?P<slug>[\w\-]+)/$',
        contact_detail,
        name='crm_contact_detail'),
    url(r'^skill/$',
        skill_list,
        name='crm_skill_list'),
    url(r'^skill/(?P<slug>[\w\-]+)/$',
        skill_detail,
        name='crm_skill_detail'),
    url(r'^process/$',
        process_list,
        name='crm_process_list'),
    url(r'^process/(?P<slug>[\w\-]+)/$',
        process_detail,
        name='crm_process_detail'),
]