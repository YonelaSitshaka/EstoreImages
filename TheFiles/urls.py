from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('ItemVisualCreate/', views.ItemVisualCreate, name="ItemVisualCreate"),
    path('EstorLogoCreate', views.EstorLogoCreate, name="EstorLogoCreate"),
    #path('FedList', views.FedList, name="FedList"),
    path('VisualDetail/<int:pk>/', views.VisualDetail, name="VisualDetail"),
    path('EstorLogoDetail/<int:pk>',views.EstorLogoDetail, name="EstorLogoDetail"),
   # path('FederationList',views.FederationList, name="FederationList"),
    #path('FederationUpdate/<int:pk>', views.FederationUpdate, name="FederationUpdate")
    
    
	# path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	#path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
