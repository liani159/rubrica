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
        context['tatal_result'] = result.count()
        # do something
        return context
    


class StrutturaView(ListView):
    template_name= 'search/struttura.html'

    def get_queryset(self):
        queryset = SearchQuerySet()
        #queryset = super().get_queryset()
        struttura_name = self.kwargs["struttura_name"]
        print(f"{struttura_name}: verifica")

        result_struttura = queryset.models(Utenti).filter(struttura__exact=struttura_name)
        #print(result_struttura)
            
        #return queryset
        return result_struttura
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        struttura_name = self.kwargs.get("struttura_name", None)
        struttura_padre = self.kwargs.get("struttura_padre", None)
        
        #if self.kwargs["struttura_padre"]:
        print(f"just a test:{struttura_padre}")
        queryset = SearchQuerySet()
        padre = queryset.models(Struttura).filter(nome_struttura__exact=struttura_name)
        
        #queryset = SearchQuerySet()
        if struttura_padre:
            #struttura_padre = self.kwargs["struttura_padre"]
            for p in padre:
                    res_padre = p.object.struttura_padre
            print(f"dddd: {res_padre}")

            #context['struttura_padre'] = test_padre
            #print(test_padre)
            #print(f"hi padre")
            #print(test_padre)
            
            
            #ottengo il nome della struttura padre
            #padre = queryset.models(Struttura).filter(nome_struttura__exact=test_padre)
            #utenti_padre = queryset.models(Utenti).filter(struttura__exact=test_padre)
                #print(p.object.struttura_padre)
            #print(utenti_padre)
            """ for p in padre:
                    padrone = p.object.struttura_padre """
            #print(f"padrone: {padrone}")
            if res_padre:
                #for p in padre:
                #context['padre'] = padrone
                #print(padre)
                strutture_figli = queryset.models(Struttura).filter(struttura_padre__exact=res_padre)
                result = queryset.models(Utenti).filter(struttura__exact=res_padre)
                
                context['result'] = result
                context['name'] = res_padre
                context['sotto_strutture'] = strutture_figli
                context['struttura_padre'] = res_padre
                context['numero_utenti'] = result.count()
                context['numero_figli'] = strutture_figli.count()

                return context
                #print(f"hi {padre.count()}")
                #print(f"struttura_padre: {padrone}")
                #print(f"ddd:{p.object.struttura_padre}")
                #result = queryset.models(Utenti).filter(struttura__exact=p.object.struttura_padre)
                #context['result'] = result
            #context['padre'] = struttura_name
                #return context
            """ else:
                figli = queryset.models(Struttura).filter(struttura_padre__exact=struttura_padre)
                utenti_padre = queryset.models(Utenti).filter(struttura__exact=struttura_padre)
                context['figli'] = figli
                context['result'] = utenti_padre
                context['root'] = struttura_padre
                print(f"else: {struttura_padre}") """
        #else:
        result = queryset.models(Utenti).filter(struttura__exact=struttura_name)
        context['result'] = result
        context['name'] = struttura_name
        context['numero_utenti'] = result.count()

        #context['padre'] = struttura_name
        #print(result)
        #print(f"struttura_padre: {test_padre}")
        #print(f"struttura_name: {struttura_name}")
        print("elseee")
        print(f"{result.count()}")
            #context['struttura_padre']=
        #context['struttura_padre']=
        return context



class UtentiView(ListView):
    template_name= 'search/utenti.html'

    def get_queryset(self):
        queryset = SearchQuerySet()
        #queryset = super().get_queryset()
        nome = self.kwargs["nome"]
        cognome = self.kwargs["cognome"]
        print(f"{nome} {cognome}: verifica")

        result = queryset.models(Utenti).filter(SQ(nome__exact=nome) & SQ(cognome__exact=cognome))
        #print(result_struttura)
        for d in result:
            print(f"Object: {d.object.struttura}")
        print(result)
            
        #return queryset
        return result
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # do something
        return context