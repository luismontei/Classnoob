from django.urls import path, include
from . import views
from .views import Link_Create, Link_Update,Link_Delete,Link_List,Views_Form, Coments_List,Comentario_Delete


urlpatterns = [
    path('',views.home, name="home"),
    path('create/', Link_Create.as_view(), name="Link_Create"),
    path('aparecer/<int:id>', views.Link_Views, name="Link_Views"),
    path('criarcometario/', Views_Form.as_view(), name="Views_Form"),
    path('update/<int:pk>/', Link_Update.as_view(), name="Link_Update"),
    path('delete/<int:pk>/', Link_Delete.as_view(), name="Link_Delete"),
    path('deleteduvidas/<int:pk>/', Comentario_Delete.as_view(), name="deleteduvidas"),
    path('list/', Link_List.as_view(), name="Link_List"),
    path('listduvidas/', Coments_List.as_view(), name="Coments_List"),
    path('listduvidas/detalhes/<int:id>/', views.Detalhe_comentario, name="Detalhe_comentario")
]