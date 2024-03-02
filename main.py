# import itertools
# import time
#
#
# class User:
#     def __init__(self, username: str) -> None:
#         self.username = username
#
#     def __str__(self) -> str:
#         return self.username
#
#
# class Product:
#     def __init__(self, id: int, name: str, groups: list = [], members: list = []) -> None:
#         self.id = id
#         self.name = name
#         self.groups = groups
#         self.members = members
#         self.min_members_in_group = 5
#         self.max_members_in_group = 8
#
#
# class Group:
#     def __init__(self, name: str, product: Product = None, users: list = []) -> None:
#         self.name = name
#         self.product = product
#         self.users = users
#
#     def __str__(self) -> str:
#         return f'{self.name} length={len(self.users)}'
#
#     def __len__(self):
#         return len(self.users)
#
#
# # users = [User(username=f'user_{i}') for i in range(19)]
#
# # gr_1 = Group(name='group_55', users=[User(username=f'user_{i}') for i in range(1)])
# # gr_2 = Group(name='group_22', users=[User(username=f'user_{i}') for i in range(9)])
# # gr_3 = Group(name='group_10', users=[User(username=f'user_{i}') for i in range(9)])
#
# # pr_1 = Product(id=1, name='Product 1', groups=[gr_1, gr_2, gr_3], members=users)
#
#
# def get_next_name_of_group(product: Product) -> str:
#     last_name = max(product.groups, key=lambda group: int(group.name.split('_')[-1])).name
#     char_part, digit_part = last_name.split('_')
#     return f'{char_part}_{int(digit_part) + 1}'
#
#
# # print(get_next_name_of_group(pr_1))
#
#
# def get_min_group(product: Product) -> Group:
#     smallest_group = None
#     try:
#         smallest_group = min(filter(lambda group: len(group) < product.max_members_in_group, product.groups), key=len)
#     except ValueError:
#         print('Все группы заполенены\nСоздадим новую')
#         smallest_group = Group(name=get_next_name_of_group(product), product=product, users=[])
#         # print(smallest_group)
#         product.groups.append(smallest_group)
#     return smallest_group
#
#
# def refill_groups(product: Product):
#     users_iterator = iter(product.members)
#     for group in product.groups:
#         group.users.clear()
#     for group in itertools.cycle(product.groups):
#         try:
#             group.users.append(next(users_iterator))
#         except StopIteration:
#             print("Все ученики распределены")
#             break
#
#
# # print(len(max(pr_1.groups, key=len)))
# # print(len(min(pr_1.groups, key=len)))
#
# def invite_member(member: User, product: Product):
#     product.members.append(member)
#
#     if len(product.groups) == 0:
#         group = Group(name='name_1', product=product)
#         product.groups.append(group)
#         group.users.append(member)
#     else:
#         min_group = get_min_group(product)
#         min_group.users.append(member)
#
#         if len(max(product.groups, key=len)) - len(min(product.groups, key=len)) > 1 and len(product.members) >= len(
#                 product.groups) * product.min_members_in_group:
#             refill_groups(product)
#     for group in product.groups:
#         print(group)
#
#     print(len(product.members))
#     print('##############################')
#
#     time.sleep(2)
#
#
# # print(get_min_group(pr_1.groups, pr_1))
#
# # print(min('group_1', 'group_2', 'group_3', 'group_4'))
#
# # refill_groups(pr_1)
#
# test_user_list = [User(username=f'user_{i}') for i in range(29)]
# test_product = Product(id=1, name='name_1')
#
# print(test_product.min_members_in_group)
# print(test_product.max_members_in_group)
#
# for student in test_user_list:
#     invite_member(student, test_product)
