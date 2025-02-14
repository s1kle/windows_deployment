from pathlib import Path
import subprocess
import questionary as q

from utils import create_inventory, get_ips, ping, get_file, default_subnet


ansible_args_file = get_file(ansible.yml)
environment_args_file = get_file(environment.yml)
packages_args_file = get_file(packages.yml)

subnet = q.text('Номер подсети: ', default_subnet).ask()


subnet = input('Номер подсети: ')
start = int(input('Начало диапазона: '))
end = int(input('Конец диапазона: '))

prefix = f'192.168.{subnet}'

print('Поиск рабочих ip-адресов...')
ips = get_ips(ping, prefix, start, end)

print('Создание файла инвентаря...')
create_inventory(ips, 'inventory.yml')

print('Запуск entry.yml')
subprocess.run(['ansible-playbook', '-i', 'inventory.yml', 'entry.yml'])