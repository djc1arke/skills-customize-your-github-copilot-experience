"""Helper functions for the testing and debugging assignment."""


def calculate_total(items):
    """Return the total cost for a list of order items."""
    total = 0
    for item in items:
        total += item["price"]
    return total


def has_stock(available, requested):
    """Return whether the requested quantity is available."""
    return available < requested


def average_rating(ratings):
    """Return the average rating, or 0 for an empty list."""
    return sum(ratings) / len(ratings)
