import json
from django.shortcuts import render, HttpResponse, Http404

# Create your views here.

def dismiss_marketing_message(request):
    if request.is_ajax():
        data = {'success': True}
        json_data = json.dumps(data)
        print data
        print json_data
        return HttpResponse(json_data, content_type='application/json')
    else:
        return Http404
