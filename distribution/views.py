from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from distribution.forms import DistributionForm, MessageForm, DistributionClientForm
from distribution.models import Distribution, Message, DistributionClient


class DistributionListView(ListView):
    model = Distribution


class DistributionDetailView(DetailView):
    model = Distribution
    template_name = 'distribution/distribution_detail.html'
    context_object_name = 'distribution'


class DistributionCreateView(CreateView):
    model = Distribution
    form_class = DistributionForm
    success_url = reverse_lazy('distribution:distribution_list')


class DistributionUpdateView(UpdateView):
    model = Distribution
    form_class = DistributionForm
    success_url = reverse_lazy('distribution:distribution_list')


class DistributionDeleteView(DeleteView):
    model = Distribution
    success_url = reverse_lazy('distribution:distribution_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('distribution:distribution_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('distribution:distribution_detail')


class DistributionClientListView(ListView):
    model = DistributionClient
    template_name = 'distribution/distribution_client_list.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['client_list'] = self.get_queryset()
        return context_data


class DistributionClientCreateView(CreateView):
    model = DistributionClient
    template_name = 'distribution/distribution_client_form.html'
    form_class = DistributionClientForm
    success_url = reverse_lazy('distribution:distribution_client_list')


class DistributionClientUpdateView(UpdateView):
    model = DistributionClient
    template_name = 'distribution/distribution_client_form.html'
    form_class = DistributionClientForm
    success_url = reverse_lazy('distribution:distribution_client_list')


class DistributionClientDeleteView(DeleteView):
    model = DistributionClient
    template_name = 'distribution/distribution_client_confirm_delete.html'
    success_url = reverse_lazy('distribution:distribution_client_list')
