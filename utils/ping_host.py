import subprocess


def ping_host(address: str) -> str | None:
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '1', address], stdout=subprocess.DEVNULL)
        return address if not result.returncode else None
    except Exception as exception:
        print(f'Нет доступа к {address}: {exception}')