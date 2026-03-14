import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ---------------- LOAD MODEL ---------------- #

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained("project_files/tokenizer_directory")

    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )

    state_dict = torch.load(
        "project_files/model.path",
        map_location=torch.device("cpu")
    )

    model.load_state_dict(state_dict)

    model.eval()

    return tokenizer, model


tokenizer, model = load_model()


# ---------------- PREDICTION FUNCTION ---------------- #

def predict_url(url):

    inputs = tokenizer(
        url,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    prediction = torch.argmax(logits).item()

    if prediction == 1:
        return "Phishing"
    else:
        return "Safe"


# ---------------- STREAMLIT APP ---------------- #

def app():

    st.set_page_config(page_title="DigitalRaksha", page_icon="🛡️", layout="centered")

    st.title("🛡️ DigitalRaksha")
    st.subheader("Your Smart Phishing URL Detection Assistant")

    st.markdown("---")

    user_url = st.text_input("🔗 Enter URL")

    if st.button("Analyze"):

        if user_url.strip() == "":
            st.warning("Please enter a URL")

        else:
            result = predict_url(user_url)

            if result == "Safe":
                st.success("🟢 URL is SAFE")
            else:
                st.error("🔴 URL is PHISHING")

    st.markdown("---")
    st.write("Stay Safe with DigitalRaksha")


if __name__ == "__main__":
    app()