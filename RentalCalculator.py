import pandas as pd
import numpy as np
from datetime import date


def RentalCalculator(aprsl_price, purchase_price, arv, buy_closing_cost, rehab_cost, appreciation, rent, extra_income, prop_tax, insurance,
                     repairs, vacancy, capex, mgmt, hoa, other, num_units, loan_term, interest_rate, down_payment, extra_payments, sell_closing_cost,
                     sell_year, output):
    # INPUTS:
    # Home Appraisal Price, Purchase Price, ARV, Buy Closing Cost (%), Repair Costs
    # Appreciation Rate (%), Rental Income, Property Taxes (%), Insurance, Repairs/Maintenance (%)
    # Vacancy, CapEx, Management, HOA, Other, Number of Units, Loan Term, Interest Rate,
    # Down Payment (%), Extra Payments


    # Loan info - DATA FRAME
    # TODO: Add loan start date
    payments_year = 12
    interest_rate = interest_rate / 100
    loan_amount = purchase_price - (purchase_price*(down_payment/100))
    start_date = (date(2021,1,1))

    # Calculate monthly mortgage
    interest_monthly = float(interest_rate / 12)
    n = float(loan_term * 12)
    monthly_pmt = round(loan_amount * (interest_monthly * (1 + interest_monthly) ** n) / ((1 + interest_monthly) ** n - 1), 2)

    # Create a range for dates
    rng = pd.date_range(start_date, periods = loan_term * payments_year, freq = 'MS')
    rng.name = "Payment Date"

    # Mortgage DataFrame
    mortgage_df = pd.DataFrame(index = rng, columns = ['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance'],
                               dtype = 'float')
    mortgage_df.reset_index(inplace = True)
    mortgage_df.index += 1
    mortgage_df.index.name = "Period"
    mortgage_df['Payment'] = monthly_pmt + extra_payments
    mortgage_df['Principal Paid'] = -1*np.ppmt(interest_rate/payments_year, mortgage_df.index, loan_term * payments_year, loan_amount) + extra_payments

    mortgage_df = mortgage_df.round(2)
    mortgage_df.loc[1, "Interest Paid"] = loan_amount * interest_monthly
    mortgage_df['Ending Balance'] = 0
    mortgage_df.loc[1, "Ending Balance"] = loan_amount - mortgage_df.loc[1, "Principal Paid"]


    for period in range(2, len(mortgage_df)+1):

        mortgage_df.loc[period, 'Interest Paid'] = round(
            mortgage_df.loc[period - 1, "Ending Balance"] * (interest_monthly), 2)
        mortgage_df.loc[period,'Principal Paid'] = mortgage_df.loc[period,'Payment'] - mortgage_df.loc[period,'Interest Paid']
        previous_balance = mortgage_df.loc[period-1, "Ending Balance"]
        principal_paid = mortgage_df.loc[period, "Principal Paid"]

        if previous_balance == 0:
            mortgage_df.loc[period, ['Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance']] = 0
            continue
        elif principal_paid <= previous_balance:
            mortgage_df.loc[period, 'Ending Balance'] = previous_balance - principal_paid

    for period in range(2, len(mortgage_df) + 1):
        if mortgage_df.loc[period, "Interest Paid"] == 0 and mortgage_df.loc[period, "Ending Balance"] == 0:
            mortgage_df.drop(period, inplace=True)

    def EarlyPayoff(extra_payments):
        out = ''
        if extra_payments == 0:
            out = "You do not save any time if you don't put extra money in."
        if extra_payments != 0:
            months_saved = (loan_term * 12) - len(mortgage_df)
            years_saved = months_saved / 12
            out = "Your extra payment of $" + str(extra_payments) + "/month will save " + str(round(years_saved,2)) + " years off of your mortgage."
        return print(out)


    # BUYING and FIXING the place
    buy_income = aprsl_price - purchase_price
    fix_income = arv - aprsl_price - rehab_cost
    start_income = buy_income + fix_income

    # Up-front costs
    down_payment_cash = purchase_price * (down_payment/100)
    buy_closing_cost_cash = purchase_price * (buy_closing_cost / 100)
    first_rents = rent * 2
    total_up_front = down_payment_cash + buy_closing_cost_cash + first_rents + rehab_cost

    # Monthly Expenses
    taxes = ((prop_tax/100)*aprsl_price)/12
    ins = insurance/12
    repairs_monthly = rent*(repairs/100)
    vacant = rent * (vacancy/100)
    management = rent * (mgmt/100)
    monthly_expenses = monthly_pmt + taxes + ins + repairs_monthly + vacant + capex + hoa + management + other

    # Monthly Income
    monthly_income = rent + extra_income
    cash_flow = monthly_income - monthly_expenses
    cash_flow_unit = cash_flow / num_units
    CoCROI = ((cash_flow*12) / total_up_front)*100

    # Appreciation
    appreciation_array = []
    appreciation_array.append(float(arv))
    for year in range(40):
        appreciation_array.append(float(appreciation_array[-1])+(float(appreciation_array[-1])*(appreciation/100)))

    # Selling the property
    def SellProperty(years):
        payoff_time = loan_term # TODO: Add extra payments to mortgage and calculate total time to pay off and use here instead of entire loan term
        appreciation_array = []
        appreciation_array.append(float(arv))
        for year in range(40):
            appreciation_array.append(
                float(appreciation_array[-1]) + (float(appreciation_array[-1]) * (appreciation / 100)))
        sell_price = appreciation_array[years] - ((sell_closing_cost/100)*appreciation_array[years])
        cash_flow_total = 0
        if years <= payoff_time:
            cash_flow_total = cash_flow * 12 * years
            loan_left = mortgage_df.loc[int((years) * 12), "Ending Balance"]
        if years > payoff_time:
            cash_flow_total = (cash_flow*12*payoff_time) + ((cash_flow + monthly_pmt)*12*(years-payoff_time))
            loan_left = 0

        profit = sell_price + cash_flow_total - total_up_front - loan_left
        annual_profit = (profit)/years
        annual_roi = (annual_profit/total_up_front)*100
        return_string = "Selling your house after " + str(years) + " years results in a $" + str(round(profit,2)) + " profit. " \
                        "Your annual return would be $" + str(round(annual_profit, 2)) + " which is a yearly " + str(round(annual_roi,2)) + "% ROI."
        return print(return_string)


    # SELLING the place
    if output == "cash_flow":
        return print("Your cash flow is: $", round(cash_flow,2), "and your cash flow per unit is: $", round(cash_flow_unit,2),". Your fixed Cash on Cash ROI is: ", round(CoCROI,2), "%.")
    if output == "sell_year":
        return SellProperty(sell_year)
    if output == "early_payoff":
        return EarlyPayoff(extra_payments)



RentalCalculator(aprsl_price=110000, purchase_price=100000, arv=120000, buy_closing_cost=1.5, rehab_cost=3000,
                 appreciation=2, rent=1200, extra_income=50, prop_tax=2.35, insurance=1000, repairs=10, vacancy=5,
                 capex=185, mgmt=0, hoa=0, other=0, num_units=2, loan_term=30, interest_rate=3, down_payment=20,
                 extra_payments= 0, sell_closing_cost = 1.75, sell_year = 35, output = "sell_year")