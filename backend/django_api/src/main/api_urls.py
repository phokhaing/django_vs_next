from django.urls import path, include

urlpatterns = [
   # auth/account_login, account_logout, account_set_password
   path('auth/', include('allauth.urls')),
   # auth/ signup/ [name='account_signup']
   # auth/ login/ [name='account_login']
   # auth/ logout/ [name='account_logout']
   # auth/ password/change/ [name='account_change_password']
   # auth/ password/set/ [name='account_set_password']
   # auth/ inactive/ [name='account_inactive']
   # auth/ email/ [name='account_email']
   # auth/ confirm-email/ [name='account_email_verification_sent']
   # auth/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
   # auth/ password/reset/ [name='account_reset_password']
   # auth/ password/reset/done/ [name='account_reset_password_done']
   # auth/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
   # auth/ password/reset/key/done/ [name='account_reset_password_from_key_done']
   
   path('users/', include('user_management.urls')),
   
   path('appraisal/', include('appraisal.urls'))

]