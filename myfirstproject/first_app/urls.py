from django.conf.urls import url
from first_app import views

app_name='first_app'

urlpatterns=[

url(r'^$',views.help,name="index"),
url(r'^formpage/',views.form_page_view,name="form_page_view"),
url(r'^users/$',views.users,name="users"),
url(r'^base/$',views.base_template,name="base_template"),
url(r'^test/$',views.test_template,name="test_template")



]
