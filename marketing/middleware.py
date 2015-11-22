import datetime

from django.utils import timezone
from .models import MarketingMessage

class DisplayMarketing():
    def process_request(self, request):
    #   if 'marketing_message' not in request.session:
            print timezone.now()
            print timezone.now() + datetime.timedelta(hours=8)
            try:
                request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
            except:
                request.session['marketing_message'] = False
