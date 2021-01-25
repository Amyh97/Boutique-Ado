from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ so we can see editable line items on one page """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ firelds that can be accessed through the Django admin pannel """
    # these names come from Django documentation, must be tuple
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total', 'grand_total',
                       'original_bag', 'stripe_pid',)

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name', 'order_total',
                    'delivery_cost', 'grand_total',)

    # puts most rencent order at the top
    ordering = ('-date',)


""" register Order and Order Admin, but not OrderInlineItem a
 it is assessed through the inlines """
admin.site.register(Order, OrderAdmin)
