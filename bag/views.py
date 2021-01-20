from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ a view to return the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # session will persist while user continues to browse
    bag = request.session.get('bag', {})  # get it if it existis or create one if it doesn't

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():  # if item is in bag add how ever many
                bag[item_id]['items_by_size'][size] += quantity
            else:  # if not already got that size in the bag, add that size to bag
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:  # if size is N/A
        if item_id in list(bag.keys()):
            bag[item_id] += quantity  # if already in the bag, adds quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag  # updated version of bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the  quantity of the specified product to specified amount """
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size'][size]:
                bag.pop(item_id)
    else:  # if size is N/A
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ remove item from shopping bag """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:  # if size is N/A
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
