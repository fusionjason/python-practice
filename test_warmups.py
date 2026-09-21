def calculate_percentage(part, whole):
    return (part / whole) * 100


def test_calculate_percentage():
    assert calculate_percentage(25, 50) == 50.0
    assert round(calculate_percentage(2, 3), 2) == 66.67


def get_status(done):
    return "DONE" if done else "NOT DONE"


def test_get_status_done():
    assert get_status(1) == "DONE"


def test_get_status_not_done():
    assert get_status(0) == "NOT DONE"
