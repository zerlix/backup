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
