from django.contrib import admin
from .models import Project_Root,Startapp,Templates,Static,Css,Js,Images,Media,Article,TableOfContent

from django.contrib.auth import get_user_model




# class ProjectNameAdmin(admin.ModelAdmin):
#     list_display = ('id', 'asgi', 'settings', 'urls', 'wsgi')

# class StartappNameAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name', 'admin_file', 'apps_file', 'models_file', 'tests_file', 'urls_file', 'views_file')

# class TemplatesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'template_name')

# class StaticAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project_name')

# class CssAdmin(admin.ModelAdmin):
#     list_display = ('id', 'static_name', 'css_name')

# class JsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'static_name', 'js_name')

# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'static_name', 'images_name')

# class MediaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'media_name')

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'article_title')

# admin.site.register(ProjectName, ProjectNameAdmin)
# admin.site.register(StartappName, StartappNameAdmin)
# admin.site.register(Templates, TemplatesAdmin)
# admin.site.register(Static, StaticAdmin)
# admin.site.register(Css, CssAdmin)
# admin.site.register(Js, JsAdmin)
# admin.site.register(Images, ImagesAdmin)
# admin.site.register(Media, MediaAdmin)
# admin.site.register(Article, ArticleAdmin)

admin.site.register(TableOfContent)
admin.site.register(Project_Root)
admin.site.register(Startapp)
admin.site.register(Templates)
admin.site.register(Static)
admin.site.register(Css)
admin.site.register(Js)
admin.site.register(Images)
admin.site.register(Media)
admin.site.register(Article)

admin.site.register(get_user_model())