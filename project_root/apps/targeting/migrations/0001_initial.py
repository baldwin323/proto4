```python
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Targeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_of_interest', models.CharField(max_length=200)),
                ('demographics', models.CharField(max_length=200)),
                ('deployment_area', models.CharField(max_length=200)),
            ],
        ),
    ]
```