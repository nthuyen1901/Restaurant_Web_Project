

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0009_alter_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='items/'),
        ),
    ]
