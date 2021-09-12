from .models import ProductinBasket


def painting_basket(request):
    return_dict=dict()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_bask=ProductinBasket.objects.filter(session_key=session_key)
    kolvo_tov_in_bask=products_in_bask.count()

    return locals()