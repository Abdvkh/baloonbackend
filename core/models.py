from django.db import models


class TyresGroup(models.Model):
    code = models.CharField("Наименование группы колес", max_length=50)
    brand = models.CharField("Бренд", max_length=50)
    
    def __str__(self):
        return self.code


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

    group = models.ForeignKey(TyresGroup, blank=True, on_delete=models.CASCADE)
    image = models.ImageField('Приложите фотографию колеса:', upload_to='tyres_photo/')
    type = models.CharField("Тип колеса", max_length=2, choices=TYRE_TYPES)
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
        return self.code + '|' + self.get_full_size

    @property
    def get_full_size(self):
        return self.width + '/' + self.height + 'R' + self.radius
    
    
class UserInfo(models.Model):
    full_name = models.CharField("Имя пользователя", max_length=50)
    address = models.CharField("Адрес пользователя", max_length=50)
    number = models.IntegerField("Номер пользователя")
    
    
class Feedback(models.Model):
    message = models.TextField("Сообщение")
    email = models.EmailField("e-mail", max_length=254)