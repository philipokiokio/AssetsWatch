from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAdapter(DefaultAccountAdapter):


    def save_user(self,request,user,form,commit=False):
        user = super().save_user(request,user,form,commit)

        data = form.cleaned_data
        user.fullname = data.get('fullname')
        user.save()
        return user

    
    def send_mail(self,template_prefix,email,context):
        context['activate_url'] = settings.URL_FRONT + 'verify/'+context['key']+'/'        
        msg = self.render_mail(template_prefix, email, context)
        msg.send()