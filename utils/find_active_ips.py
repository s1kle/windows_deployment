from concurrent.futures import ThreadPoolExecutor
from typing import Callable


def find_active_ips(ping_fn: Callable[[str], str | None], prefix: str, start: int, end:int) -> list[str]:
    ips = [f'{prefix}.{x}' for x in range(start, end + 1)]

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(ping_fn, ips))
        
    return [x for x in results if x]