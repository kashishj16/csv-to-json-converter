# CSV to JSON Converter API

A Python application that converts CSV files to JSON and stores data in SQLite.

## Features
- Custom CSV parser (no external CSV libraries)
- Nested object support with dot notation
- **SQLite database (no installation required!)**
- Age distribution analysis
- Handles 50,000+ records

## Setup

1. **Clone and setup:**
```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
```

2. **Configure `.env`:**
```env
   DB_PATH=./database.db
   CSV_FILE_PATH=./data/users.csv
```

3. **Run:**
```bash
   python -m app.main
```

## Database
Uses SQLite - a file-based database (`database.db`) created automatically.
No installation or configuration needed!

## View Data
- Install [DB Browser for SQLite](https://sqlitebrowser.org/)
- Open `database.db` file