from django.db import models

class waste(models.Model):
    id=models.IntegerField(primary_key=True,max_length=25)
    type=models.CharField(max_length=25)
    quantity=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    current_status=models.CharField(max_length=25)



class recycle(models.Model):
    id=models.IntegerField(primary_key=True,max_length=25)
    center_name=models.CharField(max_length=25)
    location=models.CharField(max_length=25)
    recyable_types=models.CharField(max_length=25)



class treatment(models.Model):
    id=models.IntegerField(primary_key=True,max_length=25)
    name=models.CharField(max_length=25)
    location=models.CharField(max_length=25)


class user(models.Model):
    id=models.IntegerField(primary_key=True,max_length=25)
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=30)
    

class collection(models.Model):
    id=models.IntegerField(primary_key=True,max_length=25)
    collection_time=models.DateTimeField()
    user_id=models.ForeignKey(user,default=None)


