from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Yeni seçim alanı eklemek için varsayılan 3 boş alan

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')  # Admin listesinde gösterilecek alanlar
    list_filter = ['pub_date']  # Tarihe göre filtreleme
    search_fields = ['question_text']  # Arama çubuğu
    inlines = [ChoiceInline]  # Seçenekleri aynı sayfada düzenleme

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)