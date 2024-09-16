from django.urls import path
from .views import RicercaSearchview, StrutturaView, UtentiView
from . import views

app_name="searcher"
urlpatterns = [
    path('', RicercaSearchview.as_view(), name="home"),
    path('struttura/<int:struttura_id>', StrutturaView.as_view(), name="struttura"),
    path('struttura/<int:struttura_id>/<int:struttura_padre_id>', StrutturaView.as_view(), name="struttura"),
    path('utente/<int:id>', UtentiView.as_view(), name="utente"),
    #path('update/', views.update_informations, name="update_informations"),

]