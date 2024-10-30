from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView, CarCreateView,
    CarUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturers/update/<int:pk>/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturers/delete/<int:pk>/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-list"
    ),

    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/delete/", CarDetailView.as_view(), name="car-delete"),

    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
