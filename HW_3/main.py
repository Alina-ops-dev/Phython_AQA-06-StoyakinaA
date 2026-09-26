import test_data

user_input = int(input("Сколько тестовых пользователей сгенерировать? "))

users = []
for userss in range(user_input):
    user = test_data.generate_user()
    users.append(user)
print('Пользователи:')

for user in users:
    print(user)

active_count = 0
blocked_count = 0
inactive_count = 0

for user in users:
    if user['status'] == 'ACTIVE':
        active_count += 1
    elif user['status'] == 'BLOCKED':
        blocked_count += 1
    elif user['status'] == 'INACTIVE':
        inactive_count += 1

print('Статистика по статусам:')
print(f'ACTIVE: {active_count}')
print(f'BLOCKED: {blocked_count}')
print(f'INACTIVE: {inactive_count}')
