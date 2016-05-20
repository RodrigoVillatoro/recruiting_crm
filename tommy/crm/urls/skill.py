from django.conf.urls import url

from ..views import SkillCreate, skill_detail, skill_list


urlpatterns = [
    url(
        r'^$',
        skill_list,
        name='crm_skill_list'
    ),
    url(
        r'^create/$',
        SkillCreate.as_view(),
        name='crm_skill_create'
    ),
    url(
        r'^(?P<slug>[\w\-]+)/$',
        skill_detail,
        name='crm_skill_detail'
    ),
]