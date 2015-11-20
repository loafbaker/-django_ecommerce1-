from .models import MarketingMessage

class DisplayMarketing():
    def process_request(self, request):
        if 'marketing_message' not in request.session:
            try:
                request.session['marketing_message'] = MarketingMessage.objects.all()[0].message
            except:
                request.session['marketing_message'] = False
