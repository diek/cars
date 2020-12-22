from django.urls import include, path
from rest_framework import routers

from . import api, views

router = routers.DefaultRouter()
router.register("Car", api.CarViewSet)
router.register("Make", api.MakeViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("car/Car/", views.CarListView.as_view(), name="car_Car_list"),
    path("car/Car/create/", views.CarCreateView.as_view(), name="car_Car_create"),
    path("car/Car/detail/<int:pk>/", views.CarDetailView.as_view(), name="car_Car_detail"),
    path("car/Car/update/<int:pk>/", views.CarUpdateView.as_view(), name="car_Car_update"),
    path("car/Make/", views.MakeListView.as_view(), name="car_Make_list"),
    path("car/Make/create/", views.MakeCreateView.as_view(), name="car_Make_create"),
    path("car/Make/detail/<int:pk>/", views.MakeDetailView.as_view(), name="car_Make_detail"),
    path("car/Make/update/<int:pk>/", views.MakeUpdateView.as_view(), name="car_Make_update")
]
