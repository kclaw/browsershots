# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Priority views.
"""

__revision__ = "$Rev$"
__date__ = "$Date$"
__author__ = "$Author$"

from django.shortcuts import render_to_response
from django.template import RequestContext


def overview(http_request):
    symbol_amount_currency_list = [
        ('&euro;', '10.00', 'EUR'),
        ('$', '15.00', 'USD'),
        ]
    user_has_priority_until = None
    if not http_request.user.is_anonymous():
        priorities = http_request.user.userpriority_set.order_by('-expire')
        if len(priorities):
            user_has_priority_until = priorities[0].expire
    return render_to_response('priority/overview.html', locals(),
        context_instance=RequestContext(http_request))


def thankyou(http_request):
    return render_to_response('priority/thankyou.html', locals(),
        context_instance=RequestContext(http_request))


def support(http_request):
    return render_to_response('priority/support.html', locals(),
        context_instance=RequestContext(http_request))