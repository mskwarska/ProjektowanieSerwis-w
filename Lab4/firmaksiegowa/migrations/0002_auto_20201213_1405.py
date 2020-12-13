# Generated by Django 3.1.2 on 2020-12-13 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firmaksiegowa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
            ],
        ),
        migrations.RenameModel(
            old_name='Documents',
            new_name='Document',
        ),
        migrations.AlterField(
            model_name='client',
            name='AccountId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firmaksiegowa.account'),
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]
