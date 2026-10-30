from app.cart import summary


def test_summary_empty_cart_does_not_crash():
    result = summary([])
    assert result['lines'] == 0
    assert result['subtotal'] == 0.0
    assert result['discount'] == 0.0
    assert result['total'] == 0.0
    assert result['average_item_price'] == 0.0


def test_summary_nonempty_cart_unchanged():
    result = summary([
        {'name': 'a', 'price': 10.0, 'qty': 2},
        {'name': 'b', 'price': 5.0, 'qty': 1},
    ])
    assert result == {
        'lines': 2,
        'subtotal': 25.0,
        'discount': 0.0,
        'total': 25.0,
        'average_item_price': 12.5,
    }
