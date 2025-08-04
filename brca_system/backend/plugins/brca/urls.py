from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import PatientModelViewSet, SurgeryModelViewSet, DiagnoseModelViewSet, MedicaltestModelViewSet, CureModelViewSet, FollowupModelViewSet

router = SimpleRouter()
router.register("api/BRCA", PatientModelViewSet)
router.register("api/Surgery", SurgeryModelViewSet)
router.register("api/Diagnose", DiagnoseModelViewSet)
router.register("api/Medicaltest", MedicaltestModelViewSet)
router.register("api/Cure", CureModelViewSet)
router.register("api/Followup", FollowupModelViewSet)

# 仪表盘相关URL
dashboard_urlpatterns = [
    path('api/dashboard/patient-count/', PatientModelViewSet.as_view({'get': 'dashboard_patient_count'}), name='dashboard_patient_count'),
    path('api/dashboard/usage-statistics/', PatientModelViewSet.as_view({'get': 'dashboard_usage_statistics'}), name='dashboard_usage_statistics'),
    path('api/dashboard/patient-geo-distribution/', PatientModelViewSet.as_view({'get': 'dashboard_patient_geo_distribution'}), name='dashboard_patient_geo_distribution'),
    path('api/dashboard/tumor-type-distribution/', PatientModelViewSet.as_view({'get': 'dashboard_tumor_type_distribution'}), name='dashboard_tumor_type_distribution'),
    path('api/dashboard/patient-age-distribution/', PatientModelViewSet.as_view({'get': 'dashboard_patient_age_distribution'}), name='dashboard_patient_age_distribution'),
    path('api/dashboard/patient-gender-distribution/', PatientModelViewSet.as_view({'get': 'dashboard_patient_gender_distribution'}), name='dashboard_patient_gender_distribution'),
    path('api/dashboard/her2-distribution/', PatientModelViewSet.as_view({'get': 'dashboard_her2_distribution'}), name='dashboard_her2_distribution'),
    path('api/dashboard/login-heatmap/', PatientModelViewSet.as_view({'get': 'dashboard_login_heatmap'}), name='dashboard_login_heatmap'),
    path('api/dashboard/all-data/', PatientModelViewSet.as_view({'get': 'dashboard_all_data'}), name='dashboard_all_data'),
]

urlpatterns = [
]
urlpatterns += router.urls
urlpatterns += dashboard_urlpatterns
