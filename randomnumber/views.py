from django.shortcuts import render
from django.views import View
import random


class RandomNumberView(View):
    # Функция для отображение файла html:
    def get(self, request):
        return render(request, 'home.html')


class GetRandomNumberView(View):
    # Функция для генерации случайного числа:
    def generate(self):
        num = random.randrange(1, 1000)
        return num

    # Функция для вывода результата:
    def get(self, request):
        context = {'number': self.generate()}
        return render(request, 'random.html', context)


