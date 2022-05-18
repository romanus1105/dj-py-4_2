from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_check = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_check += 1
        if is_main_check == 0:
            raise ValidationError('Укажите основной раздел')
        elif is_main_check > 1:
            raise ValidationError('Основным должен быть только один раздел')
        else:
            pass
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']