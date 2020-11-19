from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    """Model definition for Transactions."""

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_field = models.AutoField(primary_key=True)
    transaction_desc = models.CharField(max_length=500)
    transaction_amount = models.FloatField()
    transaction_date = models.DateField(auto_now=False, auto_now_add=False)


    class Meta:
        """Meta definition for Transactions."""

        verbose_name = 'Transactions'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transactions."""
        return self.transaction_desc+" "+self.user.first_name+" "+self.user.last_name
