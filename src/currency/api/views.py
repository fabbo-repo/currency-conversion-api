from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from src.currency.models import Currency
from src.currency.api.serializers import CurrencySerializer


class CurrencyRetrieveView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @method_decorator(cache_page(12 * 60 * 60))
    def get(self, request, *args, **kwargs):
        """
        This view will be cached for 12 hours
        """
        return super(CurrencyRetrieveView, self).get(request, *args, **kwargs)


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    @method_decorator(cache_page(12 * 60 * 60))
    def get(self, request, *args, **kwargs):
        """
        This view will be cached for 12 hours
        """
        return super(CurrencyListView, self).get(request, *args, **kwargs)
