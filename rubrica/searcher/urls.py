from django.urls import path
from .views import RicercaSearchview, StrutturaView, UtentiView

app_name="searcher"
urlpatterns = [
    path('', RicercaSearchview.as_view(), name="home"),
    path('struttura/<str:struttura_name>', StrutturaView.as_view(), name="struttura"),
    path('struttura/<str:struttura_name>/<str:struttura_padre>', StrutturaView.as_view(), name="struttura"),
    path('utente/<str:nome>/<str:cognome>', UtentiView.as_view(), name="utente"),

]