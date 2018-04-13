# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


@csrf_exempt
def index_view(request):
    if request.method == 'POST':
        try:

            row_count = request.POST.get('row_length')
            for i in range(1, int(row_count)):
                for j in range(1, int(row_count)):
                    print request.POST.get('m_' + str(i) + '_' + str(j))

            print row_count

        except Exception as exc:

            logger.error(exc)

            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    context = {}
    template = 'index.html'

    return render(request, template, context)
