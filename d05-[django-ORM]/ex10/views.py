from django.shortcuts import render
from .forms import CharacterFilterForm
from .models import Movies

def get_filtered_data(data):
    # Start with the base QuerySet
    queryset = Movies.objects.all()

    # Apply the filters one by one
    queryset = queryset.filter(characters__gender=data['gender'])
    queryset = queryset.filter(release_date__gte=data['min_date'])
    queryset = queryset.filter(release_date__lte=data['max_date'])
    queryset = queryset.filter(characters__homeworld__diameter__gt=data['diameter'])

    # Select the values
    values = queryset.values_list(
        'characters__name',
        'characters__gender',
        'title',
        'characters__homeworld__name',
        'characters__homeworld__diameter'
    )
    return values

# Create your views here.
def index(request):
    res = None
    if request.method == 'POST':
        form = CharacterFilterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            queryset = Movies.objects.filter(
                characters__gender=data['gender'],
                release_date__gte=data['min_date'],
                release_date__lte=data['max_date'],
                characters__homeworld__diameter__gt=data['diameter']).order_by('release_date').values_list(
                    'characters__name',
                    'characters__gender',
                    'title',
                    'characters__homeworld__name',
                    'characters__homeworld__diameter')
            res = list(queryset)
    else:
        form = CharacterFilterForm()

    return render(request, 'ex10/index.html', {'form' : form, 'results' : res})