# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class GooglesigninappPivotTable(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=15)  # Field name made lowercase.
    po_crearte_to_release = models.FloatField(db_column='PO_Crearte_to_Release')  # Field name made lowercase.
    pkg_start_to_finish = models.FloatField(db_column='Pkg_Start_to_Finish')  # Field name made lowercase.
    release_to_pkg_start = models.FloatField(db_column='Release_to_Pkg_Start')  # Field name made lowercase.
    brr_start_to_finish = models.FloatField(db_column='BRR_Start_To_Finish')  # Field name made lowercase.
    brr_finish_to_qp_release = models.FloatField(db_column='BRR_Finish_to_QP_Release')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoogleSignInApp_pivot_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Roche(models.Model):
    rochekey = models.CharField(max_length=125, blank=True, null=True)
    process_order_number = models.CharField(max_length=255, blank=True, null=True)
    order_type = models.CharField(max_length=255, blank=True, null=True)
    material_number = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    process_order_creation_date = models.DateField(blank=True, null=True)
    batch_number = models.CharField(max_length=255, blank=True, null=True)
    process_order_release_date = models.DateTimeField(blank=True, null=True)
    packaging_start_date = models.DateField(blank=True, null=True)
    packaging_end_date = models.DateField(blank=True, null=True)
    packaging_head_pkg_signoff = models.DateField(blank=True, null=True)
    bbr_start = models.DateField(blank=True, null=True)
    bbr_end = models.DateField(blank=True, null=True)
    qa_release_date = models.DateField(blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    batch_status = models.IntegerField(blank=True, null=True)
    po_create_release = models.IntegerField(blank=True, null=True)
    release_to_pkg_start = models.IntegerField(blank=True, null=True)
    pkg_start_bbr_finish = models.IntegerField(blank=True, null=True)
    pkg_finish_begin = models.IntegerField(blank=True, null=True)
    brr_start_finish = models.IntegerField(blank=True, null=True)
    brr_finish_qp_release = models.IntegerField(blank=True, null=True)
    fge2e = models.IntegerField(blank=True, null=True)
    check_column = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roche'


class RocheAppPivotTable(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=15)  # Field name made lowercase.
    po_crearte_to_release = models.FloatField(db_column='PO_Crearte_to_Release')  # Field name made lowercase.
    pkg_start_to_finish = models.FloatField(db_column='Pkg_Start_to_Finish')  # Field name made lowercase.
    release_to_pkg_start = models.FloatField(db_column='Release_to_Pkg_Start')  # Field name made lowercase.
    brr_start_to_finish = models.FloatField(db_column='BRR_Start_To_Finish')  # Field name made lowercase.
    brr_finish_to_qp_release = models.FloatField(db_column='BRR_Finish_to_QP_Release')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roche_app_pivot_table'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
