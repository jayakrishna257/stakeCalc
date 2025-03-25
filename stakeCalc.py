import streamlit as st

# Title of the app
st.title("Stake Calculator")

# Input for Favor odds
fOdds = st.number_input("Enter Favor odds:", min_value=0.0, step=0.01)

# Input for Underdog odds
uOdds = st.number_input("Enter Underdog odds:", min_value=0.0, step=0.01)

# Input for Favor stake
s1 = st.number_input("Enter Favor stake:", min_value=0.0, step=0.01)

# Input for Underdog stake
tmp = st.text_input("Enter Underdog stake (leave blank for recommendation):")

# Calculate returns from Favor trade
r1 = float(s1 * fOdds)

# Recommended stake for underdog trade
if tmp == "":
    s2 = round(float(((s1 * fOdds) / uOdds)), 1)
else:
    s2 = float(tmp)

# Calculate returns from Underdog trade
r2 = round(float(s2) * uOdds, 1)

# Total stake
totalStake = s1 + s2

# Calculating the final P/L
favorResult = round(r1 - totalStake, 1)
underdogResult = round(r2 - totalStake, 1)

# Determine the final outcome
final = round(favorResult, 1) if favorResult < underdogResult else round(underdogResult, 1)

# Display results
st.write(f"Favor Stake is: {s1} and the returns at odds of {fOdds} are {r1}. If this is the outcome, the P/L will be: {favorResult}.")
st.write(f"Stake 2 should be: {s2} and the returns at odds of {uOdds} are {r2}. If this is the outcome, the P/L will be: {underdogResult}.")
st.write(f"Total Stake is: {totalStake}.")
st.write(f"Typical outcome at worst will be: {final}.")