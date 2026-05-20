def validate_baggage(baggage_weight, baggage_type, passenger_class, flight_type, hazardous_item, passport_valid):
    """
    Business Rules:
    - Carry-on baggage max 7 kg
    - Checked baggage max 30 kg
    - Business class gets extra 10 kg allowance
    - International flights require passport validation
    - Hazardous items are prohibited
    """

    if hazardous_item:
        return False

    if flight_type == "international" and not passport_valid:
        return False

    if baggage_type == "carry-on":
        max_allowance = 7
    elif baggage_type == "checked":
        max_allowance = 30
    else:
        return False

    if passenger_class == "business":
        max_allowance += 10
        
    if baggage_weight > max_allowance:
        return False

    return True