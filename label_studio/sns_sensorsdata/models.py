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
    



class Audios(models.Model):
    # ForeignKey 用來建立與其他模型的關聯
    project = models.ForeignKey('projects.Project', related_name='audios', on_delete=models.CASCADE)
    source = models.ForeignKey('sns_sensorsdata.Sources', related_name='audios', on_delete=models.CASCADE)

    # 字符串欄位，可選填
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name="位置")
    file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="文件路徑")
    audio_text = models.TextField(blank=True, null=True, verbose_name="音頻文本")
    
    # 上傳時間，可選填，預設為當前時間
    upload_time = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="上傳時間")

    def __str__(self):
        return f"{self.position or '未指定位置'} - {self.file_path}"



class Videos(models.Model):
    # ForeignKey 用來建立與其他模型的關聯
    project = models.ForeignKey('projects.Project', related_name='videos', on_delete=models.CASCADE)
    source = models.ForeignKey('sns_sensorsdata.Sources', related_name='videos', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='videos',on_delete=models.CASCADE)

    # 字符串欄位，可選填
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="標題")
    video_file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="視頻文件路徑")
    depth_file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="深度文件路徑")
    pointcloud_file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="點雲文件路徑")
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name="位置")
    calibration = models.TextField(blank=True, null=True, verbose_name="校準數據")
    imu = models.TextField(blank=True, null=True, verbose_name="IMU數據")
    
    # 上傳時間，可選填，預設為當前時間
    upload_time = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="上傳時間")

    def __str__(self):
        return self.title or "未命名視頻"
    


class Temperatures(models.Model):
    # ForeignKey 用來建立與其他模型的關聯
    project = models.ForeignKey('projects.Project', related_name='temperatures',on_delete=models.CASCADE)
    source = models.ForeignKey('sns_sensorsdata.Sources', related_name='temperatures',on_delete=models.CASCADE)

    # 字符串欄位，可選填
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name="位置")
    raw_file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="原始文件路徑")
    temperature_file_path = models.CharField(max_length=255, blank=True, null=True, verbose_name="溫度文件路徑")
    calibration = models.TextField(blank=True, null=True, verbose_name="校準數據")
    
    # 上傳時間，可選填，預設為當前時間
    upload_time = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name="上傳時間")

    def __str__(self):
        return f"{self.position or '未指定位置'} - {self.upload_time.strftime('%Y-%m-%d %H:%M:%S')}"






