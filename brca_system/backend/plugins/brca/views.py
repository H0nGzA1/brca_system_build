from django.shortcuts import render

# Create your views here.
from .models import Patient, Surgery, Diagnose, Medicaltest, Cure, Followup
from .serializers import PatientModelSerializer, PatientModelCreateUpdateSerializer, SurgeryModelSerializer, SurgeryModelCreateUpdateSerializer, DiagnoseModelSerializer, DiagnoseModelCreateUpdateSerializer, MedicaltestModelSerializer, MedicaltestModelCreateUpdateSerializer, CureModelSerializer, CureModelCreateUpdateSerializer, FollowupModelSerializer, FollowupModelCreateUpdateSerializer

from dvadmin.utils.viewset import CustomModelViewSet

class PatientModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Patient.objects.all()
    serializer_class = PatientModelSerializer
    create_serializer_class = PatientModelCreateUpdateSerializer
    update_serializer_class = PatientModelCreateUpdateSerializer
    filter_fields = ['name', 'medicalNumber', 'age', 'BMI', 'height', 'weight', 'idCard', 'doctor_name', 'remark', 'update_time']
    search_fields = ['name', 'medicalNumber', 'age', 'BMI', 'height', 'weight', 'idCard', 'doctor_name', 'remark', 'update_time']

class SurgeryModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Surgery.objects.all()
    serializer_class = SurgeryModelSerializer
    create_serializer_class = SurgeryModelCreateUpdateSerializer
    update_serializer_class = SurgeryModelCreateUpdateSerializer
    filter_fields = '__all__'
    search_fields = '__all__'

class DiagnoseModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseModelSerializer
    create_serializer_class = DiagnoseModelCreateUpdateSerializer
    update_serializer_class = DiagnoseModelCreateUpdateSerializer
    filter_fields = '__all__'
    search_fields = '__all__'

class MedicaltestModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例  
    destroy:删除
    """
    queryset = Medicaltest.objects.all()
    serializer_class = MedicaltestModelSerializer
    create_serializer_class = MedicaltestModelCreateUpdateSerializer
    update_serializer_class = MedicaltestModelCreateUpdateSerializer
    filter_fields = '__all__'
    search_fields = '__all__'

class CureModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Cure.objects.all()
    serializer_class = CureModelSerializer
    create_serializer_class = CureModelCreateUpdateSerializer
    update_serializer_class = CureModelCreateUpdateSerializer
    filter_fields = '__all__'
    search_fields = '__all__'

class FollowupModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Followup.objects.all()
    serializer_class = FollowupModelSerializer
    create_serializer_class = FollowupModelCreateUpdateSerializer
    update_serializer_class = FollowupModelCreateUpdateSerializer
    filter_fields = '__all__'
    search_fields = '__all__'

