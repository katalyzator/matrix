# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

import numpy as np
import sympy as sp


@csrf_exempt
def index_view(request):
    if request.method == 'POST':
        try:
            matrix = []
            row_count = request.POST.get('row_length')
            # for i in range(0, int(row_count)):
            #     for j in range(0, int(row_count)):
            #         print i, j
            for i in range(0, int(row_count)):
                matrix.append(
                    [int(request.POST.get('m_' + str(i) + '_' + str(j))) for j in range(0, int(row_count))], )

            # for item in matrix:
            #     print item

            result = np.linalg.det(matrix)

            return JsonResponse(dict(result=result))

        except Exception as exc:

            logger.error(exc)

            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    context = {}
    template = 'index.html'

    return render(request, template, context)


@csrf_exempt
def matrix_view(request):
    context = {}
    template = 'matrix.html'

    return render(request, template, context)

# @csrf_exempt
# def ajax_det_calc(request):
#     response = JsonResponse(dict(result=result))
#
#     return response
