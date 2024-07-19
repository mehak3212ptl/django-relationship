from django.db import models

# Create your models here.
class Price(models.Model):
    price=models.IntegerField()
    def __str__(self):
        return str(self.price)
    
class Company(models.Model):
    company=models.CharField(max_length=50)
    price=models.OneToOneField(Price,on_delete=models.CASCADE)
    def __str__(self):
        return self.company
    
class Title(models.Model):
    title=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Books(models.Model):
    name=models.CharField(max_length=45)
    # price=models.OneToOneField(Price,on_delete=models.CASCADE)
    # company=models.ForeignKey(Company,on_delete=models.CASCADE)
    title=models.ManyToManyField(Title)
    def __str__(self):
        return self.name+' '+str(self.title)