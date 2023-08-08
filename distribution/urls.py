from django.urls import path
from distribution.views import DistributionListView, DistributionDetailView, DistributionCreateView, \
    DistributionUpdateView, DistributionDeleteView
from distribution.apps import DistributionConfig

app_name = DistributionConfig.name

urlpatterns = [
    path('users/', DistributionListView.as_view(), name='distribution_list'),
    path('users/<int:pk>/', DistributionDetailView.as_view(), name='distribution_detail'),
    path('create/', DistributionCreateView.as_view(), name='create_distribution'),
    path('update/<int:pk>/', DistributionUpdateView.as_view(), name='update_distribution'),
    path('delete/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_confirm_delete'),

]
