from pathlib import Path

import subprocess
import questionary as q

from utils import create_inventory, get_ips, ping, get_file, default_subnet, default_end, default_start, create_environment, load_yaml, save_yaml


inventory_file = get_file('inventory.yml')
environment_file = get_file('environment.yml')
entry_filename = 'entry.yml'

subnet = q.text('Номер подсети: ', default_subnet).ask()
start = int(q.text('Начало диапазона: ', default_start).ask())
end = int(q.text('Конец диапазона: ', default_end).ask())

prefix = f'192.168.{subnet}'

print('Поиск рабочих ip-адресов...')
ips = get_ips(ping, prefix, start, end)

print('Найденные адреса:')
print(ips)

print('Создание', inventory_file)
create_inventory(ips, inventory_file)

print('Загрузка', environment_file)
environment = load_yaml(environment_file)

package_names = list(environment['pkgs'].keys())
package_choices = [Choice(item, checked=True) for item in package_names]
selected_packages = q.checkbox('Выберите пакеты:', choices=package_choices).ask()

for package in environment['pkgs']:
    environment['pkgs'][package]['checked'] = package in selected_packages

print('Создание', environment_file)
save_yaml(environment_file, environment)


print('Запуск', entry_filename)
subprocess.run(['ansible-playbook', '-i', inventory_file, entry_filename])