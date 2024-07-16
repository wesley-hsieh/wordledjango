from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.views import View
from django.core.cache import cache
from .models import Word, UserProfile
import random

class TodaysWordView(View):
    def get(self, request):
        if 'todays_word' not in request.session:
            words = Word.objects.all()
            if words.exists():
                word = random.choice(words).word
                request.session['todays_word'] = word
            else:
                word = None
        else:
            word = request.session['todays_word']
        return JsonResponse({'word': word})

# View to get a different word
class DifferentWordView(View):
    def get(self, request):
        used_words = request.session.get('used_words', [])
        words = Word.objects.exclude(word__in=used_words)
        if words.exists():
            word = random.choice(words).word
            used_words.append(word)
            request.session['used_words'] = used_words
        else:
            word = None
        return JsonResponse({'word': word})



#example dummy homepage view
def home_page_view(request):
    return HttpResponse("Hello, World")
