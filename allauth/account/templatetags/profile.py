from django import template

from allauth.account.utils import user_display
from  allauth.account.models import UserProfile


register = template.Library()

"""
Display profile:
- Avartar
- Full Name - Email
- Like - Dislike
- Comment/Idioms Stat
- Rank
 
"""

def profile_tag(parser, token ):
    
    try:
        tag_name, type = token.split_contents()
    except:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
    if type == 'small':
        return ProfileSmall()

    return Profile()

class Profile(template.Node):
    template_name = 'account/tag/profile.html'

    def __init__(self):
        pass

    def render(self, context):
        t = context.template.engine.get_template(self.template_name)
        user = context.request.user
        if user.id:
            profile, __ = UserProfile.objects.get_or_create(user=user)
            context.update({'user': user, 'profile': profile})
            res = t.render(context)
            return res 
        return ''


class ProfileSmall(template.Node):
    template_name = 'account/tag/profile_small.html'

    def __init__(self):
        pass

    def render(self, context):
        t = context.template.engine.get_template(self.template_name)
        user = context.request.user
        if user.id:
            profile, __ = UserProfile.objects.get_or_create(user=user)
            context.update({'user': user, 'profile': profile})
            res = t.render(context)
            return res 
        return ''

register.tag('profile_tag', profile_tag)