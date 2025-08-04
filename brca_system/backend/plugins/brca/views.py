from django.shortcuts import render
from django.db.models import Count, Q, Sum
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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

    @action(detail=False, methods=['get'])
    def dashboard_patient_count(self, request):
        """获取患者总数统计"""
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        
        total_patients = Patient.objects.count()
        today_new = Patient.objects.filter(create_time__date=today).count()
        week_new = Patient.objects.filter(create_time__date__gte=week_ago).count()
        month_new = Patient.objects.filter(create_time__date__gte=month_ago).count()
        
        data = {
            "total_patients": total_patients,
            "today_new": today_new,
            "week_new": week_new,
            "month_new": month_new
        }
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_usage_statistics(self, request):
        """获取系统使用量统计"""
        period = request.query_params.get('period', 'week')
        
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        year_ago = today - timedelta(days=365)
        
        # 这里使用患者创建数量作为使用量统计
        week_usage = Patient.objects.filter(create_time__date__gte=week_ago).count()
        month_usage = Patient.objects.filter(create_time__date__gte=month_ago).count()
        year_usage = Patient.objects.filter(create_time__date__gte=year_ago).count()
        
        # 最近7天的每日使用量
        daily_usage = []
        for i in range(7):
            date = today - timedelta(days=i)
            count = Patient.objects.filter(create_time__date=date).count()
            daily_usage.insert(0, count)
        
        data = {
            "week_usage": week_usage,
            "month_usage": month_usage,
            "year_usage": year_usage,
            "daily_usage": daily_usage
        }
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_patient_geo_distribution(self, request):
        """获取患者地理分布数据"""
        # 由于当前模型中没有地理字段，这里返回模拟数据
        # 实际项目中需要在Patient模型中添加province和city字段
        
        data = [
            {"name": "北京", "value": 156, "percentage": 12.5},
            {"name": "上海", "value": 234, "percentage": 18.7},
            {"name": "广东", "value": 345, "percentage": 27.6},
            {"name": "江苏", "value": 189, "percentage": 15.1},
            {"name": "浙江", "value": 167, "percentage": 13.4},
            {"name": "四川", "value": 98, "percentage": 7.8},
            {"name": "湖北", "value": 76, "percentage": 6.1},
            {"name": "山东", "value": 65, "percentage": 5.2},
            {"name": "河南", "value": 54, "percentage": 4.3},
            {"name": "其他", "value": 6, "percentage": 0.5}
        ]
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_tumor_type_distribution(self, request):
        """获取肿瘤类型分布数据"""
        # 从诊断记录中获取肿瘤类型分布
        tumor_types = Diagnose.objects.values('pathology_sub').annotate(
            count=Count('id')
        ).filter(pathology_sub__isnull=False).exclude(pathology_sub='')
        
        total = sum(item['count'] for item in tumor_types)
        
        data = []
        for item in tumor_types:
            percentage = round((item['count'] / total * 100), 1) if total > 0 else 0
            data.append({
                "name": item['pathology_sub'],
                "value": item['count'],
                "percentage": percentage,
                "count": item['count']
            })
        
        # 如果没有数据，返回模拟数据
        if not data:
            data = [
                {"name": "浸润性导管癌", "value": 562, "percentage": 45.0, "count": 562},
                {"name": "浸润性小叶癌", "value": 312, "percentage": 25.0, "count": 312},
                {"name": "导管原位癌", "value": 187, "percentage": 15.0, "count": 187},
                {"name": "小叶原位癌", "value": 125, "percentage": 10.0, "count": 125},
                {"name": "其他", "value": 64, "percentage": 5.0, "count": 64}
            ]
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_patient_age_distribution(self, request):
        """获取患者年龄分布数据"""
        age_groups = [
            {"min": 20, "max": 30, "label": "20-30岁"},
            {"min": 31, "max": 40, "label": "31-40岁"},
            {"min": 41, "max": 50, "label": "41-50岁"},
            {"min": 51, "max": 60, "label": "51-60岁"},
            {"min": 61, "max": 70, "label": "61-70岁"},
            {"min": 71, "max": 80, "label": "71-80岁"},
            {"min": 81, "max": 999, "label": "80岁以上"}
        ]
        
        total_patients = Patient.objects.filter(age__isnull=False).count()
        data = []
        
        for group in age_groups:
            if group['max'] == 999:
                count = Patient.objects.filter(age__gte=group['min']).count()
            else:
                count = Patient.objects.filter(age__gte=group['min'], age__lte=group['max']).count()
            
            percentage = round((count / total_patients * 100), 1) if total_patients > 0 else 0
            data.append({
                "age_group": group['label'],
                "count": count,
                "percentage": percentage
            })
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_patient_gender_distribution(self, request):
        """获取患者性别分布数据"""
        gender_stats = Patient.objects.values('gender').annotate(count=Count('id'))
        total_patients = Patient.objects.count()
        
        data = []
        for stat in gender_stats:
            gender_name = "未知"
            if stat['gender'] == 1:
                gender_name = "男性"
            elif stat['gender'] == 2:
                gender_name = "女性"
            
            percentage = round((stat['count'] / total_patients * 100), 1) if total_patients > 0 else 0
            data.append({
                "name": gender_name,
                "value": stat['count'],
                "percentage": percentage,
                "count": stat['count']
            })
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_her2_distribution(self, request):
        """获取HER2阴阳性分布数据"""
        her2_stats = Cure.objects.values('HER2_status').annotate(count=Count('id'))
        total_records = Cure.objects.count()
        
        data = []
        for stat in her2_stats:
            her2_name = "未知"
            if stat['HER2_status'] == 1:
                her2_name = "HER2阳性"
            elif stat['HER2_status'] == 2:
                her2_name = "HER2阴性"
            
            percentage = round((stat['count'] / total_records * 100), 1) if total_records > 0 else 0
            data.append({
                "name": her2_name,
                "value": stat['count'],
                "percentage": percentage,
                "count": stat['count']
            })
        
        # 如果没有数据，返回模拟数据
        if not data:
            data = [
                {"name": "HER2阳性", "value": 437, "percentage": 35.0, "count": 437},
                {"name": "HER2阴性", "value": 813, "percentage": 65.0, "count": 813}
            ]
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_login_heatmap(self, request):
        """获取登录使用热图数据"""
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        user_id = request.query_params.get('user_id')
        
        # 这里使用患者创建时间作为登录热图数据
        # 实际项目中应该使用真实的登录日志表
        
        if start_date and end_date:
            start = datetime.strptime(start_date, '%Y-%m-%d').date()
            end = datetime.strptime(end_date, '%Y-%m-%d').date()
            queryset = Patient.objects.filter(create_time__date__range=[start, end])
        else:
            # 默认返回最近30天的数据
            end = timezone.now().date()
            start = end - timedelta(days=30)
            queryset = Patient.objects.filter(create_time__date__range=[start, end])
        
        data = []
        current_date = start
        while current_date <= end:
            count = queryset.filter(create_time__date=current_date).count()
            data.append({
                "date": current_date.strftime('%Y-%m-%d'),
                "value": count,
                "count": count
            })
            current_date += timedelta(days=1)
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

    @action(detail=False, methods=['get'])
    def dashboard_all_data(self, request):
        """获取仪表盘所有数据（一次性获取）"""
        # 获取患者统计
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        year_ago = today - timedelta(days=365)
        
        total_patients = Patient.objects.count()
        week_usage = Patient.objects.filter(create_time__date__gte=week_ago).count()
        month_usage = Patient.objects.filter(create_time__date__gte=month_ago).count()
        year_usage = Patient.objects.filter(create_time__date__gte=year_ago).count()
        
        # 获取地理分布（模拟数据）
        geo_distribution = [
            {"name": "北京", "value": 156},
            {"name": "上海", "value": 234},
            {"name": "广东", "value": 345},
            {"name": "江苏", "value": 189},
            {"name": "浙江", "value": 167}
        ]
        
        # 获取肿瘤类型分布
        tumor_types = Diagnose.objects.values('pathology_sub').annotate(
            count=Count('id')
        ).filter(pathology_sub__isnull=False).exclude(pathology_sub='')
        
        tumor_type_distribution = []
        for item in tumor_types:
            tumor_type_distribution.append({
                "name": item['pathology_sub'],
                "value": item['count']
            })
        
        # 获取年龄分布
        age_groups = [
            {"min": 20, "max": 30, "label": "20-30岁"},
            {"min": 31, "max": 40, "label": "31-40岁"},
            {"min": 41, "max": 50, "label": "41-50岁"},
            {"min": 51, "max": 60, "label": "51-60岁"},
            {"min": 61, "max": 70, "label": "61-70岁"},
            {"min": 71, "max": 80, "label": "71-80岁"},
            {"min": 81, "max": 999, "label": "80岁以上"}
        ]
        
        age_distribution = []
        for group in age_groups:
            if group['max'] == 999:
                count = Patient.objects.filter(age__gte=group['min']).count()
            else:
                count = Patient.objects.filter(age__gte=group['min'], age__lte=group['max']).count()
            
            age_distribution.append({
                "age_group": group['label'],
                "count": count
            })
        
        # 获取性别分布
        gender_stats = Patient.objects.values('gender').annotate(count=Count('id'))
        gender_distribution = []
        for stat in gender_stats:
            gender_name = "未知"
            if stat['gender'] == 1:
                gender_name = "男性"
            elif stat['gender'] == 2:
                gender_name = "女性"
            
            gender_distribution.append({
                "name": gender_name,
                "value": stat['count']
            })
        
        # 获取HER2分布
        her2_stats = Cure.objects.values('HER2_status').annotate(count=Count('id'))
        her2_distribution = []
        for stat in her2_stats:
            her2_name = "未知"
            if stat['HER2_status'] == 1:
                her2_name = "HER2阳性"
            elif stat['HER2_status'] == 2:
                her2_name = "HER2阴性"
            
            her2_distribution.append({
                "name": her2_name,
                "value": stat['count']
            })
        
        # 获取登录热图数据
        end = timezone.now().date()
        start = end - timedelta(days=30)
        login_heatmap = []
        current_date = start
        while current_date <= end:
            count = Patient.objects.filter(create_time__date=current_date).count()
            login_heatmap.append({
                "date": current_date.strftime('%Y-%m-%d'),
                "value": count
            })
            current_date += timedelta(days=1)
        
        data = {
            "statistics": {
                "total_patients": total_patients,
                "week_usage": week_usage,
                "month_usage": month_usage,
                "year_usage": year_usage
            },
            "geo_distribution": geo_distribution,
            "tumor_type_distribution": tumor_type_distribution,
            "age_distribution": age_distribution,
            "gender_distribution": gender_distribution,
            "her2_distribution": her2_distribution,
            "login_heatmap": login_heatmap
        }
        
        return Response({
            "code": 2000,
            "message": "success",
            "data": data
        })

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

