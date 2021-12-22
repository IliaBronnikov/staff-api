from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = "департамент"
        verbose_name_plural = "департаменты"

    title = models.CharField("название департамента", max_length=200)

    def __str__(self):
        return self.title


class Staff(models.Model):
    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    full_name = models.CharField(max_length=200)
    photo = models.ImageField("логотип", default="default.jpg")
    position = models.CharField("должность", max_length=200)
    salary = models.IntegerField("зарплата")
    age = models.IntegerField("возраст")
    department = models.ForeignKey(
        Department,
        verbose_name="департамент",
        on_delete=models.CASCADE,
        related_name="staff",
    )

    def __str__(self):
        return self.full_name
