from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class financialData(models.Model):

	#entry information
	entryNo = models.IntegerField()
	companyName = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	
	#financial information fields
	ASSETS = models.FloatField()
	CASH = models.FloatField()
	CFFO = models.FloatField()
	COGS = models.FloatField()
	CURASS = models.FloatField()
	CURDEBT = models.FloatField()
	DEBTS = models.FloatField()
	INC = models.FloatField()
	INCDEP = models.FloatField()
	INV = models.FloatField()
	REC = models.FloatField()
	SALES = models.FloatField()
	WCFO = models.FloatField()

	def __str__(self):
			return self.companyName, self.date_posted