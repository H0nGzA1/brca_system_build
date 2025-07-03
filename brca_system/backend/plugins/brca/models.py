from django.db import models
from django.db.models import SmallIntegerField, IntegerField, CharField, FloatField, DateField, DateTimeField, ForeignKey, CASCADE, SET_NULL
# Create your models here.
from dvadmin.utils.models import CoreModel
#from dvadmin.op_drf.models import CoreModel

class Patient(CoreModel):
    gender_choices = (
            (0, '未知'),
            (1, '男'),
            (2, '女'),
    )
    medicalNumber = CharField(max_length=128, verbose_name='患者病历号', help_text='病历号', blank=True,null=True)
    name = CharField(max_length=128, verbose_name='患者姓名', help_text='患者姓名', null=True, blank=True,db_index=True)
    unique_label = CharField(max_length=256, verbose_name='标识', null=True, blank=True)
    phone = CharField(max_length=11, verbose_name='患者手机号',help_text='11位的手机号码(家属亦可)',blank=True,null=True)
    idCard = CharField(max_length=18, verbose_name='患者身份证号', help_text='患者18位的身份证号码', blank=True,null=True)
    gender = IntegerField(verbose_name='患者性别', default=0)
    birthday = DateTimeField(verbose_name='患者出生日期', help_text='患者出生日期', blank=True,null=True)
    age = SmallIntegerField(verbose_name='患者年龄',help_text='患者年龄:(岁)',blank=True,null=True)
    height = FloatField(verbose_name='患者身高',help_text='患者身高(m)',blank=True,null=True)
    weight = FloatField(verbose_name='患者体重',help_text='患者体重(kg)',blank=True,null=True)
    BMI = FloatField(verbose_name='BMI', help_text='BMI指数',blank=True,null=True)

    RH_type = IntegerField(verbose_name='患者RH血型', default=0)
    ABO_type = IntegerField(verbose_name='患者ABO血型', default=0)
    smoking = IntegerField(verbose_name='是否吸烟', default=0)
    alcohol = IntegerField(verbose_name='是否饮酒', default=0)
    surgery_history = CharField(max_length=512, verbose_name='院前手术史', help_text='院前手术史，如:子宫切除/卵巢切除', default='无')
    allergy_drugs = CharField(max_length=512, verbose_name='过敏药物', help_text='过敏药物', default='无')
    familial_inheritance = CharField(max_length=512,  verbose_name='家族遗传史', help_text='家族遗传病' , default='无')

    marriage = IntegerField(verbose_name='婚姻状态', default=0)
    pregnancy_times = SmallIntegerField(verbose_name='生育次数',help_text='患者生育次数',blank=True,null=True)
    menopausal = IntegerField(verbose_name='是否绝经', default=0)
    menopausal_age = SmallIntegerField(verbose_name='绝经年龄',help_text='绝经年龄',blank=True,null=True)
    last_time = DateTimeField(verbose_name='末次月经日期', help_text='末次月经日期', blank=True,null=True)

    doctor_name = CharField(max_length=128, verbose_name='主治医生', help_text='主治医生姓名', null=True, blank=True)
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    #@property
    #def unique_label(self):
        #return self.name + "#" + self.medicalNumber

    #def save(self, *args, **kwargs):
        #if not self.unique_label:
            #self.unique_label = self.name + "#" + self.medicalNumber
        #super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + "#" + self.medicalNumber

    class Meta:
        verbose_name = "患者基本信息"
        verbose_name_plural = verbose_name

class Surgery(CoreModel):
    # 病人外键DO_NOTHING修改为SET_NULL，提高代码健壮性
    patient = ForeignKey(Patient,null=True, blank=True, verbose_name='患者', on_delete=models.SET_NULL)
    surgery_name = CharField(max_length=128, verbose_name='手术名称', help_text='手术名称', null=True, blank=True)
    surgery_site = IntegerField(verbose_name='手术部位', help_text='手术部位' , default=0)
    rebuild = IntegerField(verbose_name='是否重建',help_text='是否重建' , default=2) #默认:否
    rebuild_name = CharField(max_length=512,verbose_name='重建方式', help_text='重建方式' ,null=True, blank=True)
    axillary_lymph_dissection = IntegerField(verbose_name='是否腋窝清扫',help_text='是否腋窝清扫' , default=2) #默认:否
    axillary_lymph_dissection_name = CharField(max_length=512,verbose_name='腋窝清扫手术', help_text='腋窝清扫手术名称', null=True, blank=True)
    doctor_name = CharField(max_length=128, verbose_name='手术医生', help_text='手术医生姓名', null=True, blank=True)
    surgery_time = DateTimeField(verbose_name='手术时间', null=True, blank=True)
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "手术记录"
        verbose_name_plural = verbose_name

class Diagnose(CoreModel):
    patient = ForeignKey(Patient,null=True, blank=True, verbose_name='患者', on_delete=models.SET_NULL)
    disease = CharField(max_length=512, verbose_name='疾病诊断', blank=True,null=True)
    pathology_type = IntegerField(verbose_name='病理类型', help_text='病理类型' , default=0)
    pathology_sub = CharField(max_length=512, verbose_name='病理分型', blank=True,null=True)
    TNM = CharField(max_length=128, verbose_name='TNM分期', help_text='TNM分期', null=True, blank=True)
    confirm_date = DateTimeField(verbose_name='确诊日期')
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "诊断记录"
        verbose_name_plural = verbose_name

class Cure(CoreModel):
    patient = ForeignKey(Patient,null=True, blank=True, verbose_name='患者', on_delete=models.SET_NULL)
    HER2_status = IntegerField(verbose_name='HER2结果', help_text='HER2阴阳性' , default=0)
    cure_type = IntegerField(verbose_name='治疗类型', help_text='治疗类型' , default=0)
    drug_name = CharField(max_length=256, verbose_name='药物名称', help_text='药物名称', null=True, blank=True)
    combine_incretion = IntegerField(verbose_name='联合内分泌治疗', help_text='是否联合内分泌治疗' , default=0)
    anthracycline = IntegerField(verbose_name='蒽环类用药是否脂质体', help_text='蒽环类用药是否脂质体' , default=0)
    ECT = IntegerField(verbose_name='EC-T是否密集', help_text='EC-T是否密集' , default=0)
    herceptin_use = IntegerField(verbose_name='赫赛汀使用', help_text='赫赛汀使用与否' , default=0)
    herceptin = IntegerField(verbose_name='赫赛汀是否密集', help_text='赫赛汀是否密集' , default=0)
    cycles = IntegerField(verbose_name='术前完成周期数', help_text='术前完成周期数' , blank=True,null=True)
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "治疗记录"
        verbose_name_plural = verbose_name

class Medicaltest(CoreModel):
    patient = ForeignKey(Patient,null=True, blank=True, verbose_name='患者', on_delete=models.SET_NULL)
    sample_id = CharField(max_length=256, verbose_name='样本编号', help_text='样本编号', null=True, blank=True)
    application_time = DateTimeField(verbose_name='申请时间', null=True, blank=True)
    report_time = DateTimeField(verbose_name='报告时间', null=True, blank=True)
    test_name = CharField(max_length=256, verbose_name='检验项目名称', help_text='检验项目名称', null=True, blank=True)
    test_code = CharField(max_length=256, verbose_name='检验项目编号', help_text='检验项目编号', null=True, blank=True)
    qualitative_result = CharField(max_length=256, verbose_name='定性结果', help_text='定性结果', null=True, blank=True)
    quantitative_result = CharField(max_length=256, verbose_name='定量结果', help_text='定量结果', null=True, blank=True)
    reference_range = CharField(max_length=256, verbose_name='参考区间', help_text='参考区间', null=True, blank=True)
    test_institution = CharField(max_length=256, verbose_name='检验单位', help_text='检验单位', null=True, blank=True)
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "检验记录"
        verbose_name_plural = verbose_name

class Followup(CoreModel):
    patient = ForeignKey(Patient,null=True, blank=True, verbose_name='患者', on_delete=models.SET_NULL)
    visit_date = DateTimeField(verbose_name='此次随访时间', auto_now=True)
    status = IntegerField(verbose_name='患者状态', help_text='随访时患者状态' , default=0)
    time_of_death = DateTimeField(verbose_name='死亡时间', blank=True, null=True)
    cause_of_death = CharField(max_length=512, verbose_name='死亡原因', help_text='死亡原因', blank=True, null=True)
    recurrence_metastasis = IntegerField(verbose_name='复发转移', help_text='是否复发转移' , default=0)
    metastasis_site = CharField(max_length=256, verbose_name='转移部位', help_text='转移部位', blank=True, null=True)
    postoperative_survival_time = IntegerField(verbose_name='术后生存时间',help_text='术后生存时间(月)',blank=True,null=True)
    tumor_free_survival_time = IntegerField(verbose_name='无瘤生存时间',help_text='无瘤生存时间(月)',blank=True,null=True)
    all_survival_time = IntegerField(verbose_name='总生存时间',help_text='总生存时间(月)',blank=True,null=True)
    treatment_methods = CharField(max_length=256, verbose_name='治疗方法', help_text='治疗方法', blank=True, null=True)
    treatment_effect = CharField(max_length=256, verbose_name='治疗效果', help_text='治疗效果', blank=True, null=True)
    remark = CharField(max_length=512, verbose_name='备注', blank=True,null=True)
    create_time = DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "随访记录"
        verbose_name_plural = verbose_name

