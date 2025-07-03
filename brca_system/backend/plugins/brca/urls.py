from rest_framework.routers import SimpleRouter

from .views import PatientModelViewSet, SurgeryModelViewSet, DiagnoseModelViewSet, MedicaltestModelViewSet, CureModelViewSet, FollowupModelViewSet

router = SimpleRouter()
router.register("api/BRCA", PatientModelViewSet)
router.register("api/Surgery", SurgeryModelViewSet)
router.register("api/Diagnose", DiagnoseModelViewSet)
router.register("api/Medicaltest", MedicaltestModelViewSet)
router.register("api/Cure", CureModelViewSet)
router.register("api/Followup", FollowupModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls
