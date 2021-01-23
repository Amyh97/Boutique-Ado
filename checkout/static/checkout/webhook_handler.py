from django.http import HttpResponse


class StripeWH_handler:
    """ Handle Stripe Webhooks
        in case we need to access
        any attributes of of the request from
        stripe """
    def __init__(self):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic /unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved {event["type"]}',
            status=200)
