from django.urls import path

from expense import views

urlpatterns = [
    path('get_transactions/',views.get_transaction),
    path('transactions/',views.TransactionAPI.as_view()),


]
