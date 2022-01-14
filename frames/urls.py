from django.urls import path,include
#from django.conf import settings
#from django.conf.urls.static import static
from . import views

urlpatterns = [
#path("",views.optical_form,name='find'),
path('',views.InsertData,name='InsertData'),

]
'''if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)'''
