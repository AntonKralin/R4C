from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import json

from .functions import parse_json, save_robot
from .exceptions import ValidJSON, DublicateData


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
