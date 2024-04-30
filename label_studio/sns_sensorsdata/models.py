from django.db import models
from django.utils import timezone

# 確保已經導入或定義了這些模型的參照
from projects.models import Project

# Create your models here.


class Sources(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    device_serial_number = models.IntegerField(blank=True, null=True)
    device_config = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.device_name} (SN: {self.device_serial_number})"
    


class Trajectory(models.Model):
    # ForeignKey 用來建立與其他模型的關聯
    project = models.ForeignKey('projects.Project' , related_name='trajectorys', on_delete=models.CASCADE)
    source = models.ForeignKey('sns_sensorsdata.Sources', related_name='trajectorys', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='trajectorys', on_delete=models.CASCADE)

    # 字符串欄位，可選填
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="標題")
    
    # 文件路徑
    file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="文件路徑")
    
    # 上傳時間，預設為當前時間
    upload_time = models.DateTimeField(default=timezone.now, verbose_name="上傳時間")

    def __str__(self):
        return f"{self.title or '無標題'} - {self.upload_time.strftime('%Y-%m-%d %H:%M:%S')}"



