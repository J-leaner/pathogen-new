from rest_framework import serializers
from .models import Species, Genes, Markergenes, PhylogeneticTrees, FunctionAnnotations

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class GenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genes
        fields = '__all__'

class MarkergenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markergenes
        fields = '__all__'

class PhylogeneticTreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhylogeneticTrees
        fields = '__all__'

class FunctionAnnotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionAnnotations
        fields = '__all__'