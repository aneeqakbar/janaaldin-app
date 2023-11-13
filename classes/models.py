from django.db import models
from django.utils import timezone

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    staff_members = models.ManyToManyField("authentication.StaffMember", related_name="classes")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def get_excerpt(self):
        if len(str(self.description)) > 100:
            return str(self.description)[:100] + "..."
        return str(self.description)

    def get_next_upcoming_date(self):
        current_time = timezone.now()
        upcoming_dates = self.available_times.filter(datetime__gt=current_time).order_by('datetime')
        
        if upcoming_dates.exists():
            return upcoming_dates.first().datetime
        else:
            return None

class ClassDateTime(models.Model):
    parent = models.ForeignKey("classes.Class", on_delete=models.CASCADE, related_name="available_times")
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.parent.name} - {self.datetime}'

    @property
    def get_datetime_display(self):
        try:
            return self.datetime.strftime("%Y-%m-%dT%H:%M")
        except:
            return ""
