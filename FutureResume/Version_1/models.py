from django.db import models

# Create your models here.



class Owners(models.Model):
	name = models.CharField(max_length=100)
	fox_id = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Jobs(models.Model):

	job_project = models.CharField(max_length=100)
	job_function_item = models.CharField(max_length=100)

	job_owner = models.ForeignKey(Owners)
	
	job_description = models.CharField(max_length=1000)
	job_open_time = models.DateTimeField()
	job_goal_time = models.DateTimeField(null=True)
	job_close_time = models.DateTimeField(null=True)

	def __unicode__(self):
		return self.job_project, self.job_function_item, self.job_description





# a = Owners.objects.create(name='kent',fox_id='830457')
# a.save()
#from datetime impot datetime
#b = Jobs.objects.create(job_project = 'Component-DPPM',	job_function_item = 'DPPM count', job_owner = Owners.objects.get(pk=1),job_description = 'DPPM by sku & lot-code', job_open_time=datetime.now())

#Jobs.objects.values()[0]['id']
  



