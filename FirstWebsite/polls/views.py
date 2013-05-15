from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll

# generic.DetailView: Abstractt concepts of "display a list of objects" and "display a detail page" for an object
#	-- uses a template called <appname>/<modelname>_detail.html
#	-- expects "pk" so in this case we changed poll_id to "pk"


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
#	return HttpResponse("you're voting on poll %s" % poll_id)
#
# adding a view as a response to a form on polls.views.detail
	p = get_object_or_404(Poll,pk=poll_id)
	try:
	#python's counterpart of PHP POST array is a dictionary, available from a request object: request.POST
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	# if request.POST['key'] is empty it raises an exception
	except (KeyError, Choice.DoesNotExist):
		cnt = { 'poll': p, 'error_message': "You did not select a choice."}
		return render(request, 'polls/detail.html', cnt);
	else:
		selected_choice.votes += 1
		selected_choice.save()	 # this helps on post forms to avoid a user from posting twice the same data
		# when dealing with POST always use HttpResponseRedirect
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
		