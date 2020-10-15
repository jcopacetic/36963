from allauth.account.decorators import login_required
from django.shortcuts import render

@login_required
def Dashboard(request):
  return render(request, "dashboard/dashboard.html")