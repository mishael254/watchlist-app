from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_ow_four(error):
    '''
    a function to lender the 404 page
    '''
    return render_template('fourowfour.html'),404