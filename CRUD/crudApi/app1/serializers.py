from rest_framework import serializers
from .models import Database

class DatabaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()
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