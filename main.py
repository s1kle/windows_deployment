from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path

from utils import load_yaml, save_yaml

import uvicorn
import os
import subprocess


class Host(BaseModel):
    ip: str | None


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'],
                   allow_headers=['*'])

@app.post('/trigger-ansible')
async def trigger_ansible(host: Host):
    if host.ip:
        inventory_file = Path(__file__).parent / 'inventory.yml'
        entry_filename = 'entry.yml'
        inventory = load_yaml(inventory_file)
        inventory['windows']['hosts'] = [host.ip]
        save_yaml(inventory_file, inventory)
        env = os.environ.copy()
        env['ANSIBLE_DISPLAY_SKIPPED_HOSTS'] = 'False'

        subprocess.run(['ansible-playbook', '-i', inventory_file, entry_filename], env=env)
    else:
        print('no ip found')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)        