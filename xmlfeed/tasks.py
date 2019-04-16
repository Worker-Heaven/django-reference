from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from .models import Person

import random

logger = get_task_logger(__name__)


@task()
def hello():
    print('Hello World')


@task(name='add_new_member')
def add():
    random_name = str(random.randint(1, 1000))

    print(random_name)

    Person.objects.get_or_create(name=('Random Name' + random_name))