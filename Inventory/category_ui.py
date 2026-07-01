try:
    from .category_service import CategoryService
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from Inventory.category_service import CategoryService


class CategoryUI:
    def __init__(self, app=None):
        self.service = CategoryService()
        self.app = app

    def display_menu(self):
        while True:
            if self.app is not None:
                self.app.clear_screen()

            print("=" * 50)
            print("SMART INVENTORY MANAGEMENT".center(50))
            print("=" * 50)
            print("CATEGORY MENU".center(50))
            print("-" * 50)
            print("1. Add Category")
            print("2. View Categories")
            print("3. Delete Category")
            print("-" * 50)
            print("0. Back")
            print("=" * 50)

            choice = input("Choose: ").strip()

            if choice == "1":
                self.add_category()
            elif choice == "2":
                self.view_categories()
            elif choice == "3":
                self.delete_category()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def add_category(self):
        name = input("Category name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if self.service.add_category(name):
            print(f"Category '{name}' added.")
        else:
            print(f"Category '{name}' already exists.")

    def view_categories(self):
        categories = self.service.view_categories()
        if not categories:
            print("No categories found.")
            return

        print("-" * 50)
        for cat_id, name in categories:
            print(f"{cat_id}. {name}")
        print("-" * 50)

        input("Press Enter to continue...")

    def delete_category(self):
        self.view_categories()
        cat_id = input("Category ID to delete: ").strip()
        if not cat_id.isdigit():
            print("Invalid ID.")
            return
        if self.service.delete_category(int(cat_id)):
            print("Category deleted.")
        else:
            print("Category not found.")


if __name__ == "__main__":
    ui = CategoryUI()
    ui.display_menu()
