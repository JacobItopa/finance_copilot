from app.services.rule_categorizer import rule_based_category

def test_rule_based_category_matches_software():
    result = rule_based_category("AWS Cloud Services")
    assert result is not None
    assert result["category"] == "Software"
    assert result["confidence"] == "high"

def test_rule_based_category_matches_payroll():
    result = rule_based_category("Gusto Payroll Co.")
    assert result is not None
    assert result["category"] == "Payroll"
    assert result["confidence"] == "high"

def test_rule_based_category_no_match():
    # Something random that doesn't match rules
    result = rule_based_category("Unknown Vendor 1234")
    assert result is None
