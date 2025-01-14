# triangle.py

def is_valid_triangle(a, b, c):
    """Check if three sides can form a valid triangle using the triangle inequality theorem."""
    return a + b > c and a + c > b and b + c > a
