from flask import flash

def validate_hardware_data(data):
    required_fields = ['product_name', 'specs', 'category', 'brand', 'price', 'stock', 'img_url']
    for field in required_fields:
        if not data.get(field):
            flash(f"El campo '{field}' es obligatorio", "error")
            return False
    try:
        float(data['price'])
        int(data['stock'])
    except ValueError:
        flash("El precio debe de ser un número y el stock debe de ser un entero", "error")
        return False
    return True

def validate_videogame_data(data):
    required_fields = ['game_name', 'game_description', 'genre', 'platforms', 'price', 'stock', 'img_url', 'release_date', 'developer']
    for field in required_fields:
        if not data.get(field):
            flash(f"El campo '{field} es obligatorio'", "error")
            return False
    try:
        float(data['price'])
        int(data['stock'])
    except ValueError:
        flash("El precio debe de ser un número y el stock debe de ser un entero", "error")
        return False
    return True