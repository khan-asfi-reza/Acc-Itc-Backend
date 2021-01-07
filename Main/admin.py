from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ResponseMessage, PanelPost, PanelMember


# Register your models here.
class ResponseMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'email', 'time_stamp')

    class Meta:
        model = ResponseMessage


class PanelPostAdmin(admin.ModelAdmin):
    list_display = ('post_name',)

    class Meta:
        model = PanelPost


class PanelMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'year_start', 'year_end', 'email', 'post_type')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'phone_number',)}),
        ('Years Active', {'fields': ('year_start', 'year_end')}),
        ('Post', {'fields': ('post_type', 'post')}),
        ('Social Media', {'fields': ('social_link',)}),
    )

    @staticmethod
    def uploaded_image(obj):
        return mark_safe('<img src="{url}" width="auto" height="500px" />'.format(
            url=obj.picture.url
        )
        )

    readonly_fields = ('id', 'uploaded_image')

    class Meta:
        model = PanelMember


admin.site.register(ResponseMessage, ResponseMessageAdmin)
admin.site.register(PanelMember, PanelMemberAdmin)
admin.site.register(PanelPost, PanelPostAdmin)
