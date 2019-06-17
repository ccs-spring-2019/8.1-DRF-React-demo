from rest_framework import serializers
from .models import Pizza


# use Django REST Framework to transform data into JSON
class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza  # specify the fields we want to expose
        fields = ('id', 'name', 'toppings')
        depth = 1  # https://www.django-rest-framework.org/api-guide/serializers/#specifying-nested-serialization
