from repositories.supplier_repository import SupplierRepository


class SupplierService:
    def __init__(self, repository=None):
        self.repository = repository or SupplierRepository()

    def add_supplier(self, name, contact=""):
        self.repository.add(name, contact)
        return True

    def list_suppliers(self):
        return self.repository.find_all()

    def get_supplier(self, supplier_id):
        return self.repository.find_by_id(supplier_id)

    def update_supplier(self, supplier_id, name=None, contact=None):
        return self.repository.update(supplier_id, name=name, contact=contact)

    def delete_supplier(self, supplier_id):
        return self.repository.delete(supplier_id)
