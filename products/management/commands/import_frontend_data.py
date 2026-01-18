import os
import re
from django.core.management.base import BaseCommand
from products.models import (
    Category, Mattress, Furniture, BeddingProduct, 
    SpecialProduct, CustomFurniture, HeavyDutyProduct, NewArrival
)
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import data from rjwoodessenz-web/src/data into specialized models'

    def handle(self, *args, **options):
        data_dir = r'd:\projects\RJmattress\rjwoodessenz-web\src\data'
        
        # Clear existing data to avoid duplicates/conflicts during redesign
        # Mattress.objects.all().delete()
        # Furniture.objects.all().delete()
        # ... and so on if needed

        # 1. Mattresses
        self.import_mattresses(os.path.join(data_dir, 'mattresses.ts'))
        
        # 2. Furniture
        self.import_furniture(os.path.join(data_dir, 'furniture.ts'))
        
        # 3. Bedding
        self.import_bedding(os.path.join(data_dir, 'bedding.ts'))
        
        # 4. Special Products
        self.import_special(os.path.join(data_dir, 'special-products.ts'))
        
        # 5. Custom Furniture
        self.import_custom(os.path.join(data_dir, 'custom-furniture.ts'))
        
        # 6. Heavy Duty
        self.import_heavy_duty(os.path.join(data_dir, 'heavy-duty.ts'))
        
        # 7. New Arrivals
        self.import_new_arrivals(os.path.join(data_dir, 'new-arrivals.ts'))

        self.stdout.write(self.style.SUCCESS('Successfully imported all specialized data'))

    def extract_objects(self, path):
        if not os.path.exists(path):
            return []
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'\[(.*)\];', content, re.DOTALL)
        if not match: return []
        return re.findall(r'\{(.*?)\}', match.group(1), re.DOTALL)

    def get_val(self, obj_str, field):
        pattern = rf'{field}:\s*([\'"].*?[\'"]|\d+\.?\d*|true|false|\[.*?\])'
        match = re.search(pattern, obj_str, re.DOTALL)
        if match:
            val = match.group(1).strip()
            if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
                return val[1:-1]
            return val
        return None

    def clean_price(self, val):
        if not val: return 0
        p = str(val).replace('₹', '').replace(',', '').strip()
        if p.replace('.', '').isdigit():
            return float(p)
        return 0

    def import_mattresses(self, path):
        for obj in self.extract_objects(path):
            Mattress.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'brand': self.get_val(obj, 'brand'),
                    'name': self.get_val(obj, 'name'),
                    'description': self.get_val(obj, 'description'),
                    'image': self.get_val(obj, 'image'),
                    'base_price': self.clean_price(self.get_val(obj, 'basePrice')),
                    'discount_percent': int(self.get_val(obj, 'discountParams') or 0),
                    'sizes': eval(self.get_val(obj, 'sizes') or '[]'),
                    'rating': float(self.get_val(obj, 'rating') or 0)
                }
            )

    def import_furniture(self, path):
        for obj in self.extract_objects(path):
            Furniture.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'room': self.get_val(obj, 'room'),
                    'furniture_type': self.get_val(obj, 'type'),
                    'name': self.get_val(obj, 'name'),
                    'brand': self.get_val(obj, 'brand'),
                    'material': self.get_val(obj, 'material'),
                    'size': self.get_val(obj, 'size'),
                    'price': self.clean_price(self.get_val(obj, 'price')),
                    'discount': int(self.get_val(obj, 'discount') or 0),
                    'customizable': self.get_val(obj, 'customizable') == 'true',
                    'image': self.get_val(obj, 'image'),
                    'badge': self.get_val(obj, 'badge') or '',
                    'delivery_time': self.get_val(obj, 'deliveryTime'),
                    'description': self.get_val(obj, 'description')
                }
            )

    def import_bedding(self, path):
        for obj in self.extract_objects(path):
            BeddingProduct.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'name': self.get_val(obj, 'name'),
                    'category': self.get_val(obj, 'category'),
                    'price': self.get_val(obj, 'price'),
                    'original_price': self.get_val(obj, 'originalPrice') or '',
                    'discount': self.get_val(obj, 'discount') or '',
                    'image': self.get_val(obj, 'image'),
                    'description': self.get_val(obj, 'description')
                }
            )

    def import_special(self, path):
        for obj in self.extract_objects(path):
            SpecialProduct.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'category': self.get_val(obj, 'category'),
                    'name': self.get_val(obj, 'name'),
                    'brand': self.get_val(obj, 'brand'),
                    'material': self.get_val(obj, 'material'),
                    'image': self.get_val(obj, 'image'),
                    'description': self.get_val(obj, 'description'),
                    'best_seller': self.get_val(obj, 'bestSeller') == 'true'
                }
            )

    def import_custom(self, path):
        for obj in self.extract_objects(path):
            CustomFurniture.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'title': self.get_val(obj, 'title'),
                    'description': self.get_val(obj, 'description'),
                    'icon': self.get_val(obj, 'icon'),
                    'image': self.get_val(obj, 'image'),
                    'tags': eval(self.get_val(obj, 'tags') or '[]')
                }
            )

    def import_heavy_duty(self, path):
        for obj in self.extract_objects(path):
            HeavyDutyProduct.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'name': self.get_val(obj, 'name'),
                    'category': self.get_val(obj, 'category'),
                    'price': self.get_val(obj, 'price'),
                    'image': self.get_val(obj, 'image')
                }
            )

    def import_new_arrivals(self, path):
        for obj in self.extract_objects(path):
            NewArrival.objects.update_or_create(
                uid=self.get_val(obj, 'id'),
                defaults={
                    'name': self.get_val(obj, 'name'),
                    'category': self.get_val(obj, 'category'),
                    'price': self.get_val(obj, 'price'),
                    'original_price': self.get_val(obj, 'originalPrice') or '',
                    'discount': self.get_val(obj, 'discount') or '',
                    'image': self.get_val(obj, 'image')
                }
            )
