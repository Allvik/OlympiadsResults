import csv
from django.http import HttpResponse
from django.shortcuts import render
import urllib.parse


class SchoolResults:
    cnt_winners = 0
    cnt_prizers = 0
    school = ''

    def __init__(self, _school):
        self.school = _school


def select_year(request):
    with open("olymp.csv", "r") as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        years = dict()
        for cur in results:
            years[cur['Year']] = True
        return render(request, 'select_year.html', {'years': years})


def select_subject(request, year):
    old_year = urllib.parse.unquote_plus(year)
    with open('olymp.csv', "r") as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        subjects = dict()
        for cur in results:
            if cur['Year'] == old_year:
                subjects[cur['Subject']] = True
        return render(request, 'select_subject.html', {'subjects': subjects})


def select_type(request, year, subject):
    old_year = urllib.parse.unquote_plus(year)
    old_subject = urllib.parse.unquote_plus(subject)
    with open("olymp.csv", "r") as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        types = dict()
        for cur in results:
            if cur['Year'] == old_year and cur['Subject'] == old_subject:
                types[cur['OlympiadType']] = True
        return render(request, 'select_type.html', {'types': types})


def select_stage(request, year, subject, type):
    old_year = urllib.parse.unquote_plus(year)
    old_subject = urllib.parse.unquote_plus(subject)
    old_type = urllib.parse.unquote_plus(type)
    with open("olymp.csv", "r") as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        stages = dict()
        for cur in results:
            if cur['Year'] == old_year and cur['Subject'] == old_subject and cur['OlympiadType'] == old_type:
                stages[cur['Stage']] = True
        return render(request, 'select_stage.html', {'stages': stages})


def get_results(request, year, subject, type, stage):
    old_year = urllib.parse.unquote_plus(year)
    old_subject = urllib.parse.unquote_plus(subject)
    old_type = urllib.parse.unquote_plus(type)
    with open('olymp.csv') as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        my_results = dict()
        for cur in results:
            if cur['Year'] == old_year and cur['Subject'] == old_subject and cur['OlympiadType'] == old_type and cur['Stage'] == stage:
                if cur['FullName'] not in my_results:
                    my_results[cur['FullName']] = SchoolResults(cur['FullName'])
                if cur['Status'] == 'призёр':
                    my_results[cur['FullName']].cnt_prizers += 1
                if cur['Status'] == 'победитель':
                    my_results[cur['FullName']].cnt_winners += 1
        array_results = []
        for cur in my_results:
            array_results.append(my_results[cur])
        array_results.sort(key=lambda x: [-x.cnt_winners, -x.cnt_prizers])
        while len(array_results) > 20:
            array_results.pop()
        return render(request, 'results.html', {'results': array_results})


def test(request):
    with open('olymp.csv') as fin:
        results = csv.DictReader(fin, delimiter=';', quotechar='"')
        cnt_winners = 0
        cnt_prizers = 0
        cnt_others = 0
        for cur in results:
            if cur['Subject'] == 'Информатика' and cur['Stage'] == "4" and cur['Year'] == '2018/2019' and \
                cur['OlympiadType'] == 'Всероссийская олимпиада':
                    if cur['Status'] == 'призёр':
                        cnt_prizers += 1
                    elif cur['Status'] == 'победитель':
                        cnt_winners += 1
                    else:
                        cnt_others += 1
    return HttpResponse(f"{cnt_winners}, {cnt_prizers}, {cnt_others}")
