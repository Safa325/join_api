# Join - Backend

## Beschreibung

Das Backend für die **Join-To-Do-App** ist mit dem Django Framework und Django REST Framework (DRF) entwickelt. Es stellt die API-Endpunkte bereit, die die Frontend-Anwendung nutzen kann, um Aufgaben, Benutzer und andere Daten zu verwalten. Das Projekt ist auf **PythonAnywhere** gehostet und bietet eine stabile Grundlage für die Verwaltung der App-Daten.

---

## Inhaltsverzeichnis

1. [Features](#features)
2. [API-Endpunkte](#api-endpunkte)
3. [Installation und Einrichtung](#installation-und-einrichtung)
4. [Datenbank](#datenbank)
5. [Deployment auf PythonAnywhere](#deployment-auf-pythonanywhere)
6. [Projektstruktur](#projektstruktur)

---

## Features

- **Benutzer-Authentifizierung**: Eigene Benutzeranmeldung mit Token-Authentifizierung.
- **RESTful API**: CRUD-Funktionen für Aufgaben, Benutzer und Boards.
- **Datenbankintegration**: SQLite als lokale Datenbank, Unterstützung für MySQL oder PostgreSQL bei Bedarf.
- **Host**: Deployment auf PythonAnywhere für einfachen Zugriff.
- **Admin-Bereich**: Voll funktionsfähiger Django-Admin-Bereich zur Verwaltung der Daten.

---

## API-Endpunkte

### Benutzer
- `POST /api/register/` - Registriere einen neuen Benutzer.
- `POST /api/login/` - Login und Erhalt eines Tokens.
- `GET /api/users/` - Liste aller Benutzer (Admin-Zugriff erforderlich).

### Aufgaben
- `GET /api/tasks/` - Liste aller Aufgaben.
- `POST /api/tasks/` - Erstelle eine neue Aufgabe.
- `PUT /api/tasks/<id>/` - Bearbeite eine vorhandene Aufgabe.
- `DELETE /api/tasks/<id>/` - Lösche eine Aufgabe.

### Boards
- `GET /api/boards/` - Liste aller Boards.
- `POST /api/boards/` - Erstelle ein neues Board.

---

## Installation und Einrichtung

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python-Paketmanager)
- Virtuelle Umgebung (optional, aber empfohlen)

### Schritte

1. **Repository klonen**
   ```bash
   git clone https://github.com/dein-github-account/join-backend.git
   cd join-backend
