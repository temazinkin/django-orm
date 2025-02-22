from django.http import HttpResponse
from django.shortcuts import render
from notebooks.utils import print_sql, sql_raw
from django.db.models import (
    Q,
    F,
    Case,
    When,
    Count,
    Func,
    Min,
    Max,
    Sum,
    Avg,
    Value,
    OuterRef,
    Subquery,
    CharField,
)
from django.db.models.functions import Concat, Cast, Round, Length
from django.db import connection
from pandas import DataFrame as df

from customer_db.models import Province, Patient, Doctor, Admission


def show(request):
    qs = Patient.objects.all().values()

    context = {
        'qs': df(qs).to_html,
    }

    return render(
        request,
        template_name='show.html',
        context=context
    )
