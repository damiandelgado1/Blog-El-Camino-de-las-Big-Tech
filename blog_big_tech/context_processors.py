from blog.forms import SuscribeForm

def form_context(request):
    return {"form": SuscribeForm()}