from django.shortcuts import render
from django.http import HttpResponse
from frontPage.models import PortfolioPiece, AboutPiece

# Create your views here.

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    #context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    portfolio_piece_list = PortfolioPiece.objects.all()
    about_piece_list = AboutPiece.objects.all()
    context_dict = {'portfolio_pieces': portfolio_piece_list, 'about_pieces': about_piece_list}
    return render(request, 'frontPage/startbootstrap-agency-1.0.4/index.html', context_dict)
