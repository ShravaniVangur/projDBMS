from optparse import Option
from django.db import models
from datetime import datetime

stat = (('PROCESSING','PROCESSING'),('CLOSED','CLOSED'))
locations = (( 'Bangalore','Bangalore'),('Hyderabad','Hyderabad'),('Chennai','Chennai'),('Kolkata','Kolkata'),('Delhi','Delhi'),('Pune','Pune'),('Cochin','Cochin'))
gen = (('Male','Male'),('Female','Female'),('Non Binary','Non Binary'),('Not Specified','Not Specified'))
ctype = (('Violent Crime','Violent Crime'),('Property Crime','Property Crime'),('Public Order Crime','Public Order Crime'),('White Collar Crime','White Collar Crime'),('Organized Crime','Organized Crime'),('Cyber Crime','Cyber Crime'))
blood = (('A+','A+'),('A-','A-'),('B+','B-'),('O+','O-'),('AB+'),('AB+'),('AB-','AB-'),('Not Specified','Not Specified'))

class police_station(models.Model):
    psid = models.CharField(max_length=11)
    name = models.CharField(max_length=11)
    location = models.CharField(max_length=20,choices=locations ,default ='Bangalore')
    phoneno = models.IntegerField()
    def __str__(self) -> str:
        return self.psid 

class biodata(models.Model):
    name = models.CharField(max_length=11)
    address= models.CharField(max_length=2000)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=gen, default='Not Specified')
    phoneno= models.IntegerField()
    blood_group = models.CharField(max_length=20,choices=blood,default='Not Specified')

class officer_record(models.Model):
    ofid = models.CharField(max_length=11)
    psid = models.ForeignKey(police_station,on_delete=models.CASCADE)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    position = models.CharField(max_length=11)

class reporter(models.Model):
    rid=models.CharField(max_length=11)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    doffence = models.DateTimeField()
    dreport = datetime.now() 

class crime_register(models.Model):
    crimeid = models.CharField(max_length=11)
    ofid = models.ForeignKey(officer_record,on_delete=models.CASCADE)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    doffence= models.DateTimeField()
    dreport = datetime.now() 
    status = models.CharField(max_length=20,choices=stat, default='PROCESSING')
    crimetype = models.CharField(max_length=20,choices=ctype,default='Violent Crime')
    description = models.CharField(max_length= 2000)
    rid=models.ForeignKey(reporter,on_delete=models.CASCADE)

class accused(models.Model):
    accusedid = models.CharField(max_length=11)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    cid=models.ForeignKey(crime_register,on_delete=models.CASCADE)

class witness(models.Model):
    witnessid= models.CharField(max_length=11)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=stat,default='PROCESSING')
    cid=models.ForeignKey(crime_register,on_delete=models.CASCADE)

class victim(models.Model):
    vid = models.CharField(max_length=11)
    bio=models.ForeignKey(biodata,on_delete=models.CASCADE)
    cid=models.ForeignKey(crime_register,on_delete=models.CASCADE)

class criminal(models.Model):
    bio = models.ForeignKey(biodata,on_delete=models.CASCADE)
    evidence = models.CharField(max_length=2000)
    psid=models.ForeignKey(police_station,on_delete=models.CASCADE)
    crimeid = models.ForeignKey(crime_register,on_delete= models.CASCADE)

#hello