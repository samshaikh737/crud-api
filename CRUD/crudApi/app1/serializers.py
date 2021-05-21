from rest_framework import serializers
from .models import Database
from django.http import JsonResponse


def email_checker(value):
    db = Database.objects.filter(email = value)
    if db.exists():
        raise serializers.ValidationError("Email is exits")

def age_checker(value):
    if value >= 100:
        raise serializers.ValidationError("sorry your age is can't accept")

class DatabaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(validators=[age_checker])
    email = serializers.EmailField(validators=[email_checker])
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Database.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.age = validated_data.get("age",instance.age)
        instance.email = validated_data.get("email",instance.email)
        instance.city = validated_data.get("city",instance.city)

        instance.save()
        return instance

    # def validate_age(self, value):
    #     if value >= 100:
    #         raise serializers.ValidationError("sorry your age is can't accept")
    #     return value
    
    # def validate_email(self, value):
    #     db = Database.objects.filter(email = value)
    #     if db.exists():
    #         raise serializers.ValidationError("email is exits")
    #     return value

    # def validate(self, value):
    #     name = value.get("name")
    #     age = value.get("age")
    #     city = value.get("city")

    #     if age >= 100:
    #         raise serializers.ValidationError("sorry your age is can't accept")
    #     return value