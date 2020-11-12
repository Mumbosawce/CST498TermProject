from django.shortcuts import render
from .models import financialData
from .forms import FinanceDataForm


# Create your views here.
def enterData(request):
	form = FinanceDataForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "prediction/financeData.html", context)
