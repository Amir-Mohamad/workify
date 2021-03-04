from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .models import AboutUsModel, WorkSamples
from .forms import ContactUsForm, NewsLetterForm



class Home(View):
    template_name = 'core/home.html'
    
    def get(self, request, *args, **kwargs):
        workSamples = WorkSamples.objects.filter(promote=True)
        context = {'worksamples':workSamples}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        newsletter = NewsLetterForm(request.POST)
        if newsletter.is_valid():
            newsletter.save()
            return redirect('core:home')
            messages.success(request, 'You successfully submit your form') # :\
        context = {'newsletter':newsletter}
        return render(request, self.template_name, context)

class AboutUsList(ListView):
    queryset = AboutUsModel.objects.filter(is_active=True)
    template_name = 'core/about-us.html'
    context_object_name = 'members'

class ContactUs(FormView):
    template_name = 'contact.html'
    form_class = ContactUsForm
    success_url = 'core:home'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)