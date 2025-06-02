def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def generate_report(data):
    # Placeholder for report generation logic
    return f"Report generated with {len(data)} entries."

def extract_keywords(text, num_keywords=5):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return keywords[:num_keywords]