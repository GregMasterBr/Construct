# Generated by Django 4.1 on 2022-09-13 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('-created_at',), 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='produtos')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]