from django.conf.urls import url

from .views import (CompanyCreate, CompanyNoteCreate, ContactCreate,
                    ProcessCreate, ProcessNoteCreate, SkillCreate,
                    company_detail, company_list, contact_detail, contact_list,
                    process_detail, process_list, skill_detail, skill_list)


urlpatterns = [
    url(
        r'^company/$',
        company_list,
        name='crm_company_list'
    ),
    url(
        r'^company/create/$',
        CompanyCreate.as_view(),
        name='crm_company_create'
    ),
    url(
        r'^company/(?P<slug>[\w\-]+)/$',
        company_detail,
        name='crm_company_detail'
    ),
    url(
        r'^company/note/create/$',
        CompanyNoteCreate.as_view(),
        name='crm_company_note_create'
    ),
    url(
        r'^contact/$',
        contact_list,
        name='crm_contact_list'
    ),
    url(
        r'^contact/create/$',
        ContactCreate.as_view(),
        name='crm_contact_create'
    ),
    url(
        r'^contact/(?P<slug>[\w\-]+)/$',
        contact_detail,
        name='crm_contact_detail'
    ),
    url(
        r'^process/$',
        process_list,
        name='crm_process_list'
    ),
    url(
        r'^process/create/$',
        ProcessCreate.as_view(),
        name='crm_process_create'
    ),
    url(
        r'^process/(?P<slug>[\w\-]+)/$',
        process_detail,
        name='crm_process_detail'
    ),
    url(
        r'^process/note/create/$',
        ProcessNoteCreate.as_view(),
        name='crm_process_note_create'
    ),
    url(
        r'^skill/$',
        skill_list,
        name='crm_skill_list'
    ),
    url(
        r'^skill/create/$',
        SkillCreate.as_view(),
        name='crm_skill_create'
    ),
    url(
        r'^skill/(?P<slug>[\w\-]+)/$',
        skill_detail,
        name='crm_skill_detail'
    ),
]