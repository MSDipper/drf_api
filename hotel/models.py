from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    """ Категория """
    name = models.CharField(max_length=150, verbose_name='Имя')
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True)
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
      
    def __str__(self):
        return self.name        
               


class ImageRoom(models.Model):
    """ Изображение """
    image = models.ImageField(upload_to='images/', verbose_name='Изображения')
    
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return f'{self.image}'
    
    
class Hotel(models.Model):
    """ Отель """
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    create_at = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)
    quantity = models.IntegerField(verbose_name='Количество комнат', default=1)
    gps = models.CharField(max_length=250, verbose_name='Место положение')
    main_image = models.ImageField(upload_to='images/', verbose_name='Главное изображение', null=True)
    slug = models.SlugField(max_length=150, verbose_name='URL', unique=True, null=True)
    description = RichTextField(verbose_name='Описание')
    name_video = models.CharField(max_length=250, verbose_name='Заголовок к видео')
    video = models.FileField(verbose_name='Видео', upload_to='video/', max_length=100)
    category = models.ForeignKey(
        Category, 
        related_name='room',
        verbose_name='Категория',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    imageroom = models.ManyToManyField(
        ImageRoom, 
        related_name='room',
        verbose_name='Изображения'
        )
    
    
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
        
        
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """ Комментарии """
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    publish = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(verbose_name='Фото', upload_to='photo/', blank=True, null=True)
    message = models.TextField(max_length=500, verbose_name='Текст')
    hotel = models.ForeignKey(
        Hotel, 
        related_name='comment', 
        verbose_name='Комментарий',
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name="Родитель",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
        
    def __str__(self):
        return f'{self.name} - {self.email}'    


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.SmallIntegerField("Значение", default=0)


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]
        
        
    def __str__(self):
        return f'{self.value}'    
        
        
        
class Rating(models.Model):
    """ Рейтинг """
    ip = models.CharField("IP адрес", max_length=25)
    star = models.ForeignKey(RatingStar, verbose_name="Звезда", on_delete=models.CASCADE,)
    hotel = models.ForeignKey(
        Hotel, 
        verbose_name="Отель",
        on_delete=models.CASCADE, 
        related_name="rating"
        )

    def __str__(self):
        return f"{self.star}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"   
    

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    message = models.TextField("Сообщение", max_length=500)
    parent = models.ForeignKey(
        'self',
        verbose_name="Родитель",
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    hotel = models.ForeignKey(
        Hotel,
        related_name="review",
        verbose_name="Отель",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"