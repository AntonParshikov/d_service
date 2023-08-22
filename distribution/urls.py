from django.urls import path
from distribution.views import DistributionListView, DistributionDetailView, DistributionCreateView, \
    DistributionUpdateView, DistributionDeleteView, MessageCreateView, DistributionClientListView, \
    DistributionClientCreateView, DistributionClientUpdateView, DistributionClientDeleteView
from distribution.apps import DistributionConfig


app_name = DistributionConfig.name


urlpatterns = [
    path('', DistributionListView.as_view(), name='distribution_list'),
    path('distribution/<int:pk>/', DistributionDetailView.as_view(), name='distribution_detail'),
    path('create/', DistributionCreateView.as_view(), name='create_distribution'),
    path('update/<int:pk>/', DistributionUpdateView.as_view(), name='update_distribution'),
    path('delete/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_confirm_delete'),
    path('create/message/', MessageCreateView.as_view(), name='create_message'),
    path('client/', DistributionClientListView.as_view(), name='distribution_client_list'),
    path('client/create', DistributionClientCreateView.as_view(), name='create_distribution_client'),
    path('client/update/<int:pk>', DistributionClientUpdateView.as_view(),
         name='update_distribution_client'),
    path('client/delete/<int:pk>', DistributionClientDeleteView.as_view(),
         name='delete_distribution_client'),
]
