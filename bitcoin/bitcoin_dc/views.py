from .models import Address, Transactions
import requests
from django.shortcuts import render
from .forms import AddressForm
from django.http import HttpResponseRedirect


def address_view(request):
    # get form and post bitcoin address of interest
    if request.method == 'GET':
        form = AddressForm(request.GET)
        return render(request, 'address.html', {'form': form})
    if request.method == 'POST':
        form = AddressForm(request.POST)
        # get Address object if already in database or create new instance
        if form.is_valid():
            addr, created = Address.objects.get_or_create(**form.cleaned_data)
            request.session['addr'] = str(addr)
            #if new instance was created, get transaction data from API blockchain
            # and insert data into Transactions table
            if created:
                r = requests.get(
                    'https://blockchain.info/rawaddr/{0}?format=json'.format(str(addr)))
                a = Address.objects.get(address=addr)

                for i in range(len(r.json()['txs'])):
                    time = r.json()['txs'][i]['time']
                    tx_id = r.json()['txs'][i]['tx_index']
                    size = r.json()['txs'][i]['size']
                    a.transactions_set.create(time=time, tx_index=tx_id, size=size)

            return HttpResponseRedirect('/transactions')


def transactions_view(request):
    #show information on transactions of address from AddressForm
    addr = request.session.get('addr')
    address = Address.objects.filter(address=addr)
    transactions = Transactions.objects.filter(address__address=addr)
    context = {'address': address,
               'transactions': transactions}

    return render(request, 'transactions.html', context)





