from course.models import Product, Group, Lesson
from django.contrib.auth import get_user_model
from django.core.cache import cache

import itertools, time


def get_next_name_of_group(product: Product) -> str:
    last_name = max(product.group_product.all(), key=lambda group: int(group.title.split('_')[-1])).title
    course_name, group_prefix, digit_part = last_name.split('_')
    return f'{course_name}_{group_prefix}_{int(digit_part) + 1}'


def get_min_group(product: Product, all_groups) -> Group:
    try:
        smallest_group = min(
            filter(lambda group: len(group) < product.max_students_in_group, all_groups), key=len)
    except ValueError:
        print('Все группы заполенены\nСоздадим новую')
        smallest_group = Group.objects.create(title=get_next_name_of_group(product), product=product)
        product.group_product.add(smallest_group)
    return smallest_group


def refill_groups(product: Product):
    users_iterator = iter(product.students.all())
    for group in product.group_product.all():
        group.students.clear()
    for group in itertools.cycle(list(product.group_product.all())):
        try:
            group.students.add(next(users_iterator))
        except StopIteration:
            print("Все ученики распределены")
            break


def invite_member(member: get_user_model(), product: Product):
    cache.set('all_groups', product.group_product.prefetch_related('students').all())
    min_group = get_min_group(product, cache.get('all_groups'))
    min_group.students.add(member)

    cache.set('all_groups', product.group_product.prefetch_related('students').all())

    if (len(max(cache.get('all_groups'), key=len)) - len(min(cache.get('all_groups'), key=len)) > 1 and
            len(product.students.all()) >= len(cache.get('all_groups')) * product.min_students_in_group):
        refill_groups(product)
        cache.delete('all_groups')
    cache.delete('all_groups')

