from rest_framework import serializers
from .models import WeatherEntity

class WeatherSerializer(serializers.Serializer):
    # Definindo os campos do serializer
    temperature = serializers.FloatField()  # Campo para a temperatura, sendo um número de ponto flutuante
    city = serializers.CharField(max_length=100, required=False)  # Campo para a cidade, opcional
    atmosphericPressure = serializers.CharField(max_length=100, required=False)  # Campo para a pressão atmosférica, opcional
    humidity = serializers.CharField(max_length=100, required=False)  # Campo para a umidade, opcional
    weather = serializers.CharField(max_length=100, required=False)  # Campo para o clima, opcional
    date = serializers.DateTimeField()  # Campo para a data e hora

    def create(self, validated_data):
        # Método para criar uma nova instância de WeatherEntity a partir dos dados validados
        return WeatherEntity(**validated_data)

    def update(self, instance, validated_data):
        # Método para atualizar uma instância existente de WeatherEntity com os dados validados
        # Aqui, estamos atualizando os campos da instância com os dados fornecidos,
        # ou mantendo os valores existentes se nenhum valor for fornecido
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.date = validated_data.get('date', instance.date)
        return instance