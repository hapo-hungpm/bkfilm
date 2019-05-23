from django.template.response import TemplateResponse
from django.shortcuts import render
from polls.forms import *
from django.http import JsonResponse
import json

from .models import *

import pysolr

option_query = {}
solr = pysolr.Solr('http://localhost:8983/solr/paper_final/', timeout=10)


def search(request):

    global option_query
    rows = 10
    currentPage = int (request.GET.get('page')) if request.GET.get('page') != "" else 1

    set_rows(rows)
    set_start(rows*(int(currentPage)-1))
    set_generic_args()

    results = solr.search(request.GET.get('search_query'), **option_query)

    print("Saw {0} result(s).".format(len(results)))
    numFound = results.raw_response['response']['numFound']
    qtime = results.raw_response['responseHeader']['QTime']/1000
    highlighting = list(results.raw_response['highlighting'].values())
    numPages = int((numFound/rows) if (numFound % rows == 0) else (numFound/rows+1))
    pages = set_pagination(numPages, currentPage)

    documents = []
    i = 0
    for doc in results:
        documents.append(doc)
        if highlighting[i].get('content') != None:
            doc['hl_content'] = highlighting[i].get('content')[0]
        else:
            doc['hl_content'] = doc['description']
        i += 1

    # print((highlighting))

    for doc in results.facets["facet_fields"]:
        print(results.facets["facet_fields"][doc])

    return render(request, 'result.html',
                  {
                      'search_query': request.GET.get('search_query'),
                      'documents': documents,
                      'numFound': numFound,
                      'qtime': qtime,
                      'highlighting': highlighting,
                      'pages': pages,
                      'page': currentPage,
                      'end_page': pages[-1]
                  })


def search_advance(request):

    global option_query
    rows = 10
    currentPage = int (request.GET.get('page')) if request.GET.get('page') != "" else 1

    set_rows(rows)
    set_start(rows*(int(currentPage)-1))
    set_generic_args()

    results = solr.search(request.GET.get('search_query') + ' AND author:\"' + request.GET.get('author') +'\"'
                          + ' AND category:\"' + request.GET.get('category') +'\"',
        **option_query)

    print("Saw {0} result(s).".format(len(results)))
    numFound = results.raw_response['response']['numFound']
    qtime = results.raw_response['responseHeader']['QTime']/1000
    highlighting = list(results.raw_response['highlighting'].values())
    numPages = int((numFound/rows) if (numFound % rows == 0) else (numFound/rows+1))
    pages = set_pagination(numPages, currentPage)

    documents = []
    i = 0
    for doc in results:
        documents.append(doc)
        if highlighting[i].get('content') != None:
            doc['hl_content'] = highlighting[i].get('content')[0]
        else:
            doc['hl_content'] = doc['description']
        i += 1

    # print((highlighting))

    for doc in results.facets["facet_fields"]:
        print(results.facets["facet_fields"][doc])

    return render(request, 'search_advance.html',
                  {
                      'init': False,
                      'search_query': request.GET.get('search_query'),
                      'documents': documents,
                      'numFound': numFound,
                      'qtime': qtime,
                      'highlighting': highlighting,
                      'pages': pages,
                      'page': currentPage,
                      'end_page': pages[-1]
                  })

def formView(request):
    return render(request, 'index.html')


def formAdvanceView(request):
    return render(request, 'search_advance.html', {'init': True})


def suggest_title(request):
    search_query = request.GET.get('search_query', None)
    print(search_query)
    solr = pysolr.Solr('http://localhost:8983/solr/paper_final/', search_handler="/suggest")
    raw_results = solr.search('', **{'suggest':'true', 'suggest.dictionary':'mySuggester', 'suggest.q': search_query})
    dicti = raw_results.raw_response['suggest']
    print(raw_results.raw_response['suggest']['mySuggester'][search_query]['suggestions'])
    return JsonResponse(json.dumps(raw_results.raw_response['suggest']['mySuggester'][search_query]['suggestions']), safe=False)


def set_rows(rows):
    option_query["rows"] = rows


def set_sort(field, sort_type):
    option_query["sort"] = field + ' ' + sort_type


def set_start(start):
    option_query["start"] = start


def set_generic_args():
    option_query["fl"] = ['title', 'time', 'url', 'content', 'description', 'author']
    option_query["facet"] = "on"
    # option_query["facet.field"] = ['rom', 'ram']
    # option_query["facet.limit"] = '-1'
    # option_query["facet.mincount"] = '1'
    option_query["hl"] = "true"
    option_query["hl.fl"] = "content"
    option_query["wt"] = "json"


def set_pagination(numPages, currentPage):
    pages = []
    if numPages < 10:
        for i in range(1, numPages + 1):
            pages.append(i)
    else:
        if currentPage >= (numPages - 10):
            for i in range(1, 11):
                pages.append(numPages - 10 + i)
        else:
            for i in range(currentPage, currentPage + 10):
                pages.append(i)

    return pages
