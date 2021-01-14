from django import template

from allauth.account.utils import user_display


register = template.Library()

"""
Display profile:
- Avartar
- Full Name - Email
- Like - Dislike
- Comment/Idioms Stat
- Rank
 
"""
@register.simple_tag(name="profile_display")
def profile_display_tag(user):
    """
    Example usage::

        {% profile_display user %}

    or if you need to use in a {% blocktrans %}::

        {% profile_display user as profile_display %}
        {% blocktrans %}
        {{ profile_display }} has sent you a gift.
        {% endblocktrans %}

    """
    return user_display(user)
