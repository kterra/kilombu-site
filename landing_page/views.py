from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from validate_email_address import validate_email
from .forms import MailForm
from .models import Visitor

# Create your views here.
def index(request):

    if request.method == "POST":
        visitor_email = request.POST["news_later_email"]
        if(validate_email(visitor_email)):
            visitor = Visitor(email=visitor_email)
            visitor.save()

    return render(request, "landing_page/index.html", {})

@login_required
def registered_emails(request):
    return render(request, "emails_list.html", {})
