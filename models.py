from django.db import models

# Create your models here.
class Dataset(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 
  
    class Meta:
        db_table = 'dataset_table'
        


class InceptionV3_model(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    model_accuracy = models.CharField(max_length=100)
    model_executed = models.CharField(max_length=100)
    class Meta:
        db_table = "InceptionV3_model"



class EfficientNet_model(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    model_accuracy = models.CharField(max_length=100)
    model_executed = models.CharField(max_length=100)

    class Meta:
        db_table = "EfficientNet_model"
        
        
class Hybrid_model(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    model_accuracy = models.CharField(max_length=100)
    model_executed = models.CharField(max_length=100)

    class Meta:
        db_table = "Hybrid_model"



class Comparison_graph(models.Model):
    S_No = models.AutoField(primary_key=True)
    Inception = models.CharField(max_length=10, null=True)
    EfficientNet = models.CharField(max_length=10, null=True)
    Hybrid = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "Comparisongraph"
        
        
class graph_model(models.Model):
    Fake_details=  models.CharField(max_length=100)
    Real_details =  models.CharField(max_length=100)

    class Meta:
        db_table = "graph_model"



class Train_test_split_model(models.Model):
    S_No = models.AutoField(primary_key=True)
    Images_training = models.CharField(max_length=10, null=True)
    Images_validation = models.CharField(max_length=10, null=True)
    Images_classes = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "Traintestsplit"