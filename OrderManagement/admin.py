from django.contrib import admin

from OrderManagement.models import Clients, Articles, Orders

# Register your models here.


class ClientsAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone")  # Show custom display names
    search_fields = ("name", "phone")  # Add search field


class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ("section",)  # filter


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("number", "date")
    list_filter = ("date",)  # filter
    date_hierarchy = "date"


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Orders, OrdersAdmin)