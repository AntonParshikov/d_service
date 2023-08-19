from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from distribution.forms import DistributionForm, MessageForm
from distribution.models import Distribution, Message, DistributionClient
from users.models import Users


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


# class DistributionUserListView(ListView):
#     model = DistributionClient
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#
#         context_data['user'] = Users.objects.all()
#         context_data['distribution_pk'] = self.kwargs.get('pk')
#
#         return context_data
#
#
# def toogle_user(request, pk, user_pk):
#     if DistributionClient.objects.filter(
#         user_id=user_pk,
#         distribution_settings_id=pk
#     ).exists():
#         DistributionClient.objects.filter(
#             user_id=user_pk,
#             distribution_settings_id=pk
#         ).delete()
#
#     else:
#         DistributionClient.objects.create(
#             user_id=user_pk,
#             distribution_settings_id=pk
#         ).delete()
#     return redirect(reverse('distribution:distributionclient_list', args=[pk]))
