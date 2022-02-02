from django.shortcuts import redirect, render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import Http404

from .models import URL
from .forms import URLForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            val = URLValidator()
            try:
                print("ORIGINAL URL", form.cleaned_data['original_url'])
                val(form.cleaned_data['original_url'])
            except ValidationError:
                print("ERROR WITH URL VALIDATION")
                message = "Please enter a valid url"
                return render(request, 'main/index.html', {"message": message, "form": form})
            try:
                url_model = URL.objects.get(original_url = form.cleaned_data['original_url'])
                print("URL EXISTS")
                id = url_model.id
                # link = f'http://localhost:8000/{id}'
            except:
                print("NEW URL")
                id = form.save().id
            link = f'http://localhost:8000/{id}'
        else:
            link = ""
    else:
        form = URLForm()
        link = ""
    print("LINK", link)
    data = { "form": form, "link": link }
    return render(request, 'main/index.html', data)

def show(request, id):
    try:
        print("I am being ran")
        url = URL.objects.get(pk = id)
        return redirect(url.original_url)
    except:
        print("I am being excepted")
        raise Http404("url does not exist")

# def not_found_404(request, exception):
#     data = { 'err': exception }
#     return render(request, 'main/404.html', data)

def server_error_500(request):
    return render(request, 'main/500.html')



def not_found_404(request, exception):
    data = { "message": "That link doesn't work, sorry!", "form": URLForm() }
    # return render(request, 'main/index.html', data)
    return redirect("main-home")

# def server_error_500(request):
#     data = { "message": "that link doesn't work, drat" , "form": URLForm()}
#     return redirect("main-home", data)