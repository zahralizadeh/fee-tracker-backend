# -*- coding: utf-8 -*-
import requests
import logging
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta
from .models import Scrape, PropertyFile
from django.utils.timezone import make_aware

logger = logging.getLogger(__name__)

# Create your views here.
def collectdata(request):
    logger.debug("----def collectdata BUY ----->  is running")
    try:    #property database is not empty
        last_buy_property_time = PropertyFile.objects.filter(offertype ='خرید-فروش').order_by('-publishdate')[0].publishdate
        scrapeIhomeBuy = Scrape(scrapetype= 'خرید-فروش',last_update_time=last_buy_property_time)
        if scrapeIhomeBuy.startscraping_update():
            scrapeIhomeBuy.save()
        response = 'Hi...I saved information about offertype = Buy in database!'    
    except: 
        if  not PropertyFile.objects.filter(offertype ='خرید-فروش'): #property database is  empty
            scrapeIhomeBuy = Scrape(scrapetype= 'خرید-فروش',last_update_time=make_aware(datetime.now() - timedelta(days=60)))
            if scrapeIhomeBuy.startscraping_update():
                scrapeIhomeBuy.save() 
                response ='Hi...There was no BUY files saved in DB! Data published in the last month was scraped successfully!'
        else:
            response = 'Hi...There was an error in process of collecting  BUY data!'
    
    logger.debug("----def collectdata RENT ----->  is running")
    try:
        last_rent_property_time = PropertyFile.objects.filter(offertype ='رهن-اجاره').order_by('-publishdate')[0].publishdate
        scrapeIhomeRent = Scrape(scrapetype= 'رهن-اجاره',last_update_time=last_rent_property_time)
        if scrapeIhomeRent.startscraping_update():
            scrapeIhomeRent.save()
        response = response +'\n I saved information about offertype = Rent in database!'
    except: 
        if  not PropertyFile.objects.filter(offertype ='رهن-اجاره'): #property database is  empty
            scrapeIhomeRent = Scrape(scrapetype= 'رهن-اجاره',last_update_time=make_aware(datetime.now() - timedelta(days=60)))
            if scrapeIhomeRent.startscraping_update():
                scrapeIhomeRent.save() 
                response = response +'\n There was no RENT files saved in DB! Data published in the last month was scraped successfully!'
        else:
            response = response + '\n There was an error in process of collecting  RENT data!'
    return HttpResponse(response)
