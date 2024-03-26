# Backup-Skript mit Python

Dieses Python-Skript bietet eine einfache Möglichkeit, Verzeichnisse und MySQL-Datenbanken auf einem Linux-System zu sichern. Das Skript unterstützt die regelmäßige Durchführung von Backups durch die Verwendung einer Konfigurationsdatei.

## Voraussetzungen

- Python 3
- Linux-Betriebssystem
- MySQL-Installation mit entsprechenden Zugangsdaten

## Installation und Verwendung

1. **Herunterladen des Skripts**: Lade das Skript herunter und speichere es auf deinem Linux-System.

2. **Konfigurationsdatei erstellen**: Erstelle eine JSON-Datei mit dem Namen `cfg.json`. In dieser Datei werden die MySQL-Zugangsdaten, die zu sichernden Verzeichnisse und der Speicherort für die Backups konfiguriert. Ein Beispiel für den Inhalt der Konfigurationsdatei findest du weiter unten.

3. **Ausführung des Skripts**: Führe das Skript aus, indem du es in einem Terminal öffnest und `python backup_script.py` eingibst. Stelle sicher, dass du über die erforderlichen Berechtigungen verfügst, um auf die zu sichernden Verzeichnisse und die MySQL-Datenbanken zuzugreifen.

## Beispielkonfiguration (cfg.json)

```json
{
  "mysql_user": "benutzername", 
  "mysql_password": "passwort",
  "mysql_databases": ["datenbank1", "datenbank2"],
  
  "backup_location": "/pfad/zum/backup/verzeichnis",
  "backup_dirs": ["/pfad/zum/verzeichnis1", "/pfad/zum/verzeichnis2"]
}
- `mysql_user`: Der Benutzername für den Zugriff auf die MySQL-Datenbanken.
- `mysql_password`: Das Passwort für den MySQL-Benutzer.
- `mysql_databases`: Eine Liste der zu sichernden MySQL-Datenbanken.
- `backup_location`: Der Pfad zum Verzeichnis, in dem die Backups gespeichert werden sollen.
- `backup_dirs`: Eine Liste der zu sichernden Verzeichnisse.
```
### Funktionen des Skripts

- **print_error(msg)**: Gibt eine Fehlermeldung in roter Farbe aus.
- **print_success(msg)**: Gibt eine Erfolgsmeldung in grüner Farbe aus.
- **print_warning(msg)**: Gibt eine Warnung in gelber Farbe aus.
- **read_config()**: Liest die Konfigurationsdatei aus und gibt sie als Dictionary zurück.
- **check_backupDir()**: Überprüft und erstellt die Backup-Verzeichnisse, falls sie nicht vorhanden sind.
- **backup_dirs()**: Sichert die angegebenen Verzeichnisse in komprimierten Tar-Dateien.
- **backup_databases()**: Sichert die angegebenen MySQL-Datenbanken als SQL-Dump-Dateien.

### Hinweis

Dieses Skript wurde für den Einsatz auf Linux-Systemen entwickelt und erfordert die entsprechenden Berechtigungen zum Ausführen von Sicherungen und zum Zugriff auf die Datenbanken und Verzeichnisse. Stelle sicher, dass du die Sicherheitsbestimmungen und Datenschutzrichtlinien deines Systems beachtest, insbesondere im Umgang mit sensiblen Daten wie Passwörtern und Datenbankinhalten.
