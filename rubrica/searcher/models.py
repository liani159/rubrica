from django.db import models

# Create your models here.

class Struttura(models.Model):
    # many to one: ForeignKeyField
    #many to many: ManyToManyField
    # aggiungere id
    #nome_struttura = models.CharField(max_length=200, primary_key=True)
    nome_struttura = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200)
    struttura_padre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nome_struttura}"


class Utenti(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    data_nascita = models.DateField()
    titolo = models.CharField(max_length=200)
    struttura = models.ForeignKey(Struttura, on_delete=models.CASCADE)
    #db_column="nome_struttura"
    #struttura_padre = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome}"


