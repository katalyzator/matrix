# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

import numpy as np


def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)


def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new


# def power_method(mat, start, maxit):
#     """
#     Does maxit iterations of the power method
#     on the matrix mat starting at start.
#     Returns an approximation of the largest
#     eigenvector of the matrix mat.
#     """
#     result = start
#     for i in xrange(maxit):
#         result = mat * result
#         result = result / np.linalg.norm(result)
#     return result
#
#
# def check(mat, otp):
#     """
#     Compares the output otp of the power
#     method with the largest eigenvalue
#     of the matrix mat.
#     """
#     prd = mat * otp
#     eigval = prd[0] / otp[0]
#     print 'computed eigenvalue :', eigval
#     [eigs, vecs] = np.linalg.eig(mat)
#     abseigs = list(abs(eigs))
#     ind = abseigs.index(max(abseigs))
#     print ' largest eigenvalue :', eigs[ind]


@csrf_exempt
def index_view(request):
    if request.method == 'POST':
        try:
            matrix = []
            row_count = request.POST.get('row_length')
            col_count = request.POST.get('col_length')

            for i in range(0, int(row_count)):
                for j in range(0, int(col_count)):
                    print request.POST.get('m_' + str(i) + '_' + str(j))

            for i in range(0, int(col_count)):
                matrix.append(
                    [int(request.POST.get('m_' + str(i) + '_' + str(j))) for j in range(0, int(row_count))], )
            X = np.array(matrix)
            print matrix
            result = np.linalg.det(matrix)
            print power_iteration(X)
            j = complex(0, 1)
            nbs = np.random.normal(0, 1, (row_count, 1)) \
                  + np.random.normal(0, 1, (row_count, 1)) * j
            rndvec = np.matrix(nbs)
            # eigmax = power_method(X, rndvec, 10)
            # print check(X, eigmax)

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
