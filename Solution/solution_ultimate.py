#!/usr/bin/env python3

def categorize_trip(d, m, r):
    """Categorize a trip based on its characteristics"""
    mpd = m / d if d > 0 else 0
    rpd = r / d if d > 0 else 0
    
    # Primary category by duration
    if d == 1:
        duration_cat = "1day"
    elif d == 2:
        duration_cat = "2day"
    elif d == 3:
        duration_cat = "3day"
    elif d <= 5:
        duration_cat = "4to5day"
    elif d <= 10:
        duration_cat = "6to10day"
    else:
        duration_cat = "11plus_day"
    
    # Mileage category
    if mpd > 300:
        mileage_cat = "very_high_mileage"
    elif mpd > 150:
        mileage_cat = "high_mileage"
    elif mpd > 75:
        mileage_cat = "medium_mileage"
    else:
        mileage_cat = "low_mileage"
    
    # Receipt category  
    if rpd > 500:
        receipt_cat = "very_high_receipts"
    elif rpd > 200:
        receipt_cat = "high_receipts"
    elif rpd > 75:
        receipt_cat = "medium_receipts"
    else:
        receipt_cat = "low_receipts"
    
    return f"{duration_cat}_{mileage_cat}_{receipt_cat}"

def calculate_reimbursement(d, m, r):
    """Calculate reimbursement using discovered formulas"""
    category = categorize_trip(d, m, r)
    
    # Perfect formulas for each category
    formulas = {"3day_low_mileage_low_receipts": (95, 0.75, 0.7), "1day_low_mileage_low_receipts": (65, 0.85, 0.5), "2day_low_mileage_low_receipts": (90, 0.5, 0.7), "1day_medium_mileage_low_receipts": (80, 0.85, 1.0), "4to5day_low_mileage_low_receipts": (65, 0.8, 0.9), "4to5day_low_mileage_high_receipts": (75, 0.7, 0.55), "4to5day_medium_mileage_high_receipts": (80, 0.75, 0.65), "4to5day_high_mileage_medium_receipts": (120, 0.3, 0.6), "11plus_day_low_mileage_medium_receipts": (65, 0.55, 0.5), "6to10day_low_mileage_medium_receipts": (60, 0.3, 0.75), "6to10day_medium_mileage_medium_receipts": (60, 0.6, 0.65), "3day_very_high_mileage_medium_receipts": (95, 0.3, 0.75), "3day_high_mileage_high_receipts": (135, 0.4, 0.6), "2day_very_high_mileage_high_receipts": (65, 0.2, 0.95), "1day_very_high_mileage_high_receipts": (130, 0.45, 0.55), "1day_very_high_mileage_very_high_receipts": (95, 0.4, 0.55), "1day_high_mileage_very_high_receipts": (90, 0.2, 0.5), "11plus_day_medium_mileage_low_receipts": (70, 0.4, 0.7), "11plus_day_low_mileage_low_receipts": (60, 0.2, 1.0), "2day_very_high_mileage_very_high_receipts": (65, 0.65, 0.5), "4to5day_high_mileage_high_receipts": (90, 0.35, 0.75), "2day_high_mileage_very_high_receipts": (85, 0.7, 0.55), "3day_high_mileage_very_high_receipts": (75, 0.35, 0.6), "3day_high_mileage_low_receipts": (110, 0.5, 0.65), "3day_low_mileage_high_receipts": (60, 0.25, 0.9), "6to10day_high_mileage_medium_receipts": (65, 0.65, 0.75)}
    
    if category in formulas:
        formula = formulas[category]
        return formula[0] * d + formula[1] * m + formula[2] * r
    else:
        # Default formula
        return 100 * d + 0.5 * m + 0.8 * r

if __name__ == "__main__":
    import sys
    d, m, r = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    print(f"{calculate_reimbursement(d, m, r):.2f}")
