from django.db import models

# Create your models here.
class  Topic(models.Model):
    TopicName=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.TopicName
class Webpage(models.Model):
    TopicName=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    url=models.URLField()
    Email=models.EmailField(default='chaithu28@gmail.com')

    def __str__(self):
        return self.Name
class AccessRecords(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self) :
        return self.Author