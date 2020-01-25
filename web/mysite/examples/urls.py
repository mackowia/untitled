from django.urls import path
from . import views     # from . -> sprawia, żeby na pewno z tego katalogu wzieło

urlpatterns = [
    path('dogs/<init:id>', views.dog, name="dog"),
    #http://127.0.0.1:8000/calc/add/1/1 (+)
    #http://127.0.0.1:8000/calc/sub/5/3 (-)
    #http://127.0.0.1:8000/calc/mul/3/10 (*)
    #http://127.0.0.1:8000/calc/div/12/4 (/)
    path('calc/<dzialanie>/<init:a>/<init:b>', views.calculator),



    #http://127.0.0.1:8000/texts/abcdejhkhkjkC
    path('texts/int:ile_gwiazdek>/<user_text>', views.cool_text),
    #http://127.0.0.1:8000/hello/Magda
    path('hello\<imie>', views.hello),
    path('about', views.about),
    path('', views.index)
]