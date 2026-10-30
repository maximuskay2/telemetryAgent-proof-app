from app.cart import summary


def test_summary_empty_cart_does_not_crash():
    result = summary([])
    assert result == {
        "lines": 0,
        "subtotal": 0.0,
        "discount": 0.0,
        "total": 0.0,
        "average_item_price": 0.0,
    }


def test_summary_nonempty_cart_unchanged():
    result = summary([
        {"name": "a", "price": 10.0, "qty": 1},
        {"name": "b", "price": 20.0, "qty": 1},
    ])
    assert result["lines"] == 2
    assert result["subtotal"] == 30.0
    assert result["discount"] == 0.0
    assert result["total"] == 30.0
    assert result["average_item_price"] == 15.0
