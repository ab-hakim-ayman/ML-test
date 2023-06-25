from django.shortcuts import render
from .models import SentimentModel
from .forms import SentimentForm
from setfit import SetFitModel

# from code import SentimentAnalyzer

# Create your views here.
def SentimentApp(request):
    form = SentimentForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Sentence')    # got the sentence

            model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
            # Run inference
            preds = model(['sent', 'sent'])
            print(preds[0])

            context['text'] = preds
        else:
            form = SentimentForm()
    
    context['form'] = form
    return render(request, 'app.html', context=context)