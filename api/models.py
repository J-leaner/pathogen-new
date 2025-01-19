from django.db import models

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=255)
    taxonomy = models.CharField(max_length=255, null=True, blank=True)
    genome_data_url = models.TextField(null=True, blank=True)

class Genes(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sequence = models.TextField()
    function_annotation = models.TextField(null=True, blank=True)
    gene_type = models.CharField(max_length=255)

class Markergenes(models.Model):
    gene = models.ForeignKey(Genes, on_delete=models.CASCADE)
    marker_type = models.CharField(max_length=255)

class PhylogeneticTrees(models.Model):
    tree_data = models.TextField()
    species_list = models.TextField()

class FunctionAnnotations(models.Model):
    gene = models.ForeignKey(Genes, on_delete=models.CASCADE)
    ontology_type = models.CharField(max_length=255)
    annotation_details = models.TextField()