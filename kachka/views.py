from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import Trainer,Contact,Article
from .forms import ContactForm
from .bot import send_message
from django.contrib import messages  # new
from django.urls import reverse  # new
from .forms import ArticleForm, CommentForm


def home_view(request):
    trainers = Trainer.objects.all()
    context = {"trainers":trainers}
    return render(request, "index.html",context=context )


def trainer_view(request):
    return render(request, "trainer.html")


#-----------------------------------------------------------------------------------------------------------------

def contact_view(request):
    
    if request.method == "GET":
        form  = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone_number = form.cleaned_data["phone_number"]
        description = form.cleaned_data["description"]

        send_message(name,email,phone_number,description)
        
        form.save()
        form = ContactForm()
        
    context = {"form":form}


    return render(request, "contact.html",context)


def create_article(request):

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']

            article = Article(
                title=title,
                description=description,
                image=image,
            )
            article.save()
            messages.success(request, '🥳 Maqolangiz adminga yuborildi, tekshiruvdan so\'ng chop etiladi')
            return HttpResponseRedirect(reverse('articles-list'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    else:
        form = ArticleForm()
    context = {"form": form}
    
    return render(request, "contact.html", context)

#--------------------------------------------------------------------------------------------------------------------


def why_view(request):
    return render(request, "why.html")


def base_view(request):
    return render(request,"base.html")
