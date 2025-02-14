from questionary import Choise


def get_file(file_name: str):
    return Path(__file__).parent / 'env' / file_name

default_subnet = '1'
default_start = '100'
default_end = '250'