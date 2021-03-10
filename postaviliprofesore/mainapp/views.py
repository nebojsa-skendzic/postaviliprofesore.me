from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UpdatedFilesSerializer
from django.db.models import Q  # noqa: F401
from .models import UpdatedFiles, Fakultet, Smjer, Semestar
from ucginfimport import getlinks
import json

#  http://127.0.0.1:8000/result/https://www.ucg.ac.me/objave_spisak/blog/44389,https://www.ucg.ac.me/objave_spisak/blog/44390,https://www.ucg.ac.me/objave_spisak/blog/43073,https://www.ucg.ac.me/objave_spisak/blog/43072,https://www.ucg.ac.me/objave_spisak/blog/43989,https://www.ucg.ac.me/objave_spisak/blog/43988,https://www.ucg.ac.me/objave_spisak/blog/55432,https://www.ucg.ac.me/objave_spisak/blog/55431


def searchResult(request):
    query = request.GET.get('q')
    obj = Semestar.objects.filter(smjer__fakultet__fakultet=query).order_by('-smjer__smjer', 'semestar')
    test = {}
    listofsmjer = []
    for i in obj:
        if i.smjer not in listofsmjer:
            listofsmjer.append(i.smjer)

    for i in listofsmjer:
        test[i] = {x.semestar: x.resultlink for x in obj if x.smjer == i}

    return render(request, "mainapp/search.html", {'result': obj, 'test': test})


def index(request):

    return render(request, "mainapp/index.html")


def test(request):

    return render(request, "mainapp/test.html")


def napravisvoj(request):

    return render(request, "mainapp/napravi-svoj.html")


def resultView(request, webtag):
    splitted = webtag.split(",")
    for i in splitted:
        if i == "":
            splitted.remove(i)
        else:
            if not UpdatedFiles.objects.filter(webtag=i):
                getlinks(i)

    execstr = "UpdatedFiles.objects.filter("
    for i in splitted:  # Building the command based on number of links requested
        if splitted.index(i) == len(splitted) - 1:
            execstr += "Q(webtag='{}')).order_by('-date')".format(i)
        else:
            execstr += "Q(webtag='{}')|".format(i)

    results = eval(execstr)

    splitlist = json.dumps(splitted)

    context = {
        'results': results,
        'splitted': splitlist,
    }

    return render(request, "mainapp/results.html", context)


@api_view(['GET'])
def apiView(request):
    api_urls = {
        'Detail View': '/detail-view/<str:webtag>/',
        'List of colleges': '/api/fakultet-view/',

    }
    return Response(api_urls)


@api_view(['GET'])
def detailView(request, webtag):
    splitted = webtag.split(",")
    for i in splitted:
        if i == "":
            splitted.remove(i)
        else:
            if not UpdatedFiles.objects.filter(webtag=i):
                getlinks(i)

    execstr = "UpdatedFiles.objects.filter("
    for i in splitted:  # Building the command based on number of links requested
        if splitted.index(i) == len(splitted) - 1:
            execstr += "Q(webtag='{}')).order_by('-date')".format(i)
        else:
            execstr += "Q(webtag='{}')|".format(i)

    objlist = eval(execstr)

    serializer = UpdatedFilesSerializer(objlist, many=True)

    return Response(serializer.data)


from django.http import JsonResponse  # noqa: E402, F401


@api_view(['GET'])
def fakultetView(request):
    fobjs = Fakultet.objects.values_list('fakultet', flat=True)
    counter = 1
    result = {}
    for element in fobjs:
        result[element] = counter
        counter += 1

    return Response(result)
