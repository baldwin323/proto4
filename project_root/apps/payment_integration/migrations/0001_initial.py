```python
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey('auth.User', on_delete=models.CASCADE)),
                ('payment_method', models.CharField(max_length=20)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('transaction_id', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```