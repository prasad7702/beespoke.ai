from django.db import models
import pandas as pd

class User(models.Model):
    customer_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, blank=True, null=True)
    preferred_category = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField()
    product_category = models.CharField(max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand_name} - {self.product_description}"

    class Meta:
        ordering = ['rank']

def load_catalog_from_excel(file_path):
    try:
        catalog_df = pd.read_excel(file_path)
        if set(['Product_id', 'Brand_name', 'Product_description', 'Price', 'Image_link', 'Product_category', 'Rank']).issubset(set(catalog_df.columns)):
            Product.objects.all().delete() 

            products = []
            for _, row in catalog_df.iterrows():
                product = Product(
                    product_id=row['Product_id'],
                    brand_name=row['Brand_name'],
                    product_description=row['Product_description'],
                    price=row['Price'],
                    image_link=row['Image_link'],
                    product_category=row['Product_category'],
                    rank=row['Rank']
                )
                products.append(product)

            Product.objects.bulk_create(products)
        else:
            print("Column names in Excel file do not match the expected fields.")
    except Exception as e:
        print(f"An error occurred: {e}")
