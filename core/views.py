from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.views.generic.list import ListView
<<<<<<< HEAD
from django.views.generic import FormView
from django.urls import reverse
=======
from django.views.generic import FormView, CreateView
from django.contrib.messages.views import SuccessMessageMixin as message
from django.contrib.auth.mixins import LoginRequiredMixin
>>>>>>> 6068d3e73a1ed95296493264025e6d62263e68a1
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


# class ContactUsView(FormView): 
#     form_class = ContactUsForm 
#     template_name = "core/contact-us.html"
#     success_url = reverse_lazy("core:home")


def contactusview(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('core:home')
    return render(request, 'core/contact-us.html', {'form':form})


# emad ..

# class ContactUs(LoginRequiredMixin, message, CreateView):
#     template_name = 'core/contact-us.html'
#     form_class = ContactUsForm
#     success_url = reverse_lazy('core:home')
#     success_message = 'form saved.'

#     def form_valid(self, form):
#         cd = form.cleaned_data
#         f = form.save(commit=False)
#         f.user = self.request.user
#         f.save()
#         return super().form_valid(form)
