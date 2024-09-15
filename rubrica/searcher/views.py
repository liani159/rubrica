from django.shortcuts import render
from haystack.generic_views import SearchView, SearchQuerySet
from .models import Utenti, Struttura
from django.views.generic import ListView
from haystack.query import SQ

# Create your views here.
class RicercaSearchview(SearchView):
    template_name= 'search/page.html'

    def get_queryset(self):
        #queryset = super().get_queryset()
        queryset = SearchQuerySet()
        dato_input = self.request.GET.get("q")
        checkbox = self.request.GET.get("check")
        print(f"{dato_input}  {checkbox}")
        
        if checkbox=="searcher.utenti":
            print("utenti")
            #ricerca sia su nome che suu cognome
            result = queryset.models(Utenti).filter(SQ(nome=dato_input) | SQ(cognome=dato_input))
            #result = queryset.models(Utenti).filter(SQ(nome=dato_input) | SQ(cognome=dato_input))
        else:
            print("Struttura")
            result = queryset.models(Struttura).filter(nome_struttura=dato_input)
        #dr = SearchQuerySet().filter(content=dato)
        #if dato :
        #    qst = queryset.filter(nome=dato)
        #else:
        #    qst = queryset.none()
        #result = SearchQuerySet().filter(content='liani')
        
        return result

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['dato'] = self.request.GET.get("check")
        result = self.get_queryset()
        context['total_result'] = result.count()
        # do something
        return context
    


class StrutturaView(ListView):
    template_name= 'search/struttura.html'

    def get_queryset(self):
        queryset = SearchQuerySet()
        #queryset = super().get_queryset()
        struttura_id = self.kwargs["struttura_id"]
        print(f"{struttura_id}: verifica")

        result_struttura = queryset.models(Utenti).filter(struttura_id=struttura_id)
        #print(result_struttura)
            
        #return queryset
        return result_struttura
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        struttura_id = self.kwargs.get("struttura_id", None)
        struttura_padre_id = self.kwargs.get("struttura_padre_id", None)
        
        #if self.kwargs["struttura_padre_id"]:
        print(f"just a test:{struttura_padre_id}")
        queryset = SearchQuerySet()
        #padre = queryset.models(Struttura).filter(nome_struttura__exact=struttura_name)
        #===========>new code
        padre = Struttura.objects.get(id=struttura_id)
        #queryset = SearchQuerySet()
        if struttura_padre_id:
            #struttura_padre = self.kwargs["struttura_padre"]
            res_padre = padre.struttura_padre
            print(f"rrrr: {res_padre} {struttura_id}")
            #se ottengo il nome della struttura padre significa che non è
            # la struttura root quindi proseguo con le query
            if res_padre:
                #elenco tutti suoi figli(strutture figli)
                strutture_figli = Struttura.objects.filter(struttura_padre=res_padre)
                numero_figli = strutture_figli.count()
                #prendo tutti gli utenti della struttura padre
                id_res_padre = Struttura.objects.filter(nome_struttura=res_padre)

#============================= today =================
                print(f"ttt: {id_res_padre[0].id}")
#============================= today =================

                result = Utenti.objects.filter(struttura_id=id_res_padre[0].id)
                numero_utenti = result.count()

                context['result'] = result
                context['struttura_id'] = id_res_padre[0].id
                context['sotto_strutture'] = strutture_figli
                context['struttura_padre'] = res_padre
                context['numero_utenti'] = numero_figli
                context['numero_figli'] = numero_utenti

                return context
        #else:
        print("elsee")
        result = Utenti.objects.filter(struttura_id=struttura_id)
        name = Struttura.objects.filter(id=struttura_id)
        print(f"result else:{result[0]}")
        print(f"result else:{name[0]}")
        numero_utenti = result.count()
        context['result'] = result
        context['name'] = name[0]
        context['struttura_id'] = struttura_id
        context['numero_utenti'] = numero_utenti

        return context



class UtentiView(ListView):
    template_name= 'search/utenti.html'

    def get_queryset(self):
        queryset = SearchQuerySet()
        #queryset = super().get_queryset()
        id = self.kwargs["id"]
        #cognome = self.kwargs["cognome"]
        print(f"{id}: verifica")

        #result = queryset.models(Utenti).filter(SQ(nome__exact=nome) & SQ(cognome__exact=cognome))
        result = Utenti.objects.filter(id=id)
            
        return result
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # do something
        return context