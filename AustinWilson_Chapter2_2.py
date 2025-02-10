# Austin Wilson Chater 2 Assignment 2 Scam Emails

def search_for_keywords():

# stores keywords for further use
    return [
        "act now", "save money", "best price", "big bucks", "click here",
        "congratulations", "double your income", "huge savings", "earn extra cash",
        "eliminate debt", "exclusive deal", "free access", "free consultation",
        "free gift", "free trial", "guarantee", "increase sales", "limited time",
        "lose weight", "lowest price", "make money", "money back", "no cost",
        "order now", "risk-free", "special promotion", "urgent", "weight loss",
        "win big", "winner"

    ]
# calculates spam score based on number of spam keywords, returns spam score and list of keywords
def spam_score_finder(email_message, spam_keywords):

    spam_score = 0
    found_keywords = []
# makes text lowercase for easy matching
    email_text_lower = email_message.lower()

    for keyword in spam_keywords:
        if keyword in email_text_lower:
            spam_score += 1
            found_keywords.append(keyword)

    return spam_score, found_keywords
# uses an elif to rate likelihood of spam
def rate_spam_likelihood(spam_score, total_keywords):

    if spam_score == 0:
        return "Not Spam"
    elif spam_score <= total_keywords * 0.2:
        return "Unlikely to be Spam"
    elif spam_score <= total_keywords * 0.5:
        return "Possible to be Spam"
    else:
        return "Likely Spam"
# handles inputs
def main():
# gets list
    spam_keywords = search_for_keywords()
# prompts entry for email
    email_message = input("Enter email message:\n")
# calculates spam score and keywords
    spam_score, found_keywords = spam_score_finder(email_message, spam_keywords)
# rates likelihood
    spam_likelihood = rate_spam_likelihood(spam_score, len(spam_keywords))
# prints
    print("\nSpam Test Results:")
    print(f"Spam Score: {spam_score}")
    print(f"Spam Likelihood: {spam_likelihood}")
    if found_keywords:
        print("Detected Spam Phrases:")
        for keyword in found_keywords:
            print(f"- {keyword}")




main()








