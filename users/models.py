from django.db   import models
from core.models import TimeStampModel

class User(TimeStampModel):
    name             = models.CharField(max_length=45)
    account          = models.CharField(max_length=45, null=True, unique=True)
    mobile_number    = models.CharField(max_length=45)
    password         = models.CharField(max_length=200, null=True)
    address          = models.CharField(max_length=200, null=True)
    email            = models.CharField(max_length=45, null=True)
    mileage          = models.IntegerField(default=0)
    point            = models.DecimalField(default=1000000.0 ,max_digits=15, decimal_places=3)
    gender           = models.BooleanField()
    foreigner        = models.BooleanField()
    date_of_birth    = models.DateField(null=True)

    class Meta:
        db_table = "users"
