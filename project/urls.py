from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$', 'main.views.home'),
	url(r'^signup/$', 'main.views.signup'),
    url(r'^login/$', 'main.views.login_view'),
    url(r'^logout/$', 'main.views.logout_view'),
    url(r'^tender/(?P<pk>\d+)/$', 'main.views.tender_detail'),
    url(r'^logout/$', 'main.views.logout_view'),
    url(r'^tenders/$', 'main.views.tender_list'),
    url(r'^quotations/$', 'main.views.quotation_list'),
    url(r'^quotation/(?P<pk>\d+)/$', 'main.views.quotation'),
    url(r'^tender_create/$', 'main.views.tender_create'),
    url(r'^quote_create/$', 'main.views.quote_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
