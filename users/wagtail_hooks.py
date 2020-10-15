from wagtail.contrib.modeladmin.options import (
  ModelAdmin,
  ModelAdminGroup,
  modeladmin_register,
)
from .models import User

class UserAdmin(ModelAdmin):
  model = User
  menu_label ="Users"
  menu_order = 100
  add_to_settings_menu = False
  exclude_from_explorer = False
  list_display = ('pk', 'email', 'is_provider', 'is_staff', 'is_active', 'date_joined', 'last_login')

modeladmin_register(UserAdmin)