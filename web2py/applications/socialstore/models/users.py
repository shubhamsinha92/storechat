# coding: utf8
from gluon.tools import Auth
user_extra_fields = [Field('Name'), ...]
employee_extra_fields = [Field('Store_Name', ...]

auth.settings.extra_fields['auth_user'] = (
    [Field('user_type', requires=IS_IN_SET(['User', 'Store']))] +
    user_extra_fields + _extra_fields


