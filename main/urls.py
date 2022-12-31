from django.contrib import admin
from django.urls import path
from blog.views import frontpage
from blog.views import testpage


# / が必要
urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", testpage),
    path("", frontpage)
]
