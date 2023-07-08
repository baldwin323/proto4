```python
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliate_name', models.CharField(max_length=200)),
                ('affiliate_link', models.URLField()),
                ('affiliate_commission', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
```