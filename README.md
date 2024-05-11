# Library Management System (LibSys)

LibSys is a command-line interface (CLI) based application designed to manage library operations efficiently. This system allows administrators to perform various tasks such as adding books, listing books, managing users, and more. Regular users can browse books and check them out.

## Features

### Admin Features
- **Add New Book**: Enter details for a new book to add to the library.
- **List Books**: Display a list of all books in the library.
- **Add New User**: Register a new library user.
- **Add New Admin**: Register a new library administrator.
- **Checkout Book**: Process the checkout of a book for a user.
- **Export Database**: Export the current state of the library database to a JSON file.
- **Exit**: Exit the admin menu.

### User Features
- **List Books**: Display a list of all books available in the library.
- **Checkout Book**: Checkout a book from the library.
- **Exit**: Exit the user menu.

## Prerequisites

- Python 3.8 or higher
- Libraries: SQLAlchemy, argparse, pyfiglet

## Installation

1. **Clone the Repository**:
   ```
   git clone https://yourrepository.com/Redesigning-Poor-Code.git
   cd Redesigning-Poor-Code
   ```

2. **Set up a Python Environment** (Optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```
   pip install -r requirements.txt
   ```

## Usage

Start the program by navigating to the project directory and running:

```
python main.py
```

### Arguments

- `--mode`: Launch the program in either Admin (0) or User (1) mode. Default is User mode.
  - Example: `python main.py --mode 0`
- `--username`: Username for admin login (required for Admin mode).
  - Example: `python main.py --mode 0 --username admin`
- `--password`: Password for admin login (required for Admin mode).
  - Example: `python main.py --mode 0 --username admin --password 123456`

### Default Admin Credentials
- **Username**: `123456`
- **Password**: `123456`

