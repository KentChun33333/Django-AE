from django.conf.urls import url
from Version_1 import views
from Version_1 import video_parser_view




urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
	# r'^$'  http://127.0.0.1:8000/Version_1/

    url(r'^main_page/$', views.main_page, name='main_page'),
	url(r'^form_maker/(?P<question_id>[0-99]+)/$', views.form_maker, name='form_maker'),
	url(r'^echart_v1/$', views.echart_v1, name='echart_v1'),
	url(r'^inventory_scm_v1/$', views.inventory_scm_v1, name='inventory_scm_v1'),
	url(r'^fileupload/$', views.fileupload, name='fileupload'),
	# diabetes datathon
	url(r'^diabetes_datathon/$', views.diabetes_datathon, name='diabetes_datathon'),
	url(r'^demo/$', views.demo, name='demo'),
	url(r'^three3d_test/$', views.three3d_test, name='three3d_test'),


	url(r'^NotusemodelView/$', views.NotusemodelView, name='NotusemodelView'),

    url(r'^video_parser/$', video_parser_view.main, name='video_parser'),



	url(r'^FR_main_page/$', views.FR_main_page, name='FR_main_page'),
	url(r'^FR_main_page_2/$', views.FR_main_page_2, name='FR_main_page_2'),
	url(r'^FR_main_page_2_login/$', views.FR_main_page_2_login, name='FR_main_page_2_login'),

	url(r'^nightgarden/$',views.nightgarden, name = 'nightgarden'),
	url(r'^(?P<question_id>[0-9]+)/$',views.test_url, name='test_url'),

    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login_2,name = 'login_2'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    #url(r'^importAgencyCustomers/$',views.importAgencyCustomers,name = 'importAgencyCustomers'),
    #url(r'^E63F2Cv1/$', views. wireframev1,name='E63F2Cv1'),
	#url(r'^E63F2Cv2/$', views. wireframev2),
    #url(r'^E63F2C/$', views. wireframe),
	#url(r'^AlertMission/$', views. alert_v1, name='alert_v1'),


	]
