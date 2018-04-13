# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.shortcuts import render
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
            for i in range(1, int(row_count) + 1):
                matrix.append([int(request.POST.get('m_' + str(i) + '_' + str(j))) for j in range(1, int(row_count) + 1)], )

            for item in matrix:
                print item

            print np.linalg.det(matrix)

        except Exception as exc:

            logger.error(exc)

            return JsonResponse({
                "result": u"{}".format(str(exc))
            })

    context = {}
    template = 'index.html'

    return render(request, template, context)
