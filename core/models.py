from django.db import models

class Tyre(models.Model):
    TYRE_TYPES = (
        ("Л", "Легковой"),
        ("Г", "Грузовой")
    )

    WIDTH = (
        ("275","275"),
        ("295", "295"),
        ("315", "315")
    )

    HEIGHT = (
        ("70", "70"),
        ("75", "75"),
        ("80", "80")
    )

    RADIUS = (
        ('22.5', '22.5'),
    )

    image = models.ImageField('Приложите фотографию колеса:', upload_to='tyres_photo/')
    type = models.CharField("Тип колеса", max_length=2, null=True, choices=TYRE_TYPES)
    code = models.CharField("Код протектора", max_length=10)
    title = models.CharField("Название", max_length=30)
    width = models.CharField('Ширина', max_length=5, choices=WIDTH)
    height = models.CharField('Высота', max_length=5, choices=HEIGHT)
    radius = models.CharField('Радиус', max_length=5, choices=RADIUS)
    speed_index = models.IntegerField('Индекс скорости')
    tread_depth = models.IntegerField('Глубина протектора')
    standard = models.FloatField('Какой-то стандарт')
    oa_dia = models.IntegerField("OA DIA")
    max_pressure = models.IntegerField('Максимальное давление(КРА/PSI)')
    certificate = models.CharField('Сертификат качества', max_length=5)
    distance = models.IntegerField("Преодолимая дистанция колёс")
    max_loading = models.IntegerField("Максимальная нагрузка")

    def __str__(self):
        return self.code

    def get_full_size(self):
        return self.width + '/' + self.height + 'R' + self.radius