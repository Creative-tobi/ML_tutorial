# tweets = [
#     "I am having a great day",
#     "I feel so hopeless and sad.",
#     "I want to sleep and never wake up.",
#     "Eating rice and chicked."
# ]

# trigger_words = ["hopeless", "sad", "never wake up", "die"]

# print("--- StARTING ANALYSIS ---")

# for tweet in tweets:
#     is_danger = False

#     for word in trigger_words:
#         if word in tweet.lower():
#             is_danger = True
#             break

#     if is_danger:
#         print(f"ALERT: {tweet}")
#     else:
#         print(f"SAFE: {tweet}")        

# print("---ANALYSIS COMPLETE---")  

# depression checker

# def get_depression_schore(tweet):
#     clean_text = tweet.lower()

#     score = 0
#     if "sad" in clean_text:
#         score = score + 5
    
#     if "hopeless" in clean_text:
#         score = score + 10

#     if "die" in clean_text:
#         score = score + 20

#     return score

# tweets = [
#     "I am having a great day",
#     "I feel so hopeless and die.",
#     "I want to sleep and never wake up.",
#     "Eating rice and chicked."
# ]

# print ("---SCORING SYSTEM---")
# for t in tweets:
#     final_score = get_depression_schore(t)

#     if final_score >= 20:
#         status = "SEVERE DANGER"
#     elif final_score >= 5:
#         status = "MODERATE RISK"
#     else:
#         status = "SAFE"

#     print(f"Score: {final_score} | Status: {status}| Tweet: {t}") 

#payload bot deector
def check_for_bot(user_data):
    if user_data['age'] < 3:
        return "BOT (Too New)"
    
    bio_text = user_data['bio'].lower()

    if "giveaway" in bio_text or "crypto" in bio_text:
        return "BOT (Spam Bio)"
    
    return "HUMAN"


user_db = [
    {"name": "Ade", "age": 40, "bio": "Student loving python"},
    {"name": "ScamKing", "age": 1, "bio": "I love coding"},
    {"name": "ElonMusk_Fake", "age": 10, "bio": "Click link for CRYPTO giveaway"}
]

print("---SECURITY SCAN STARTING---")
for user in user_db:
    status = check_for_bot(user)

    print(f"User: {user['name']} | Verdict: {status}")
