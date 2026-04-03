def get_response(text):
    text = text.lower()

    if "chest pain" in text or "breathing problem" in text:
        return "🚨 Emergency! Please go to the nearest hospital immediately."

    elif "sad" in text or "depressed" in text:
        return "😟 You seem stressed. Talk to someone you trust and take rest."

    elif "happy" in text:
        return "😊 Great to hear that! Stay healthy!"

    elif "fever" in text:
        return "🤒 You may have a fever. Drink fluids and take rest."

    elif "headache" in text:
        return "💊 Headache may be due to stress or dehydration. Take rest."

    else:
        return "⚕️ Please provide more details for better assistance."
