from django.contrib import admin
from account.models import Account, Profile
import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# class CsvImportForm(forms.Form):
#  csv_file = forms.FileField()

# @admin.register(Hero)
# class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
#  ...
#  change_list_template = "entities/heroes_changelist.html"
#  def get_urls(self):
#  urls = super().get_urls()
#  my_urls = [
#  ...
#  path('import-csv/', self.import_csv),
#  ]
#  return my_urls + urls
#  def import_csv(self, request):
#  if request.method == "POST":
#  csv_file = request.FILES["csv_file"]
#  reader = csv.reader(csv_file)
#  # Create Hero objects from passed in data
#  # ...
#  self.message_user(request, "Your csv file has been
# imported")
#  return redirect("..")
#  form = CsvImportForm()
#  payload = {"form": form}
#  return render(
#  request, "admin/csv_form.html", payload
#  )


def mark_as_viewed(self, request, queryset):
    queryset.update(viewed=True)

mark_as_viewed.short_description = "Mark as read"

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','email','id', 'first_name','last_name','phone','country','city','zip_code','is_subscribed','is_staff','is_admin','is_superuser') 
    readonly_fields=('date_joined', 'last_login', 'password','username','email', 'is_active')

admin.site.register(Account, AccountAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user',)
    list_filter = ('user',)
    ordering = ('user',)
