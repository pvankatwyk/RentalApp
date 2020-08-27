username_input = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

# aprsl_price, purchase_price, arv, buy_closing_cost, rehab_cost, appreciation, rent, extra_income, prop_tax, insurance,
#                      repairs, vacancy, capex, mgmt, hoa, other, num_units, loan_term, interest_rate, down_payment, extra_payments, sell_closing_cost,
#                      sell_year, output):

address = """
MDTextField:
    hint_text: "Address"
    pos_hint: {'x':0.05,'y':0.765}
    size_hint: None, None
    width: 200
    """

num_units = """
    MDTextField:
        hint_text: "Number of Units"
        pos_hint: {'x':0.05,'y': 0.7}
        size_hint: None, None
        width: 125
"""

aprsl_price = """
MDTextField:
    hint_text: "Appraisal Price"
    #mode: "rectangle"
    #helper_text: "Price of home upon appraisal ($)"
    #helper_text_mode: "on_focus"
    pos_hint:{'x': 0.05, 'y': 0.635}
    size_hint_x: None
    width: 125
"""


purchase_price = """
MDTextField:
    hint_text: "Purchase Price"
    #helper_text: "Purchase Price($)"
    #helper_text_mode: "on_focus"
    pos_hint:{'x': 0.05, 'y': 0.57}
    size_hint: (None, None)
    width: 125
"""


repair = """
MDTextField:
    hint_text: "Repair Cost"
    pos_hint: {'x':0.05,'y':0.505}
    #pos_hint: {'x':0.25,'y':0.505}
    size_hint: None,None
    width: 125
"""

arv = """
MDTextField:
    hint_text: "ARV"
    #helper_text: "After Repair Value ($)"
    #helper_text_mode: "on_focus"
    pos_hint:{'x': 0.05, 'y': 0.44}
    #pos_hint:{'x': 0.25, 'y': 0.7}
    size_hint: (None, None)
    width: 125
"""

