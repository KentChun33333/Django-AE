from django.conf.urls import patterns, url
from Version_1 import views


		
urlpatterns = patterns('',
    url(r'^$', views.login_user, name='login_user'),
	# r'^$'  http://127.0.0.1:8000/Version_1/

    url(r'^main_page/$', views.main_page, name='main_page'),
	url(r'^form_maker/$', views.form_maker, name='form_maker'),
	url(r'^echart_v1/$', views.echart_v1, name='echart_v1'),
	url(r'^inventory_scm_v1/$', views.inventory_scm_v1, name='inventory_scm_v1'),
	url(r'^FR_main_page/$', views.FR_main_page, name='FR_main_page'),
	url(r'^nightgarden/$',views.nightgarden, name = 'nightgarden'),
    #url(r'^E63F2Cv1/$', views. wireframev1,name='E63F2Cv1'),
	#url(r'^E63F2Cv2/$', views. wireframev2),
    #url(r'^E63F2C/$', views. wireframe),
	#url(r'^AlertMission/$', views. alert_v1, name='alert_v1'),
	
	
	)