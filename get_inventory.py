from pathlib import Path

import questionary as q

from utils import get_ips, ping, default_subnet, default_end, default_start, load_yaml, save_yaml


inventory_file = Path(__file__).parent / 'inventory.yml'

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