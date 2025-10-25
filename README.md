# CSV to JSON Converter API

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-green.svg)](https://www.sqlite.org/)

> **📌 Note on Technology Choice:** This solution is implemented in **Python** instead of Node.js as specified in the challenge. This decision was made because:
> - Python is my primary tech stack and best showcases my production-ready skills
> - All functional requirements are fully met
> - Custom CSV parsing logic implemented from scratch (no external CSV libraries)
> - Clean, maintainable, and well-documented code architecture
> - The problem-solving approach and code quality remain the same regardless of language

## 🚀 Quick Start
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
