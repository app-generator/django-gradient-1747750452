# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    birimi = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Oncelikler(models.Model):

    #__Oncelikler_FIELDS__
    oncelik = models.CharField(max_length=255, null=True, blank=True)

    #__Oncelikler_FIELDS__END

    class Meta:
        verbose_name        = _("Oncelikler")
        verbose_name_plural = _("Oncelikler")


class Durum_Kodlari(models.Model):

    #__Durum_Kodlari_FIELDS__
    durumu = models.CharField(max_length=255, null=True, blank=True)
    acik = models.BooleanField()

    #__Durum_Kodlari_FIELDS__END

    class Meta:
        verbose_name        = _("Durum_Kodlari")
        verbose_name_plural = _("Durum_Kodlari")


class Kategoriler(models.Model):

    #__Kategoriler_FIELDS__
    kategori = models.CharField(max_length=255, null=True, blank=True)

    #__Kategoriler_FIELDS__END

    class Meta:
        verbose_name        = _("Kategoriler")
        verbose_name_plural = _("Kategoriler")


class Bildirimler(models.Model):

    #__Bildirimler_FIELDS__
    aciklama = models.TextField(max_length=255, null=True, blank=True)
    oncelik = models.IntegerField(null=True, blank=True)
    kategori = models.IntegerField(null=True, blank=True)
    durumu = models.IntegerField(null=True, blank=True)
    bildirim_tarihi = models.DateTimeField(blank=True, null=True, default=timezone.now)
    kapama_tarihi = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Bildirimler_FIELDS__END

    class Meta:
        verbose_name        = _("Bildirimler")
        verbose_name_plural = _("Bildirimler")


class Birimler(models.Model):

    #__Birimler_FIELDS__
    ustbirim = models.IntegerField(null=True, blank=True)

    #__Birimler_FIELDS__END

    class Meta:
        verbose_name        = _("Birimler")
        verbose_name_plural = _("Birimler")



#__MODELS__END
