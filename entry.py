from pathlib import Path
import subprocess
import questionary as q

from utils import create_inventory, get_ips, ping, get_file, default_subnet, default_end, default_start, create_environment

ansible_args_file = get_file(ansible.yml)
environment_args_file = get_file(environment.yml)
packages_args_file = get_file(packages.yml)
inventory_filename = 'inventory.yml'
environment_filename = 'environment.yml'
entry_filename = 'entry.yml'

subnet = q.text('Номер подсети: ', default_subnet).ask()
start = q.text('Начало диапазона: ', default_start).ask()
end = q.text('Конец диапазона: ', default_end).ask()

prefix = f'192.168.{subnet}'

print('Поиск рабочих ip-адресов...')
ips = get_ips(ping, prefix, start, end)

print('Создание', inventory_filename)
create_inventory(ips, inventory_filename)

print('Создание', environment_filename)
create_environment()

print('Запуск', entry_filename)
subprocess.run(['ansible-playbook', '-i', inventory_filename, entry_filename])