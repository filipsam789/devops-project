from django.test import TestCase
from .models import Category


class CategoryCreateTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Category1", active=True, description="cat1")

    def test_category_creation(self):
        category = Category.objects.get(name="Category1")
        self.assertEqual(category.name, "Category1")
        self.assertEqual(category.active, True)
        self.assertEqual(category.description, "cat1")


class CategoryUpdateTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category2", active=False, description="cat2")

    def test_category_update(self):
        self.category.name = "UpdatedCategory"
        self.category.active = False
        self.category.description = "UpdatedDescription"
        self.category.save()

        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.name, "UpdatedCategory")
        self.assertEqual(updated_category.active, True)
        self.assertEqual(updated_category.description, "UpdatedDescription")


class CategoryDeleteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Category3", active=False, description="cat3")

    def test_category_delete(self):
        category_id = self.category.id
        self.category.delete()

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=category_id)
