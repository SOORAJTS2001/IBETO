from django.db import models

# Create your models here.
# it is in the format of key value
ROOM_CHOICES = (
    ('bedroom1-2nd floor','bedroom1-2nd floor'),
    ('familyroom-2nd floor','familyroom-2nd floor'),
    ('bath-2nd floor','bath-2nd floor'),
    ('stairentry-2nd floor','stairentry-2nd floor'),
    ('empty-2nd floor','empty-2nd floor'),
    ('stairexit-2nd floor','stairexit-2nd floor'),
    ('bedroom3-2nd floor','bedroom3-2nd floor'),
    ('bedroom2-2nd floor','bedroom2-2nd floor'),
    ('bathroom-2nd floor','bathroom-2nd floor'),
    #this is the 1st floor
    ('kitchen-1st floor','kitchen-1st floor'),
    ('bedroom1-1st floor','bedroom1-1st floor'),
    ('empty-1st floor','empty-1st floor'),
    ('bath-1st floor','bath-1st floor'),
    ('stairentry-1st floor','stairentry-1st floor'),
    ('bath2-1st floor','bath2-1st floor'),
    ('room-1st floor','room-1st floor'),
    ('stairexit-1st floor','stairexit-1st floor'),
    ('formaldinnning-1st floor','formaldinnning-1st floor'),
    ('office-1st floor','office-1st floor'),
    ('familyroom-1st floor','familyroom-1st floor'),
    ('exit-1st floor','exit-1st floor'),
)

class MyModel(models.Model):
  From = models.CharField(max_length=600, choices=ROOM_CHOICES, default='Hall')
  To = models.CharField(max_length=600, choices=ROOM_CHOICES, default='Hall')