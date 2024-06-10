from django.urls import path
from .views import credentialList, CredentialDetail, CredentialCreate, CredentialUpdate, DeleteView, CustomLoginView, RegisterPage, CredentialReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', credentialList.as_view(), name='credentials'),
    path('credential/<int:pk>/', CredentialDetail.as_view(), name='credential'),
    path('credential-create/', CredentialCreate.as_view(), name='credential-create'),
    path('credential-update/<int:pk>/', CredentialUpdate.as_view(), name='credential-update'),
    path('credential-delete/<int:pk>/', DeleteView.as_view(), name='credential-delete'),
    path('credential-reorder/', CredentialReorder.as_view(), name='credential-reorder'),
]
