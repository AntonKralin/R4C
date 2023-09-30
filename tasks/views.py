from django.http import HttpRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import json
import os

from .functions import parse_json, save_robot
from .exceptions import ValidJSON, DublicateData
from .report import create_file


# Create your views here.
@require_http_methods(["POST"])
@csrf_exempt
def add(request: HttpRequest):
    try:
        data = json.loads(request.body)
        robot = parse_json(data)
        save_robot(robot)
        return JsonResponse({'success': True})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'invalid JSON'})
    except ValidJSON as ex:
        return JsonResponse({'success': False, 'error': str(ex)})
    except DublicateData as ex:
        return JsonResponse({'success': False, 'error': str(ex)})
    except ValueError:
        return JsonResponse({'success': False, 'error': 'ValueError'})


@require_http_methods(["GET"])
def report(request: HttpRequest):
    filename = create_file(7)
    if os.path.exists(filename):
        with open(filename, mode='rb') as fh:
            response = HttpResponse(fh.read(),
                                    content_type="application/ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(filename)
        return response
