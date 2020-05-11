
"""BookingRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from MainApp import urls as mainappurls, views as mainappviews
from django.urls import path
from AuthApp import urls as authappurls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mainappurls), name='info'),
    path('', include(authappurls), name='auth'),
    
    path('error.html/', mainappviews.error, name='error'),
    path('booking/<int:pk>/', mainappviews.BookingDetails.as_view(), name='booking'),
    path('update/', mainappviews.UpdatedRoom.as_view(), name='updated_room_page'),
    path('delete/<int:pk>/', mainappviews.DeleteBook.as_view(), name='delete')
    ]\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""BookingRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from MainApp import urls as mainappurls, views as mainappviews
from django.urls import path
from AuthApp import urls as authappurls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mainappurls), name='info'),
    path('', include(authappurls), name='auth'),
    
    path('error.html/', mainappviews.error, name='error'),
    path('booking/<int:pk>/', mainappviews.BookingDetails.as_view(), name='booking'),
    path('update/', mainappviews.UpdatedRoom.as_view(), name='updated_room_page'),
    path('delete/<int:pk>/', mainappviews.DeleteBook.as_view(), name='delete')
    ]\
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

