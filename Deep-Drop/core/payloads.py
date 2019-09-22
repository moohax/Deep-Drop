import os

from core import config


def patch_payloads(payload_files, domain):
    server = '**server**'

    for pfile in payload_files:
        new_payload = open(payload_files[pfile], 'r').read().replace(server, config.domain)

        domain = config.domain.split('.')[0]

        new_payload_file = os.path.join(config.basedir, 'macros', f'{domain}.{pfile}')

        with open(new_payload_file, 'w') as f:
            f.write(new_payload)
