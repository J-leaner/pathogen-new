from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Species, Genes, Markergenes, PhylogeneticTrees, FunctionAnnotations
from .serializers import SpeciesSerializer, GenesSerializer, MarkergenesSerializer, PhylogeneticTreesSerializer, FunctionAnnotationsSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class GenesViewSet(viewsets.ModelViewSet):
    queryset = Genes.objects.all()
    serializer_class = GenesSerializer

class MarkergenesViewSet(viewsets.ModelViewSet):
    queryset = Markergenes.objects.all()
    serializer_class = MarkergenesSerializer

class PhylogeneticTreesViewSet(viewsets.ModelViewSet):
    queryset = PhylogeneticTrees.objects.all()
    serializer_class = PhylogeneticTreesSerializer

class FunctionAnnotationsViewSet(viewsets.ModelViewSet):
    queryset = FunctionAnnotations.objects.all()
    serializer_class = FunctionAnnotationsSerializer