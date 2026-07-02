from repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, repository=None):
        self.repository = repository or CategoryRepository()

    def add_category(self, name):
        return self.repository.add(name)

    def view_categories(self):
        categories = self.repository.find_all()
        return [(category.id, category.name) for category in categories]

    def update_category(self, category_id, new_name):
        self.repository.update(category_id, new_name)

    def delete_category(self, category_id):
        return self.repository.delete(category_id)
