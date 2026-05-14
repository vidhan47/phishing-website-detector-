import joblib
import pandas as pd
from utils.feature_extraction import extract_features

# Load model
model = joblib.load("models/model.pkl")

# Feature names (same as training dataset)
feature_names = [
    "having_IP_Address", "URL_Length", "Shortining_Service",
    "having_At_Symbol", "double_slash_redirecting", "Prefix_Suffix",
    "having_Sub_Domain", "SSLfinal_State", "Domain_registeration_length",
    "Favicon", "port", "HTTPS_token", "Request_URL", "URL_of_Anchor",
    "Links_in_tags", "SFH", "Submitting_to_email", "Abnormal_URL",
    "Redirect", "on_mouseover", "RightClick", "popUpWidnow", "Iframe"
]

def predict_url(url):
    features = extract_features(url)

    # Convert to DataFrame with column names
    df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(df)[0]

    return "Phishing" if prediction == 1 else "Legitimate"