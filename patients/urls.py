from django.urls import path
from .views import (home_page, Patient_detail, Patient_create, Patient_delete,Patient_update,
                    create_record,view_record, Delete_record,Record_update)

app_name='patients'

urlpatterns = [
    path('',home_page,name='home'),
    path('<int:pk>',Patient_detail,name='patient-detail'),
    path('<int:pk>/update/',Patient_update.as_view(),name='patient-update'),
    path('<int:pk>/delete/',Patient_delete.as_view(),name='patient-delete'),
    path('<int:pk>/record-detail/',view_record,name='record-detail'),
    path('<int:pk>/record-create/',create_record,name='record-create'),
    path('<int:pk>/record-update/',Record_update.as_view(),name='record-update'),
    path('<int:pk>/record-delete/',Delete_record.as_view(),name='record-delete'),
    path('create/',Patient_create.as_view(),name='patient-create'),

]