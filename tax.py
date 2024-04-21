import streamlit as st

# Dictionary of state names
state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Define the standard deductions based on filing status
standard_deductions = {
    1: 14600,   # Single
    2: 29200,   # Married filing jointly
    3: 14600,   # Married filing separately
    4: 21900,   # Head of household
    5: 0        # Nonresident Alien
}

# Federal tax brackets for 2024
tax_brackets = {
    1: [(609350, 0.37), (243725, 0.35), (191950, 0.32), (100525, 0.24), (47150, 0.22), (11600, 0.12), (0, 0.10)],
    2: [(731200, 0.37), (487450, 0.35), (383900, 0.32), (201050, 0.24), (94300, 0.22), (23200, 0.12), (0, 0.10)],
    3: [(609350, 0.37), (243725, 0.35), (191950, 0.32), (100525, 0.24), (47150, 0.22), (11600, 0.12), (0, 0.10)],
    4: [(609350, 0.37), (243700, 0.35), (191950, 0.32), (100500, 0.24), (63100, 0.22), (16550, 0.12), (0, 0.10)],
    5: [(609350, 0.37), (243725, 0.35), (191950, 0.32), (100525, 0.24), (47150, 0.22), (11600, 0.12), (0, 0.10)]
}

# Calculate federal tax based on income and filing status
def calculate_federal_tax(income, filing_status):
    brackets = tax_brackets[filing_status]
    tax = 0
    for limit, rate in brackets:
        if income > limit:
            tax += (income - limit) * rate
            income = limit
    return tax

# Main calculation function including charity
def calculate_taxes(income, state, filing_status, charity):
    federal_tax_pre_charity = calculate_federal_tax(income - standard_deductions[filing_status], filing_status)
    federal_tax_post_charity = calculate_federal_tax(income - max(min(charity, 0.6 * income),standard_deductions[filing_status]), filing_status)

    total_federal_pre = federal_tax_pre_charity
    total_federal_post = federal_tax_post_charity
    total_federal_savings = total_federal_pre - total_federal_post

    return {
        "Estimated Federal Tax Savings from the Donnation": total_federal_savings
    }

# Streamlit webpage setup
st.title('Charity Tax Deduction Calculator')

# Input fields
state = st.selectbox('Select your state', [''] + sorted(state_abbreviations))
filing_status = st.selectbox('Select your filing status', list(standard_deductions.keys()), format_func=lambda x: {1: 'Single', 2: 'Married filing jointly', 3: 'Married filing separately', 4: 'Head of household', 5: 'Nonresident Alien'}[x])
income = st.number_input('Estimated Annual Gross Income', min_value=0.0, step=1000.0, value=100000.0)
# Display the standard deduction based on the selected filing status
standard_deduction = standard_deductions[filing_status]
st.write(f"Your standard deduction is: ${standard_deduction}")
# Input for estimated itemized deductions before charity
other_itemized_deductions = st.number_input('Enter your estimated itemized deductions before donnation:', min_value=0.0, step=100.0, format='%.2f')
charity = st.number_input('Charity Expense', min_value=0.0, step=100.0, value=5000.0)

if st.button('Calculate'):
    if state and income > 0:
        results = calculate_taxes(income, state, filing_status, charity)
        st.write(f"**Estimated Tax Savings (Federal) from Donnation:** ${results['Estimated Federal Tax Savings from the Donnation']:.2f}")
    else:
        st.error("Please fill in all the fields. Contact us if you have a special case.")