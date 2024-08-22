import logging as log
import os

def logger(path=None, intention='warn', message=None):
    try:
        log.basicConfig(filename=path,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=log.INFO)

        if intention == 'error':
            log.error(message)
        elif intention == 'info':
            log.info(message)
        else:
            log.warning(message)

        return {'message': 'log generated successfully'}
    except Exception as error:
        return {'message': f'unable to generate logs as saying {error}'}
