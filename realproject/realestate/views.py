from django.shortcuts import render

from .forms import SignUpForm
# Create your views here.
def index(request):
    title = "REAL ESTATE PROJECT"
    # if request.user.is_authenticated():
    #  title = "WELCOME %s" %(request.user)
    # #use this to display name of user who is login (request.user)
    # form = SignUpForm()
    context = {
       "template_title": title,
       # "form": form
    }
    return render(request, "base.html", context)

def accounts(request):
    return render(request, "accounts.html", {})