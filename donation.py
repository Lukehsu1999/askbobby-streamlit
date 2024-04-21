import streamlit as st
import json

col1, col2 = st.columns([7,3])

with col1:
    # Define data for multiple rows of cards
    data = [
        {"title": "Food for East Harlem", "description": "Bobby received an increasing food requests in East Harlem area.", "icon_url":"https://cdn-icons-png.flaticon.com/512/706/706164.png"}, 
        {"title": "Refugees Health Fund", "description": "Bobby spotted a 120% increase in health requests from refugees in NYC.", "icon_url":"https://cdn-icons-png.flaticon.com/512/3004/3004458.png"},
        {"title": "Fresh food Program NYC", "description": "Based on 120+ user feedback, people are looking for fresh vegetables and fruits replacing canned foods", "icon_url":"https://cdn-icons-png.flaticon.com/512/706/706164.png"}, 
        {"title": "Building a new shelter @Greater South Bronx", "description": "Over the last 2 weeks, Bobby received 100+ requests for shelter in Greater South Bronx.", "icon_url":"https://cdn-icons-png.flaticon.com/512/4165/4165944.png"},
        {"title": "Spanish-speaking Volunteers needed @Queens", "description": "Food Pantries in Queens area reported a 30% increase in Spanish-speaking clients. Volunteers familiar with Spanish are needed.", "icon_url":"https://cdn-icons-png.flaticon.com/128/10710/10710939.png"}
    ]

    with st.container(border=True):
        st.subheader("Current Projects:")
        st.markdown("""
            <style>
            .card {
                background-color: #ffffff; /* White background */
                border: 2px solid #e1e4e8; /* Solid border with light gray color */
                border-radius: 10px; /* Rounded corners */
                padding: 10px; /* Padding inside the card */
                margin-top: 0px; /* Increased top margin */
                margin-bottom: 10px; /* Bottom margin */
                margin-right: 10px; /* Right margin */
                margin-left: 10px; /* Left margin */
                box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow around the card */
            }
            .button {
                display: block;
                width: 100%;
                padding: 8px;
                margin: 10px 0;
                background-color: #007BFF;
                color: white;
                text-align: center;
                border-radius: 5px;
                text-decoration: none;
            }
            </style>
            """, unsafe_allow_html=True)

        # Loop through each row of cards
        for card in data:
            # Create a full card's HTML content
            card_html = f"""
            <div class='card'>
                <img src="{card.get('icon_url', 'https://cdn-icons-png.flaticon.com/512/1046/1046784.png')}" style="width: 50px; height: 50px; float: left; margin-right: 10px;">
                <h2>{card['title']}</h2>
                <p>{card['description']}</p>
                <button class='button' onclick="alert('Clicked {card['title']}!');">Donate</button>
            </div>

            """
            st.markdown(card_html, unsafe_allow_html=True)

with col2:
    state_abbreviations = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    # Define the standard deductions based on filing status
    standard_deductions = {
        5: 0,        # Nonresident Alien
        1: 14600,    # Single
        2: 29200,    # Married filing jointly
        3: 14600,    # Married filing separately
        4: 21900     # Head of household
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
        for limit, rate in sorted(brackets, reverse=True):
            if income > limit:
                tax += (income - limit) * rate
                income = limit
        return tax

    # Main calculation function including charity
    def calculate_taxes(income, other_itemized_deductions, filing_status, charity):
        # Define standard deductions
        standard_deductions = {
            5: 0,        # Nonresident Alien
            1: 14600,    # Single
            2: 29200,    # Married filing jointly
            3: 14600,    # Married filing separately
            4: 21900     # Head of household
        }
        
        standard_deduction = standard_deductions[filing_status]
        taxable_income_pre_charity = income - standard_deduction
        taxable_income_post_charity = income - max(min(charity, 0.6 * income) + other_itemized_deductions, standard_deduction)

        federal_tax_pre_charity = calculate_federal_tax(taxable_income_pre_charity, filing_status)
        federal_tax_post_charity = calculate_federal_tax(taxable_income_post_charity, filing_status)

        total_federal_savings = federal_tax_pre_charity - federal_tax_post_charity

        return {
            "Estimated Federal Tax Savings from the Donation": total_federal_savings
        }
    with st.container(border=True):
        st.subheader('Charity Tax Deduction Calculator')
        state = st.selectbox('Select your state', [''] + sorted(state_abbreviations))
        zip_code = st.text_input('Enter your ZIP Code')
        filing_status = st.selectbox('Select your filing status', list(standard_deductions.keys()), format_func=lambda x: {1: 'Single', 2: 'Married filing jointly', 3: 'Married filing separately', 4: 'Head of household', 5: 'Nonresident Alien'}[x])
        income = st.number_input('Estimated Annual Gross Income', min_value=0.0, step=1000.0, value=100000.0)
        other_itemized_deductions = st.number_input('Other itemized deductions (if any):', min_value=0.0, step=100.0, value=0.0, format='%.2f')

        standard_deduction = standard_deductions[filing_status]
        st.write(f"Consider combining multi-year donations into one to maximize potential tax savings.")

        total_itemized_deductions = other_itemized_deductions
        recommended_charity = max(0.03 * income, 2 * (standard_deduction - total_itemized_deductions))  # Ensure this is a float
        charity = st.number_input('Your Intended Donation', min_value=0.0, step=100.0, value=float(recommended_charity))  # Convert to float

        if total_itemized_deductions + charity <= standard_deduction:
            st.write(f"Your standard deduction is: ${standard_deduction:,}. We recommend increasing your intended donation to exceed your standard deduction to receive potential tax savings.")

        if st.button('Calculate'):
            if state and income > 0:
                results = calculate_taxes(income, other_itemized_deductions, filing_status, charity)
                st.write(f"**Extra Tax Savings (Federal) from Donation:** ${results['Estimated Federal Tax Savings from the Donation']:,}")
            else:
                st.error("Please fill in all the fields. Contact us if you have a special case.")


# with open('wave.css') as f:
#     css = f.read()

# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)