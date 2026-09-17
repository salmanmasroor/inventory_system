# Smart Inventory Management System

A command-line inventory application built with Python and SQLite. It supports user authentication, product CRUD, categories, suppliers, search with pagination, input validation, and structured logging.

Uses only the Python standard library — no pip packages required.

---
## Features

- **Authentication** — Register and login with email validation and SHA-256 password hashing
- **Products** — Add, view, update, delete, and search with pagination
- **Categories & Suppliers** — Manage related records linked to products
- **Stock tracking** — Low-stock monitoring via background scheduler (optional)
- **Logging** — Inventory changes written to `app.log`

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  CLI Layer (cli/)                                       │
│  menu.py, auth_ui.py, product_ui.py, category_ui.py     │
│  → prints menus, reads input, basic validation          │
└───────────────────────┬─────────────────────────────────┘
                        │ calls
┌───────────────────────▼─────────────────────────────────┐
│  Service Layer (services/)                              │
│  auth_service, product_service, category_service, ...   │
│  → business rules, hashing, logging                     │
└───────────────────────┬─────────────────────────────────┘
                        │ calls
┌───────────────────────▼─────────────────────────────────┐
│  Repository Layer (repositories/)                       │
│  base_repository + *_repository                         │
│  → SQL queries only                                     │
└───────────────────────┬─────────────────────────────────┘
                        │ reads/writes
┌───────────────────────▼─────────────────────────────────┐
│  SQLite (inventory.db) via database.py                  │
└─────────────────────────────────────────────────────────┘
```

**Request flow:** `CLI → Service → Repository → Database`

Models (`models/`) are plain Python objects passed between layers. Shared helpers live in `core/` and `config.py`.

---

## Project Structure

```
inventory_system/
│
├── main.py                     # Application entry point
├── config.py                   # Paths and app constants
├── database.py                 # SQLite schema setup (runs on import)
├── logger.py                   # Logging to app.log
│
├── cli/                        # Presentation layer (menus & input)
│   ├── menu.py                 # Main app loop and navigation
│   ├── auth_ui.py              # Login & registration screens
│   ├── product_ui.py           # Product menus and pagination
│   ├── category_ui.py          # Category management UI
│   └── supplier_ui.py          # Supplier management UI
│
├── services/                   # Business logic
│   ├── auth_service.py         # Register, login, password hashing
│   ├── product_service.py      # Product CRUD and search
│   ├── category_service.py     # Category operations
│   └── supplier_service.py     # Supplier operations
│
├── repositories/               # Data access (SQL only)
│   ├── base_repository.py      # Shared DB connection helpers
│   ├── user_repository.py
│   ├── product_repository.py
│   ├── category_repository.py
│   └── supplier_repository.py
│
├── models/                     # Domain objects
│   ├── user.py
│   ├── product.py
│   ├── category.py
│   └── supplier.py
│
├── core/                       # Shared utilities
│   ├── utils.py                # Input helpers (get_int, get_float, get_text)
│   └── exceptions.py           # Custom application errors
│
├── jobs/                       # Background tasks
│   ├── scheduler.py            # Low-stock check thread
│   └── send_email.py           # Email alert helper (optional)
│
├── tests/
│   ├── test_product_service.py
│   └── test_repositories.py
│
├── requirements.txt
├── inventory.db                # Auto-generated (gitignored)
└── app.log                     # Auto-generated (gitignored)
```

### Layer Responsibilities

| Layer | Folder | Responsibility |
|-------|--------|----------------|
| CLI | `cli/` | Menus, user input, screen display |
| Service | `services/` | Business rules, validation, logging |
| Repository | `repositories/` | SQL queries and database access |
| Model | `models/` | Data objects (`User`, `Product`, etc.) |
| Core | `core/` | Reusable helpers and exceptions |
| Jobs | `jobs/` | Scheduled background work |

---

## Prerequisites

- Python 3.9+
- Git (optional)

---

## Installation & Run

```bash
git clone https://github.com/salmanmasroor/inventory_system.git
cd inventory_system

python main.py
```

The database (`inventory.db`) and tables are created automatically on first run.

### Run tests

```bash
python -m unittest discover -s tests
```

### Run menu module directly

From the project root:

```bash
python -m cli.menu
```

> Do not run `cli/menu.py` directly — imports require the project root on the Python path.

---

## Usage

1. **Welcome screen** — Login, Register, or Exit
2. **After login** — Main menu: Products, Categories, Suppliers
3. **Products** — Add, view, search, update, or delete
4. **Navigation** — `N` = next page, `P` = previous page, `0` = back / logout
5. **Exit** — Press `0` on the main menu to log out; choose Exit on the welcome screen to close

---

## Database

SQLite file: `inventory.db` (path set in `config.py`)

| Table | Purpose |
|-------|---------|
| `users` | Registered accounts |
| `products` | Inventory items (name, price, quantity, sku) |
| `categories` | Product categories |
| `suppliers` | Supplier records |

Products can optionally link to a category and supplier via `category_id` and `supplier_id`.

---

## Configuration

| Setting | File | Default |
|---------|------|---------|
| Database path | `config.py` | `./inventory.db` |
| Log file | `config.py` | `./app.log` |
| Low stock threshold | `config.py` | `5` |
| Scheduler interval | `config.py` | `50` seconds |

---

## License

MIT
