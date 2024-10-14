from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if price and MONTH_DISCOUNT_PERC:
        if brand.capitalize() in month_discount_brands: final = (price * MONTH_DISCOUNT_PERC) / 100
        else: final = price
    else: final = price
    return final


expect_content = 552.0
calculated_content = calc_discount(5520, "Vespa", month_discount_brands)
name = f'test price: {5520} brand: {"Vespa"}'
test(name, expect_content, calculated_content)

expect_content = 650.0
calculated_content = calc_discount(6500, "Kymco", month_discount_brands)
name = f'test price: {6500} brand: {"Kymco"}'
test(name, expect_content, calculated_content)

expect_content = 436.0
calculated_content = calc_discount(4360, "Yamama", month_discount_brands)
name = f'test price: {4360} brand: {"Yamama"}'
test(name, expect_content, calculated_content)

report()