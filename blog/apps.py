
# apps.py: このファイルでアプリケーションの設定が行われます。
# 主にアプリケーションの名前や設定を指定します。
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
