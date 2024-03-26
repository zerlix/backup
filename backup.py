import json
import platform
import os
import tarfile
import datetime
import subprocess

def print_error(msg):
    # Gibt farbliche(rot) fehlermeldung aus
    print("\033[31m" + msg + "\033[0m")

    
def print_success(msg):
    # gibt farbliche(grün) erfolgreiche meldung aus   
    print("\033[32m" + msg + "\033[0m")


def print_warning(msg):
    # Gibt farbliche(gelb) Warnung aus
    print("\033[33m" + msg + "\033[0m")


def read_config():
    # liest die Konfigurationsdatei aus und gibt sie als dict zurück
    try:
        with open('./cfg.json') as f:
            return json.load(f)
    except:
        print_error("Konfigurationsdatei nicht gefunden.")
        exit()
        

def check_backupDir():
    # Überprüfe, ob die Verzeichnise existieren, wenn nicht werden sie erstellt
    if not os.path.isdir(cfg['backup_location']):
        print_warning("Backup-Verzeichnis existiert nicht, wird erstellt")
        try:
            os.mkdir(cfg['backup_location'])
        except:
            print_error("Konnte Verzeichnis nicht erstellen.")
            exit()
        print_success("Verzeichnis " + cfg['backup_location'] + " wurde erstellt.")
        
    if not os.path.isdir(cfg['backup_location'] + '/sql'):
        print_warning("MySQL-Backup-Verzeichnis existiert nicht, wird erstellt")
        try:
            os.mkdir(cfg['backup_location'] + '/sql')
        except:
            print_error("Konnte Verzeichnis nicht erstellen.")
            exit()
        print_success("Verzeichnis " + cfg['backup_location'] + '/sql' + " wurde erstellt.")
        
    if not os.path.isdir(cfg['backup_location'] + '/files'):
        print_warning("Dateien-Backup-Verzeichnis existiert nicht, wird erstellt")
        try:
            os.mkdir(cfg['backup_location'] + '/files')
        except:
            print_error("Konnte Verzeichnis nicht erstellen.")
            exit()
        print_success("Verzeichnis " + cfg['backup_location'] + '/files' + " wurde erstellt.")
    return True


def backup_dirs():
    # Backup von angegeben Verzeichnisse
    for dir in cfg['backup_dirs']:
        if not os.path.isdir(dir):
            print_error(f"Verzeichnis {dir} existiert nicht!")
            return False
        else:
            print(f"Sichere Verzeichnis {dir} ...")
            dir_name = os.path.basename(dir)
            backup_file = f"{cfg['backup_location']}/files/{dir_name}_{now}.tar.gz"

            # Backup erstellen
            with tarfile.open(backup_file, "w:gz") as tar:
                tar.add(dir, arcname=os.path.basename(dir))
                tar.close()
        print_success(f"Backup für Verzeichnis {dir} erstellt: {backup_file}")
    return True

def backup_databases():
    # Backup der Datenbanken
    for db in cfg['mysql_databases']:
        
        db_file = f"{cfg['backup_location']}/sql/{db}_{now}.sql"
        cmd = ['mysqldump', '-u', cfg['mysql_user'], '-p' + cfg['mysql_password'], db]

        print(f"Sichere Datenbank {db}...")    
                
        result = subprocess.call(cmd, stdout=subprocess.DEVNULL) # dry run
        if result == 0:
            with open(db_file, 'w') as f:
                subprocess.run(cmd, stdout=f)
            print_success(f"Backup für Datenbank {db} erstellt: {db_file}")
        else:
            print_error(f"Fehler beim Backup der Datenbank {db}")             
    return True


if __name__ == '__main__':
    if platform.system()!= "Linux":
        print_error("Das script wurde für Linux entwickelt und kann nicht ausgeführt")
        exit()
    date_fmt = "%Y_%m_%d-%H_%M"
    now = datetime.datetime.now().strftime(date_fmt)
    cfg = read_config()
    check_backupDir()
    backup_dirs()
    backup_databases()    
    
