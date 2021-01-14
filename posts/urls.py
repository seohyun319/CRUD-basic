from django.urls import path
from . import views
app_name='posts'

urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('<int:post_id>/', view=vies.post_detail, name='detail'),
]