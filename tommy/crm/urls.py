from django.conf.urls import url

from .views import company_detail, company_list, skill_detail, skill_list


urlpatterns = [
    url(r'^companies/$',
        company_list,
        name='crm_company_list'),
    url(r'^companies/(?P<slug>[\w\-]+)/$',
        company_detail,
        name='crm_company_detail'),
    url(r'^skills/$',
        skill_list,
        name='crm_skill_list'),
    url(r'^skills/(?P<slug>[\w\-]+)/$',
        skill_detail,
        name='crm_skill_detail'),
]