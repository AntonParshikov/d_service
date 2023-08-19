from django.urls import path
from distribution.views import DistributionListView, DistributionDetailView, DistributionCreateView, \
    DistributionUpdateView, DistributionDeleteView, MessageCreateView
from distribution.apps import DistributionConfig

app_name = DistributionConfig.name

urlpatterns = [
    path('', DistributionListView.as_view(), name='distribution_list'),
    path('distribution/<int:pk>/', DistributionDetailView.as_view(), name='distribution_detail'),
    path('create/', DistributionCreateView.as_view(), name='create_distribution'),
    path('update/<int:pk>/', DistributionUpdateView.as_view(), name='update_distribution'),
    path('delete/<int:pk>/', DistributionDeleteView.as_view(), name='distribution_confirm_delete'),
    path('create/message/', MessageCreateView.as_view(), name='create_message'),
    # path('<int:pk>/users', DistributionUserListView.as_view(), name='distributionclient_list'),
    # path('<int:pk>/users/add/<int:user_pk>', toogle_user, name='distribution_toggle_user')

]
