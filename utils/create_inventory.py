def create_inventory(address_list: list[str], output_file: str) -> None:
    ansible_args: list[str] = []
    
    with open('src/var/ansible_args.txt', 'r') as args_file:
        ansible_args = args_file.readlines()
    
    with open(output_file, 'w') as inventory_file:
        inventory_file.write('windows:\n  hosts:\n')
        for line in address_list:
            inventory_file.write(f'    {line}:\n')
        inventory_file.write('  vars:\n')
        for line in ansible_args:
            inventory_file.write(f'    {line}')