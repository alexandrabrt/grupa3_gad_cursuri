from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from aplicatie2.models import Companies


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:adaugare')


class ListCompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')
