import streamlit as st

def calculate_required_sgpa(current_cgpa, required_cgpa, total_credits_done, current_sem_credits):
    numerator = (required_cgpa * (total_credits_done + current_sem_credits)) - (total_credits_done * current_cgpa)
    required_sgpa = numerator / current_sem_credits
    return round(required_sgpa, 2)

# Streamlit UI
st.title("🎓 Required SGPA Calculator")

st.markdown("""
This tool helps you calculate the SGPA required in the **current semester** to reach your **target CGPA**.
""")

current_cgpa = st.number_input("Enter your current CGPA", min_value=0.0, max_value=10.0, step=0.01)
required_cgpa = st.number_input("Enter your target CGPA", min_value=0.0, max_value=10.0, step=0.01)
total_credits_done = st.number_input("Total credits completed so far (excluding current semester)", min_value=0.0, step=1.0)
current_sem_credits = st.number_input("Total credits in the current semester", min_value=0.0, step=1.0)

if st.button("Calculate Required SGPA"):
    if current_sem_credits == 0:
        st.error("Current semester credits cannot be zero.")
    else:
        required_sgpa = calculate_required_sgpa(current_cgpa, required_cgpa, total_credits_done, current_sem_credits)
        if required_sgpa > 10:
            st.warning(f"You need an SGPA of {required_sgpa}, which exceeds the maximum possible SGPA. Reaching your target CGPA may not be feasible this semester.")
        elif required_sgpa < 0:
            st.success("You have already surpassed your target CGPA. Just maintain your performance!")
        else:
            st.success(f"You need an SGPA of at least **{required_sgpa}** this semester to reach a CGPA of **{required_cgpa}**.")
