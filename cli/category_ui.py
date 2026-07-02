from services.category_service import CategoryService
import os


class CategoryUI:
    def __init__(self, app=None):
        self.service = CategoryService()
        self.app = app
    
    def _design(self, title):
        width = 50
        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("-" * width)
        print(title.center(width))
        print("=" * width)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
    
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
                self.clear_screen()
                self.add_category()
            elif choice == "2":
                self.clear_screen()
                self.view_categories()
            elif choice == "3":
                self.clear_screen()
                self.delete_category()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def add_category(self):
        self._design("ADD CATEGORY")
        name = input("Category name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if self.service.add_category(name):
            print(f"Category '{name}' added.")
            input("\nPress Enter to continue...")
        else:
            print(f"Category '{name}' already exists.")
            input("\nPress Enter to continue...")

    def view_categories(self):
        self._design("VIEW CATEGORIES")
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
        self._design("DELETE CATEGORY")
        cat_id = input("Category ID to delete: ").strip()
        if not cat_id.isdigit():
            print("Invalid ID.")
            return
        if self.service.delete_category(int(cat_id)):
            print("Category deleted.")
        else:
            print("Category not found.")
