from .models import Patient, Surgery, Diagnose, Medicaltest, Cure, Followup
from dvadmin.utils.serializers import CustomModelSerializer

class PatientModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Patient
        fields = "__all__"

class PatientModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Patient
        fields = '__all__'

###############################################################
class SurgeryModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Surgery
        fields = "__all__"

class SurgeryModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Surgery
        fields = '__all__'

###############################################################
class DiagnoseModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Diagnose
        fields = '__all__'

class DiagnoseModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Diagnose
        fields = '__all__'

###############################################################
class MedicaltestModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Medicaltest
        fields = '__all__'

class MedicaltestModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Medicaltest
        fields = '__all__'

###############################################################
class CureModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Cure
        fields = '__all__'

class CureModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Cure
        fields = '__all__'

###############################################################
class FollowupModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = Followup
        fields = '__all__'

class FollowupModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = Followup
        fields = '__all__'

