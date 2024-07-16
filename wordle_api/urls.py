from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodaysWordView, DifferentWordView

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'words', WordViewSet)
# router.register(r'user-profiles', UserProfileViewSet)
# router.register(r'', home_page_view)

urlpatterns = [
#     path('', include(router.urls)),
    path("todays-word", TodaysWordView.as_view(), name='todays-word'),
    path('different-word/', DifferentWordView.as_view(), name='different-word'),
]
