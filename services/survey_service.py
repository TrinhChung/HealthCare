def get_intro_text():
    return "Chào mừng bạn đến với bài khảo sát sức khỏe. Vui lòng trả lời một số câu hỏi sau để chúng tôi có thể phân tích."

def generate_health_prompt(survey):
    gender = "Nam" if survey.gender == "male" else "Nữ"
    chronic = "có" if survey.has_chronic_disease else "không"
    smoking = "có" if survey.smoking else "không"

    prompt = (
        f"Tôi {survey.age} tuổi, giới tính {gender}, "
        f"{chronic} bệnh nền và {smoking} hút thuốc. "
        f"Bạn có thể phân tích giúp tôi những rủi ro sức khỏe tôi có thể gặp phải "
        f"và đưa ra lời khuyên phù hợp không?"
    )

    return prompt