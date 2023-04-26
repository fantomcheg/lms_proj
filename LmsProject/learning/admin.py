from django.contrib import admin
from .models import Course, Lesson

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title','author','start_date','description')
    list_display_links = ('title','start_date')
    list_editable = ('description', )
    #exclude = ('description','duration','price')
    search_fields = ('^title','start_date','description')
    list_per_page = 3
    actions_on_top = True
    actions_selection_counter = True
    save_on_top = True

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display=('course','name','preview', )
    search_fields = ('name', )
    list_per_page = 3
    actions_on_top = False
    actions_on_bottom = False
    actions_selection_counter = True
