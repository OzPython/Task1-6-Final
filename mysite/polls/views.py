from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from polls.models import Poll, Choice


def homepage(request):
    return render_to_response('polls/Home.html')

# enables the url /polls
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        """Return the last Five published polls. also removing those published set in the future"""
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# enables the url polls/specifics/x  ; x can be any number for poll_id
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls\detail.html'
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


#enables the url /polls/specifics/x/result
class ResultView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


# enables the url /polls/specifics/x/vote
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): #Refresh display since no choice is selected
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))