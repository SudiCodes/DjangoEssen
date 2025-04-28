"""
URL configuration for django_essen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.urls.conf import include
from django_tus.views import TusUpload
from chunked_upload.views import (
    ChunkedUploadView, ChunkedUploadCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path("products/",include("fileupload.urls")),
    path('tus-upload/', TusUpload.as_view(), name='tus_upload'),
    path('tus-upload/<uuid:resource_id>', TusUpload.as_view(), name='tus_upload_chunks'),
    path('chunked-upload/', ChunkedUploadView.as_view(), name='chunked-upload'),
    path('chunked-upload-complete/', ChunkedUploadCompleteView.as_view(), name='chunked-upload-complete')
]
