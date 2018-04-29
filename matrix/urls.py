from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from main.views import index_view, matrix_view
from matrix import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index_view'),
    url(r'^matrix/$', matrix_view, name='matrix_view')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
