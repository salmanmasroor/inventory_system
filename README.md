# Smart Inventory Management System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/salmanmasroor/inventory_system)
[![GitHub Stars](https://img.shields.io/github/stars/salmanmasroor/inventory_system?style=social)](https://github.com/salmanmasroor/inventory_system)

A **command-line inventory management application** built with Python. It provides secure user authentication, full product lifecycle management (CRUD), search with pagination, SKU tracking, input validation, and structured logging — designed with a clean separation between UI, service, and data layers.

> **Note:** This project uses **SQLite** for local, zero-configuration persistence. Tables are created automatically on first run — no separate SQL import is required.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **User Authentication** | Secure registration and login with email validation and password hashing (SHA-256). |
| **Product Management (CRUD)** | Add, view, update, and delete products through an interactive CLI menu. |
| **Search** | Find products by **ID** or **name** (case-insensitive name matching). |
| **SKU Management** | Each product is assigned a unique alphanumeric SKU at creation time. |
| **Stock Tracking** | Quantity is stored per product; low-stock monitoring is available via the scheduler module. |
| **Pagination** | View and search results are paginated for readability (`N` = Next, `P` = Previous). |
| **Input Validation** | Enforces alphabetic names, alphanumeric SKUs, minimum password length, and numeric price/quantity checks. |
| **Structured Logging** | All inventory mutations are logged to `app.log` for audit and debugging. |
| **Modular Architecture** | Separated into `Auth`, `Inventory`, `models`, and shared utilities for maintainability. |
| **Navigation** | Press `0` on Login, Registration, or Main Menu screens to return to the welcome page. |

---

## 🛠 Tech Stack

### Programming Language
- **Python 3.9+** — Core application logic and CLI interface

### Database
- **SQLite 3** — Lightweight, file-based relational database (`inventory.db`)

### Libraries / Packages
| Package | Purpose |
|---------|---------|
| `sqlite3` *(stdlib)* | Database connectivity and queries |
| `hashlib` *(stdlib)* | Password hashing (SHA-256) |
| `getpass` *(stdlib)* | Secure password input (hidden typing) |
| `logging` *(stdlib)* | Application and inventory event logging |
| `threading` *(stdlib)* | Background low-stock scheduler |
| `smtplib` *(stdlib)* | Email alert scaffolding (optional) |

> **No third-party pip packages are required.** All dependencies are part of the Python standard library.

### Development Tools
- **Git** — Version control
- **VS Code / Cursor** — Recommended IDE
- **DB Browser for SQLite** *(optional)* — Visual database inspection
- **Terminal / PowerShell / Bash** — Running the CLI application

---

## 📁 Project Structure

```
inventory_system/
│
├── Auth/
│   ├── authentication.py       # Auth service: register, login, email check, password hashing
│   └── authentication_ui.py    # Login & registration CLI menus and validation
│
├── Inventory/
│   ├── inventory_service.py    # Inventory data layer: CRUD, search, low-stock queries
│   └── inventory_ui.py         # Product menus, pagination, and user-facing inventory flows
│
├── models/
│   ├── __init__.py
│   ├── user.py                 # User domain model
│   └── product.py              # Product domain model
│
├── main.py                     # Application entry point and main navigation loop
├── database.py                 # SQLite connection, schema creation, and migrations
├── utils.py                    # Shared input helpers (_get_int, _get_float, _get_text)
├── logger.py                   # Logging configuration (writes to app.log)
├── schedular.py                # Background low-stock monitoring thread
├── send_email.py               # SMTP email alert utility (optional / configurable)
│
├── inventory.db                # SQLite database file (auto-generated, gitignored)
├── app.log                     # Application log file (auto-generated, gitignored)
├── .gitignore
└── README.md
```

### Folder Purposes

| Path | Responsibility |
|------|----------------|
| `Auth/` | Everything related to user identity — registration, login, and auth UI. |
| `Inventory/` | Product inventory business logic and CLI presentation layer. |
| `models/` | Plain Python classes representing `User` and `Product` entities. |
| Root files | App bootstrap, database setup, logging, utilities, and scheduling. |

---

## 📋 Prerequisites

Before you begin, ensure the following are installed:

| Requirement | Version / Details |
|-------------|-------------------|
| **Python** | 3.9 or higher |
| **SQLite** | 3.x *(bundled with Python — no separate install needed)* |
| **Git** | Latest stable version |
| **Terminal** | PowerShell (Windows), Bash (Linux/macOS) |
| **IDE** *(optional)* | VS Code, Cursor, or PyCharm |
| **DBeaver** *(optional)* | For inspecting `inventory.db` visually |

> **Tip:** Verify your Python installation:
> ```bash
> python --version
> ```

---

## 🗄 Database Setup (Step-by-Step)

This project uses **SQLite**. The database file and tables are created automatically — follow these steps to get started.

### Step 1 — Clone and navigate to the project

```bash
git clone https://github.com/salmanmasroor/inventory_system.git
cd inventory_system
```

### Step 2 — Run the application once (auto-creates the database)

```bash
python database.py
```

Running `database.py` directly executes `create_table()` and `user_table()`, which creates `inventory.db` in the project root with the required schema.

> **Alternative:** Simply run `python main.py` — importing `database.py` triggers the same schema initialization.

### Step 3 — Verify the database was created

```bash
# Windows (PowerShell)
dir inventory.db

# Linux / macOS
ls -la inventory.db
```

You should see `inventory.db` in the project root.

### Step 4 — Inspect tables *(optional)*

Open `inventory.db` in **DB Browser for SQLite** or use the CLI:

```bash
sqlite3 inventory.db

# Inside the SQLite shell:
.tables
.schema users
.schema products
.quit
```

### Step 5 — Configure the database path *(optional)*

The database path is defined in `database.py`:

```python
DB_PATH = Path(__file__).resolve().parent / "inventory.db"
```

To use a custom location, update `DB_PATH` accordingly.

> **Important:** `inventory.db` is listed in `.gitignore` and will not be committed. Each developer maintains their own local database.

---

## 🚀 Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/salmanmasroor/inventory_system.git
cd inventory_system
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv

# Linux / macOS
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

### 4. Install dependencies

This project uses only the Python standard library — no `pip install` is required.

```bash
# Optional: verify Python can import all modules
python -c "from main import Application; print('Setup OK')"
```

> **Tip:** If you add third-party packages in the future, create a `requirements.txt` and run:
> ```bash
> pip install -r requirements.txt
> ```

### 5. Configure environment variables *(optional)*

No `.env` file is required for basic usage. For email alerts, configure credentials in `send_email.py`:

```python
server.login("your-email@gmail.com", "your-app-password")
server.sendmail("your-email@gmail.com", "recipient@example.com", text)
```

### 6. Run the application

```bash
python main.py
```

You should see the **Smart Inventory Management** welcome screen with Login, Register, and Exit options.

---

## 🔐 Authentication Module

### Authentication Flow

```
Welcome Menu
    ├── Register  →  Validate inputs  →  Hash password  →  Save to DB
    ├── Login     →  Verify email exists  →  Hash & compare  →  Grant access
    └── Exit
```

### User Registration

1. User enters **First Name**, **Last Name**, **Email**, and **Password**.
2. Validation rules are enforced:
   - First name is required and must be alphabetic.
   - Last name (if provided) must be alphabetic.
   - Email must contain `@` and must not already exist.
   - Password must be at least **8 characters**.
3. Password is hashed with **SHA-256** before storage.
4. User record is inserted into the `users` table.

### Login

1. User enters email and password.
2. System checks if the email exists in the database.
3. Password is hashed and compared against the stored hash.
4. On success, the user session is established and the inventory main menu is displayed.
5. Press **`0`** at any time to return to the welcome page.

### Password Hashing

Passwords are **never stored in plain text**. The `Authentication` service uses:

```python
hashlib.sha256(password.encode()).hexdigest()
```

### Roles and Permissions

> **Current status:** The application supports a **single user role**. All authenticated users have full access to inventory operations. Role-based access control (Admin/User) is planned as a future enhancement.

### Logout

- Press **`0`** on the **Main Menu** (after login) to log out and return to the welcome screen.
- The session is cleared by setting `current_user = None`.

---

## 📦 Inventory Module

### Add Product

- Capture **Product Name**, **SKU**, **Quantity**, and **Price**.
- Validates alphabetic product names and alphanumeric SKUs.
- Persists the product via `Inventory.add_product()`.

### Update Product

- Enter a product **ID** to locate the record.
- Choose the field to update: **Name**, **Price**, **Quantity**, or **SKU**.
- Changes are written to the database and logged.

### Delete Product

- Enter a product **ID**.
- System verifies the product exists before deletion.
- Record is permanently removed from the `products` table.

### View Products

- Displays all products in a formatted table.
- Supports **pagination** (4 items per page by default).
- Navigation: `N` (Next), `P` (Previous), `0` (Back).

### Search Products

- Search by **product ID** (integer) or **product name** (string).
- Results are paginated (2 items per page by default).
- Displays a "No Products Found" message when no matches exist.

### Stock Management

- Each product stores a `quantity` field representing current stock level.
- `low_stock_products()` queries products with quantity below 5.
- A background scheduler in `schedular.py` periodically checks for low stock *(email alerts are optional and currently commented out)*.

### SKU Management

- SKU is a required alphanumeric identifier assigned at product creation.
- SKU can be updated independently via the Update Product flow.

### Pagination

| Screen | Default Page Size |
|--------|-------------------|
| View Products | 4 |
| Search Products | 2 |

### Validation

| Field | Rule |
|-------|------|
| Product Name | Alphabetic characters only, cannot be empty |
| SKU | Alphanumeric only, cannot be empty |
| Quantity | Positive integer (`_get_int`) |
| Price | Positive float, minimum 0.01 (`_get_float`) |
| Email | Must contain `@`, must be unique |
| Password | Minimum 8 characters |

---

## 🗃 Database Schema

### `users` Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique user identifier |
| `first_name` | TEXT | NOT NULL, max 50 chars | User's first name |
| `last_name` | TEXT | NULL, max 50 chars | User's last name |
| `email` | TEXT | UNIQUE, NOT NULL | Login email address |
| `password` | TEXT | NOT NULL | SHA-256 hashed password |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation time |

### `products` Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique product identifier |
| `sku` | TEXT | NOT NULL | Stock Keeping Unit code |
| `name` | TEXT | NOT NULL | Product name |
| `price` | REAL | NOT NULL | Unit price |
| `quantity` | INTEGER | NOT NULL | Current stock quantity |

### Relationships

```
users (1) ──── manages ────> (N) products   [logical — no FK enforced yet]
```

> **Note:** There is currently **no foreign key** between `users` and `products`. Products are globally accessible to all authenticated users. A `user_id` foreign key on `products` is recommended for multi-tenant support in future versions.

### Entity-Relationship Diagram

```
┌─────────────────────┐          ┌──────────────────────┐
│       users         │          │      products        │
├─────────────────────┤          ├──────────────────────┤
│ id          PK      │          │ id          PK       │
│ first_name          │          │ sku                  │
│ last_name           │          │ name                 │
│ email       UNIQUE  │          │ price                │
│ password            │          │ quantity             │
│ created_at          │          └──────────────────────┘
└─────────────────────┘
```

---

## 📸 Screenshots

> Place your screenshots in the `docs/screenshots/` directory before publishing.

| Screen | File Path |
|--------|-----------|
| Welcome Menu | `docs/screenshots/01-welcome-menu.png` |
| Login Screen | `docs/screenshots/02-login.png` |
| Registration Screen | `docs/screenshots/03-registration.png` |
| Main Menu (Dashboard) | `docs/screenshots/04-main-menu.png` |
| Product List (Paginated) | `docs/screenshots/05-view-products.png` |
| Add Product | `docs/screenshots/06-add-product.png` |
| Search Results | `docs/screenshots/07-search-products.png` |

### Example embed syntax (after adding images):

```markdown
![Welcome Menu](docs/screenshots/01-welcome-menu.png)
```

---

## ⚙️ Configuration

### Database Configuration

| Setting | Location | Default |
|---------|----------|---------|
| Database file path | `database.py` → `DB_PATH` | `./inventory.db` |
| Auto schema creation | `database.py` → `create_table()`, `user_table()` | On import |

### Logging Configuration

| Setting | Location | Default |
|---------|----------|---------|
| Log file | `logger.py` → `LOG_PATH` | `./app.log` |
| Log level | `logger.py` | `DEBUG` |
| Log format | `logger.py` | `%(asctime)s - %(levelname)s - %(message)s` |

### Email Alerts *(Optional)*

| Setting | Location | Description |
|---------|----------|-------------|
| SMTP server | `send_email.py` | `smtp.gmail.com:587` |
| Credentials | `send_email.py` | Gmail address and app password |
| Scheduler interval | `schedular.py` | 50 seconds (low-stock check) |

### Application Settings

| Setting | Location | Description |
|---------|----------|-------------|
| View page size | `inventory_ui.py` → `view_product(page_size=4)` | Products per page |
| Search page size | `inventory_ui.py` → `search_product(page_size=2)` | Search results per page |
| Low stock threshold | `inventory_service.py` → `low_stock_products()` | Quantity < 5 |

> **Warning:** Never commit real email credentials or production database files. Keep sensitive values out of version control.

---

## 📖 Usage

Follow these steps after installation:

### Step 1 — Launch the application

```bash
python main.py
```

### Step 2 — Register a new account

1. Select **`2`** (Register) from the welcome menu.
2. Fill in your details and press **`1`** to register.
3. Press **`0`** to go back without registering.

### Step 3 — Log in

1. Select **`1`** (Login) from the welcome menu.
2. Enter your registered email and password.
3. Press **`1`** to log in, or **`0`** to return.

### Step 4 — Manage products

1. From the **Main Menu**, select **`1`** (Products).
2. Choose an action:
   - `1` — Add Product
   - `2` — View Products
   - `3` — Search Product
   - `4` — Update Product
   - `5` — Delete Product
   - `0` — Back to Main Menu
3. Use **`N`** / **`P`** to navigate paginated lists.
4. Press **`0`** to go back at any sub-screen.

### Step 5 — Log out

- From the **Main Menu**, press **`0`** to log out and return to the welcome screen.

### Step 6 — Exit the application

- From the **Welcome Menu**, select **`3`** (Exit).

---
