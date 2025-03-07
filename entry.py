from pathlib import Path

import os
import subprocess
import questionary as q

from utils import get_ips, ping, default_subnet, default_end, default_start, default_choise, load_yaml, save_yaml


inventory_file = Path(__file__).parent / 'inventory.yml'
environment_file = Path(__file__).parent / 'environment.yml'
entry_filename = 'entry.yml'

subnet = q.text('Номер подсети: ', default_subnet).ask()
start = int(q.text('Начало диапазона: ', default_start).ask())
end = int(q.text('Конец диапазона: ', default_end).ask())

prefix = f'192.168.{subnet}'

print('Поиск рабочих ip-адресов...')
ips = get_ips(ping, prefix, start, end)

print('Загрузка', inventory_file)
inventory = load_yaml(inventory_file)
inventory['windows']['hosts'] = [{ip: None} for ip in ips]

print('Сохранение', inventory_file)
save_yaml(inventory_file, inventory)

print('Загрузка', environment_file)
environment = load_yaml(environment_file)

wifi = environment['wifi']
choise = q.text(f'Сменить wifi (Текущий: {wifi['ssid']}) y/n?', default_choise)
if choise == 'y':
    new_ssid = q.text('SSID: ')
    new_password = q.text('Password: ')
    environment['wifi']['ssid'] = new_ssid
    environment['wifi']['password'] = new_password


package_names = list(environment['pkgs'].keys())
package_choices = [q.Choice(item, checked=True) for item in package_names]
selected_packages = q.checkbox('Выберите пакеты:', choices=package_choices).ask()

for package in environment['pkgs']:
    environment['pkgs'][package]['checked'] = package in selected_packages

print('Сохранение', environment_file)
save_yaml(environment_file, environment)

env = os.environ.copy()
env['ANSIBLE_DISPLAY_SKIPPED_HOSTS'] = 'False'

print('Запуск', entry_filename)
subprocess.run(['ansible-playbook', '-i', inventory_file, entry_filename], env=env)