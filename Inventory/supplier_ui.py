try:
    from .supplier_service import SupplierService
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from Inventory.supplier_service import SupplierService


class SupplierUI:
    def __init__(self, app=None):
        self.service = SupplierService()
        self.app = app

    def display_menu(self):
        while True:
            if self.app is not None:
                self.app.clear_screen()

            print("=" * 50)
            print("SMART INVENTORY MANAGEMENT".center(50))
            print("=" * 50)
            print("SUPPLIER MENU".center(50))
            print("-" * 50)
            print("1. Add Supplier")
            print("2. View Suppliers")
            print("3. Update Supplier")
            print("4. Delete Supplier")
            print("-" * 50)
            print("0. Back")
            print("=" * 50)

            choice = input("Choose: ").strip()

            if choice == "1":
                self.add_supplier()
            elif choice == "2":
                self.view_suppliers()
            elif choice == "3":
                self.update_supplier()
            elif choice == "4":
                self.delete_supplier()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def add_supplier(self):
        name = input("Supplier name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        contact = input("Contact (phone/email): ").strip()
        self.service.add_supplier(name, contact)
        print(f"Supplier '{name}' added.")
        input("\nPress Enter to continue...")

    def view_suppliers(self):
        suppliers = self.service.list_suppliers()
        if not suppliers:
            print("No suppliers found.")
            return

        print("-" * 50)
        for supplier in suppliers:
            contact = supplier.contact or "-"
            print(f"{supplier.id}. {supplier.name} - {contact}")
        print("-" * 50)
        input("Press Enter to continue...")

    def update_supplier(self):
        self.view_suppliers()
        sup_id = input("Supplier ID to update: ").strip()
        if not sup_id.isdigit():
            print("Invalid ID.")
            return

        supplier = self.service.get_supplier(int(sup_id))
        if supplier is None:
            print("Supplier not found.")
            return

        name = input(f"New name (blank to keep '{supplier.name}'): ").strip()
        contact = input(
            f"New contact (blank to keep '{supplier.contact or '-'}'): "
        ).strip()

        self.service.update_supplier(
            int(sup_id),
            name=name if name else None,
            contact=contact if contact else None,
        )
        print("Supplier updated.")
        input("\nPress Enter to continue...")

    def delete_supplier(self):
        self.view_suppliers()
        sup_id = input("Supplier ID to delete: ").strip()
        if not sup_id.isdigit():
            print("Invalid ID.")
            return
        if self.service.delete_supplier(int(sup_id)):
            print("Supplier deleted.")
        else:
            print("Supplier not found.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    ui = SupplierUI()
    ui.display_menu()
