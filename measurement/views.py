from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorSerializer, MeasurementDetailSerializer, SensorDetailSerializer


class SensorListCreateView(ListCreateAPIView):
    """
    GET: получить список датчиков;
    POST: создать датчик.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    GET: получить информацию по конкретному датчику;
    PATCH: изменить датчик.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    """
    POST: добавить измерение.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer
