import re

def extract_features(url):
    features = []

    # 1. Having IP Address
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # 2. URL Length
    features.append(1 if len(url) > 75 else 0)

    # 3. Shortening service
    features.append(1 if "bit.ly" in url or "tinyurl" in url else 0)

    # 4. @ symbol
    features.append(1 if "@" in url else 0)

    # 5. Double slash redirect
    features.append(1 if "//" in url[7:] else 0)

    # 6. Prefix-Suffix (- in domain)
    features.append(1 if "-" in url else 0)

    # 7. Subdomain
    features.append(1 if url.count('.') > 2 else 0)

    # 8. HTTPS
    features.append(1 if "https" in url else 0)

    # Fill remaining features with 0 (to match training columns)
    while len(features) < 23:
        features.append(0)

    return features