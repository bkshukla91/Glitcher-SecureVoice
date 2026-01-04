import pandas as pd

def verify_caller_identity(phone_number):
    # Simulating a Global Fraud Database check
    fraud_database = {
        "140": "Spam/Telemarketing",
        "404": "Known Phishing Node",
        "999": "Verified Government/Bank"
    }
    
    prefix = str(phone_number)[:3]
    category = fraud_database.get(prefix, "Unverified/Unknown")
    
    is_fraud = category in ["Spam/Telemarketing", "Known Phishing Node"]
    trust_score = 15 if is_fraud else 85

    return {
        "category": category,
        "trust_score": trust_score,
        "reports": 412 if is_fraud else 0
    }