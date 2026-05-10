from .prompts import RESPONSES


def generate_insight(feature_name, value):
    if feature_name in RESPONSES and value in RESPONSES[feature_name]:
        return RESPONSES[feature_name][value]
    return None


def generate_full_response(data, prediction, risk):
    paragraphs = []

    if risk == "Low":
        paragraphs.append("Your depression screening score is low, which suggests you're currently in a good mental state. However, mental health exists on a spectrum, and small changes in your daily habits can help maintain this wellbeing. Let's go through each area of your life that we assessed and see where you stand.")
    elif risk == "Moderate":
        paragraphs.append("Your screening indicates a moderate level of depression risk. This means some areas of your life may be contributing to emotional distress. You're not alone \u2014 many university students experience similar feelings. The good news is that moderate depression responds very well to lifestyle changes and support. Let's break down what might be affecting you.")
    else:
        paragraphs.append("Your screening indicates a high risk of depression. Please take this seriously \u2014 not with fear, but with the understanding that depression is a real, treatable medical condition. It's not a character flaw or a weakness. Many students experience what you're going through, and most recover with proper support. I strongly recommend reaching out to a mental health professional. Below, I'll walk through what might be contributing to how you feel.")

    feature_order = [
        ("sleep_duration_hours", "Sleep"),
        ("social_media_hours_daily", "Social Media Use"),
        ("physical_activity", "Physical Activity"),
        ("financial_pressure", "Financial Pressure"),
        ("has_debt", "Debt"),
        ("social_economic_status", "Economic Background"),
        ("academic_work_demands", "Academic Pressure"),
        ("living_environment_satisfaction", "Living Environment"),
        ("recent_loss", "Recent Loss"),
        ("alcohol", "Alcohol Use"),
        ("smoking", "Smoking"),
        ("medication", "Medication"),
    ]

    for feature, label in feature_order:
        value = getattr(data, feature, None)
        if value:
            insight = generate_insight(feature, value)
            if insight:
                paragraphs.append(f"**{label}:** {insight}")

    if risk == "Low":
        paragraphs.append("You're doing well overall. The best approach now is prevention \u2014 maintain your sleep routine, stay physically active, nurture your relationships, and manage stress proactively. Consider this screening a baseline. If anything changes in how you feel, don't hesitate to seek support early.")
    elif risk == "Moderate":
        paragraphs.append("Moderate depression is your mind's way of signaling that something needs attention. Start with one area \u2014 sleep is usually the best foundation. If symptoms persist for more than two weeks or interfere with your daily life, please speak with a counselor. Most universities offer free, confidential counseling services. You deserve support.")
    else:
        paragraphs.append("If you're feeling overwhelmed right now, please know: this is treatable. Depression lies to you \u2014 it tells you there's no way out. That's the illness talking, not reality. Reach out to someone you trust today. Call your university counseling center. If you're having thoughts of harming yourself, contact a crisis helpline immediately. You matter. Your life matters. And this feeling won't last forever.")

    return "\n\n".join(paragraphs)

