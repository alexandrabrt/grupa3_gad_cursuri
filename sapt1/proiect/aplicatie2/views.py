from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from aplicatie2.models import Companies


class CreateCompaniesView(CreateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:adaugare')


class ListCompaniesView(ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class UpdateCompaniesView(UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')
