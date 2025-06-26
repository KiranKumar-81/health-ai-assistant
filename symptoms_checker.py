def check_symptoms(user_input):
    symptoms = {
        "fever": "Could indicate flu, COVID-19, or an infection.",
        "headache": "May be due to migraine, stress, or dehydration.",
        "cough": "Could relate to bronchitis, asthma, or common cold.",
        "fatigue": "Possibly linked to anemia, depression, or thyroid issues."
    }
    suggestions = [desc for word, desc in symptoms.items() if word in user_input.lower()]
    return suggestions if suggestions else ["No matches found. Please consult a doctor for accurate advice."]
