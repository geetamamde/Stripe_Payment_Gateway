from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('details/<id>',views.details),
    # path('create-checkout-session/<id>',views.create_checkout_session),
    # path('success',views.success),
    # path('cancel',views.cancel),
    path('checkout-session/<str:id>/', views.create_checkout_session, name='checkout_session'),
    path('payment-cancelled', views.payment_cancelled, name='payment_cancelled'),
    path('payment-successful', views.payment_successful, name='payment_successful'),
]