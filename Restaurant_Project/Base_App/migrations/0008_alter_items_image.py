

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0007_alter_items_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='media/items/'),
        ),
    ]
