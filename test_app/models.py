from django.db import models


class Doctor(models.Model):

	name = models.CharField(max_length=255, verbose_name=u"ФИО")
	specialty = models.CharField(max_length=255, verbose_name=u"Специальность")
	

	class Meta:
		verbose_name = 'Врач'
		verbose_name_plural = 'Врачи'

	def __str__(self):
		return '{0} - {1}'.format(self.name, self.specialty)
		 


class Application(models.Model):

	TIME = (
        (9, '9:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
        (14, '14:00'),
        (15, '15:00'),
        (16, '16:00'),
        (17, '17:00'),
    )

	name_pacient = models.CharField(max_length=255, verbose_name=u"ФИО")
	doctor = models.ForeignKey(Doctor, verbose_name=u"Врач")
	date_of_receipt = models.DateField(verbose_name=u"Дата приема")
	time_of_receipt = models.IntegerField(verbose_name='Время приема', choices=TIME)

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

	def __str__(self):
		return self.name_pacient