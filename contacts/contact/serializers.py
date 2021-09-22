from rest_framework import serializers
from .models import Contact, Email, Phone_no

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_no
        fields = ['phone_number']

class ContactSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True)
    phone_nos = PhoneSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['id','first_name', 'nick_name', 'last_name', 'available', 'emails', 'phone_nos']

    def create(self, validated_data):
        phone_nos_data = validated_data.pop('phone_nos')
        emails_data = validated_data.pop('emails')
        contact = Contact.objects.create(**validated_data)
        for email_data in emails_data:
            Email.objects.create(contact=contact, **email_data)
        for phone_data in phone_nos_data:
            Phone_no.objects.create(contact=contact, **phone_data)
        return contact

