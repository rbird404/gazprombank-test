import logging
import os
import datetime


def file_remove(dir: str, days: int) -> None:
    now = datetime.datetime.now()

    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)

        if os.path.isfile(file_path):
            file_modification_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            )
            delta = now - file_modification_date
            if delta.days >= days:
                os.remove(file_path)
                logging.warning(f"Файл {filename} удален")


directory = 'test_dir'
days = 0
file_remove(directory, days)
