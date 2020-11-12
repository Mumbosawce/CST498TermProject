from django import forms
from .models import financialData


class FinanceDataForm(forms.ModelForm):
	class Meta:
		model = financialData
		fields = [
			"ASSETS","CFFO", "COGS", 
			"CURASS", "CURDEBT", "DEBTS", 
			"INC", "INCDEP", "INV",
			"REC", "SALES", "WCFO" 
		]