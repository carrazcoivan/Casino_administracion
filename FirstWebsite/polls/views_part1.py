from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from polls.models import Choice, Poll
from django.core.urlresolvers import reverse

from polls.models import Poll # since you want to use the Poll objects, you need to import it

def index(request):
#	1. test, output the given text for the whoel view
#	return HttpResponse("Hello, world. You're at the poll index.")

#	2. it outputs the the last five polls entered
#    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)

#	3.Using the template index#
#	here we're using Django's own DB-API
#	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = Context( {
#		'latest_poll_list': latest_poll_list,
#		'owner':			'Ivan Carrazco Flores',
#	})
#	return HttpResponse(template.render(context))

# 	4. using the render() function
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list, 'owner': 'ICF'}
#    context = {'latest_poll_list': latest_poll_list, 'owner': str(request)}
    return render(request, 'polls/index.html', context)
	
	
def detail(request, poll_id):
#	return HttpResponse("<p>My detail page, poll id: %s</p>" % poll_id)
#	1	return HttpResponse("you're looking at poll %s" % poll_id)
# 		Notice how we raise an exception
#	try:
#		poll = Poll.objects.get(pk=poll_id)
#	except Poll.DoesNotExist:
#		raise Http404
#		
#	2. common idiom to raise an exception in case an object doesn't exist
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll':poll , 'owner': 'ICF- KAOS'} );
#	if poll is None:
#		return HttpResponse("<p>Poll is none with poll id: %s</p>" % poll_id)
#	else:
#		return render(request, 'polls/detail.html', {'poll':poll , 'owner': 'ICF- KAOS'} );
	
	
def results(request, poll_id):
#	return HttpResponse("you're looking at the results of poll %s" % poll_id)
#
#	
	poll = get_object_or_404(Poll, pk=poll_id)
	return render( request, 'polls/results.html', { 'poll': poll} )

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
		
	
#def __404(request):
#	context = {'title': 'something went wrong in here', 'retunLink': 'localhost:8000/polls/', 'returnAnchor': 'Regresa ahora', 'returnString': 'haz click y regresa' }
#	render(request, 'polls/404.html', context)


#def this_server_error(request, template_name='500.html'):
#    """
#    500 error handler.
#
#    Templates: `500.html`
#    Context: sys.exc_info() results
#     """
#    t = loader.get_template(template_name) # You need to create a 500.html template.
#    ltype,lvalue,ltraceback = sys.exc_info()
#    sys.exc_clear() #for fun, and to point out I only -think- this hasn't happened at 
#                    #this point in the process already
#    return http.HttpResponseServerError(t.render(Context({'type':ltype,'value':lvalue,'traceback':ltraceback})))