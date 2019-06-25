from django.db import models
from datetime import datetime
import bcrypt
now = str(datetime.now())



class UserManager(models.Manager):
    def regValidator(self, form):
        
        errors = {}
        if len(form['name']) == 0:
            errors['name'] = 'Name cannot be blank'
        elif len(form['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'
        else:
            users = User.objects.filter(name=form['name'])
            if users:
                errors['name'] = "user is already in database"
        if len(form['username']) == 0:
            errors['username'] = 'Username cannot be blank' 
        elif len(form['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters'
        if len(form['password']) == 0:
            errors['password'] = 'password cannot be blank'
        elif len(form['password']) < 8:
            errors['password'] = 'password must be at least 8 characters'
        if form['confirm_PW'] != form['password']:
            errors['confirm_PW'] = 'passwords do not match!'
      
        return errors

    def loginValidator(self, form):
        errors = {}
        
        if len(form['login_username']) == 0:
            errors['login_username'] = 'Username cannot be blank'
        elif len(form['login_username']) < 3:
            errors['login_username'] = 'Username must be at least 3 characters'
        if len(form['pwd']) == 0:
            errors['pwd'] = 'Password cannot be blank'
        elif len(form['pwd']) < 8:
            errors['pwd'] = 'password must be at least 8 characters'
        else:
            users = User.objects.filter(username=form['login_username'])
            if not users:
                errors['login_username'] = 'This Username doesnt exist. Please register!'
            elif not bcrypt.checkpw(form['pwd'].encode(), users[0].password.encode()):
                errors['pwd'] = 'Wrong password'
        return errors
class TripManager(models.Manager):
    def tripValidator(self, form):
        print(form)
        errors = {}
        if len(form['destination']) == 0:
            errors['destination'] = 'Destination cannot be blank'
        if len(form['description']) == 0:
            errors['description'] ='Description cannot be blank'
        if len(form['travelDateFrom']) == 0:
            errors['travelDateFrom'] = 'TravelDateFrom cannot be blank'
        elif form['travelDateFrom']  <= now:
            errors['travelDateFrom'] = 'Invalid'
        if len(form['travelDateTo']) == 0:
            errors['travelDateTo'] = 'TravelDateTo cannot be blank'
        elif str(form['travelDateTo']) < str(form['travelDateFrom']):
            errors['travelDateTo'] = 'Invalid!!!'
        return errors
        

















class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    

class Trip(models.Model):
    destination = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    travelDateFrom = models.DateTimeField()
    travelDateTo = models.DateTimeField()
    planned_By = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    jointrip = models.ManyToManyField(User, related_name='triptogether')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
    
