from rest_framework import viewsets
from .serializers import ContactSerializer, EmailSerializer, PhoneSerializer
from .models import Contact, Email, Phone_no
import django_filters

class ContactFilter(django_filters.FilterSet):
    hasemail = django_filters.BooleanFilter(field_name='emails',lookup_expr='isnull', exclude=True)
    hasphone = django_filters.BooleanFilter(field_name='phone_nos',lookup_expr='isnull', exclude=True)
    
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'available']

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = []
    search_fields = ('first_name', 'nick_name', 'last_name')
    filterset_class = ContactFilter

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone_no.objects.all()
    serializer_class = PhoneSerializer


