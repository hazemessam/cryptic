from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='files.html', extra_context={'active': 'files'})),
    path('history/', TemplateView.as_view(template_name='history.html', extra_context={'active': 'history'})),
    path('upload/', include('files.urls'))
]
