import shutil
import os 
import datetime

def backup_file(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, 'gztar', source)

source = r"C:\Users\utkar\automation"
destination = r"C:\Users\utkar\automation\backups"

backup_file(source, destination)