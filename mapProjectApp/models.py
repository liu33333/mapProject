from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

work_id_validator = RegexValidator(r'^\d{1,10}$', 'Invalid work ID.')


class Employee(models.Model):
    # 姓名字段，类型为CharField，最大长度为50
    name = models.CharField(max_length=50)
    # 性别字段，类型为CharField，最大长度为1，只能是'M'或'F'
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    # 年龄字段，类型为PositiveIntegerField
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)])
    # 工号字段，类型为CharField，最大长度为10，使用work_id_validator进行验证
    work_id = models.CharField(max_length=10, validators=[work_id_validator])
    # 手机号字段，类型为CharField，最大长度为11
    phone = models.CharField(max_length=11)
    # 职位字段，类型为CharField，最大长度为100
    position = models.CharField(max_length=100)


class Location(models.Model):
    name = models.CharField(max_length=100)  # 名字
    latitude = models.FloatField(null=True, blank=True)  # 纬度
    longitude = models.FloatField(null=True, blank=True)  # 经度


class Mission(models.Model):
    # 任务序号id（一个数字串）
    id = models.CharField(max_length=20, primary_key=True)
    # 出发地（一个名字和一个经纬度数对，数对可以缺省）
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='origin_missions')
    # 目的地（一个名字和一个经纬度数对，数对可以缺省）
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination_missions')
    # 路线path（一个列表，可以为空，该列表由类似于出发地的数据结构组成）
    path = models.ManyToManyField(Location)
    # 出发时间（一个时刻，精确到分钟）
    departure_time = models.DateTimeField()
    # 预计到达时间（结构同上）
    expected_arrival_time = models.DateTimeField()
    # 实际到达时刻（结构同上）
    actual_arrival_time = models.DateTimeField(null=True, blank=True)
    # 承运人员id（一个十位以内数字串）
    carrier_id = models.CharField(max_length=10)
    # 承运车辆id（一个字符串）
    vehicle_id = models.CharField(max_length=50)

    # 任务状态（四种状态：未完成、进行中、已完成、已取消）
    STATUS_CHOICES = [
        ('未完成', '未完成'),
        ('进行中', '进行中'),
        ('已完成', '已完成'),
        ('已取消', '已取消'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
print('done')