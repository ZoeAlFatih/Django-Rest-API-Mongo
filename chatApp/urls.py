from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from restApp import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', views.SnippetViewSet)

schema_view = get_schema_view(title='Chat App Rest API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^stocks/$', views.StockList.as_view()),
    url(r'^stock/(?P<pk>[0-9]+)/$', views.StockDetailView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^qw/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # USE API_VIEW & USE CRSF_EXEMPT
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    # url(r'^snippets/$', views.SnippetList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^province/$', views.province.as_view()),
    url(r'^city/$', views.city.as_view()),
    url(r'^docs/$', schema_view),

    
]

