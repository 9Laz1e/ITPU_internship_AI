import streamlit as st


company_details = {
    "working_hours": "Mon–Fri: 9:00 AM – 5:00 PM",
    "address": "114A Makhtumkuli Street",
    "phone_number": "+55 520-40-00",
    "email_address": "info@itpu.uz"
}


def respond_to_query(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["hours", "working", "time", "open"]):
        return f"Our working hours are: {company_details['working_hours']}"
    elif any(keyword in user_input for keyword in ["location", "address", "where"]):
        return f"We are located at: {company_details['address']}"
    elif any(keyword in user_input for keyword in ["phone", "call", "number"]):
        return f"You can reach us at: {company_details['phone_number']}"
    elif any(keyword in user_input for keyword in ["email", "contact", "write"]):
        return f"Our email address is: {company_details['email_address']}"
    else:
        return "Sorry, I couldn't understand your question. Please try rephrasing it."


st.title("📌 Ask ITPU Assistant")

user_question = st.text_input("Ask a question about ITPU:")

if st.button("Submit"):
    result = respond_to_query(user_question)
    st.info(result)