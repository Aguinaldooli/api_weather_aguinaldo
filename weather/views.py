from bible_verse import main
from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from .exceptions import WeatherException

class WeatherView(View):
    def get(self, request):
        verse = main.get_bible_verse()
        repository = WeatherRepository(collectionName='weathers')
        try:
            weathers = list(repository.getAll())
            serializer = WeatherSerializer(data=weathers, many=True)
            if (serializer.is_valid()):
                modelWeather = serializer.save()
                print(serializer.data)
            else:
                print(serializer.errors)
            objectReturn = {"weathers":modelWeather, "verse":verse}
        except WeatherException:
            objectReturn = {"error":str(WeatherException), "verse":verse}

        print (objectReturn)
        return render(request, "home.html", objectReturn)
    
            

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now()
        )
        serializer = WeatherSerializer(data=weather.__dict__)
        if serializer.is_valid():
            repository.insert(serializer.validated_data)
        else:
            print(serializer.errors)

        return redirect('weather-view')
    
class WeatherReset(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()

        return redirect('weather-view')
