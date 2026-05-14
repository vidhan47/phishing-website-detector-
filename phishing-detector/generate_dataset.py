import pandas as pd
import numpy as np

# Number of samples
n = 2000

data = {
    "having_IP_Address": np.random.randint(0, 2, n),
    "URL_Length": np.random.randint(0, 2, n),
    "Shortining_Service": np.random.randint(0, 2, n),
    "having_At_Symbol": np.random.randint(0, 2, n),
    "double_slash_redirecting": np.random.randint(0, 2, n),
    "Prefix_Suffix": np.random.randint(0, 2, n),
    "having_Sub_Domain": np.random.randint(0, 2, n),
    "SSLfinal_State": np.random.randint(0, 2, n),
    "Domain_registeration_length": np.random.randint(0, 2, n),
    "Favicon": np.random.randint(0, 2, n),
    "port": np.random.randint(0, 2, n),
    "HTTPS_token": np.random.randint(0, 2, n),
    "Request_URL": np.random.randint(0, 2, n),
    "URL_of_Anchor": np.random.randint(0, 2, n),
    "Links_in_tags": np.random.randint(0, 2, n),
    "SFH": np.random.randint(0, 2, n),
    "Submitting_to_email": np.random.randint(0, 2, n),
    "Abnormal_URL": np.random.randint(0, 2, n),
    "Redirect": np.random.randint(0, 2, n),
    "on_mouseover": np.random.randint(0, 2, n),
    "RightClick": np.random.randint(0, 2, n),
    "popUpWidnow": np.random.randint(0, 2, n),
    "Iframe": np.random.randint(0, 2, n),
}

df = pd.DataFrame(data)

# Result
df["Result"] = (
    df["having_IP_Address"] |
    df["URL_Length"] |
    df["having_At_Symbol"] |
    df["double_slash_redirecting"]
).astype(int)

# save dataset
df.to_csv("dataset/phishing.csv", index=False)

print("Dataset generated successfully!")