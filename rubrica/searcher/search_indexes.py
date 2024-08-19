import datetime
from haystack import indexes
from .models import Utenti, Struttura

class UtentiIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    #text = indexes.CharField(document=True, use_template=True)
    nome = indexes.NgramField(model_attr='nome')
    cognome = indexes.NgramField(model_attr='cognome')
    struttura = indexes.NgramField(model_attr='struttura')
    #cod = indexes.CharField(model_attr='cod')
    

    def get_model(self):
        return Utenti

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    

class StrutturaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    nome_struttura = indexes.NgramField(model_attr='nome_struttura')
    struttura_padre = indexes.NgramField(model_attr='struttura_padre')
    

    def get_model(self):
        return Struttura

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()