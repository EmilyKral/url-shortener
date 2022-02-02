from django.shortcuts import redirect, render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import Http404

from .models import URL
from .forms import URLForm


def home(request, data={}):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            val = URLValidator()
            try:
                val(form.cleaned_data['original_url'])
            except ValidationError:
                message = "Please enter a valid url"
                return render(request, 'main/index.html', {"message": message, "form": form})
            try:
                url_model = URL.objects.get(
                    original_url=form.cleaned_data['original_url'])
                id = url_model.id
            except:
                id = form.save().id
            link = f'http://localhost:8000/{id}'
        else:
            link = ""
    else:
        form = URLForm()
        link = ""
    data["form"] = form
    data["link"] = link
    return render(request, 'main/index.html', data)


def show(request, id):
    try:
        url = URL.objects.get(pk=id)
        return redirect(url.original_url)
    except:
        raise Http404("url does not exist")


def server_error_500(request):
    return render(request, 'main/500.html')


def not_found_404(request, exception):
    data = {"message": "That link doesn't work, sorry!", "form": URLForm()}
    return redirect("main-home")
