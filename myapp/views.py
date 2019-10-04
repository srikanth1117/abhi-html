from django.shortcuts import render
from django_xhtml2pdf.views import PdfMixin
from django.views.generic import ListView,DetailView
from .models import Agreement
# Create your views here.
class ListView(ListView):
    model = Agreement

class DetailView(PdfMixin,DetailView):
    model = Agreement
