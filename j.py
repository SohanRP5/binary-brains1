import instaloader
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def profile_user(username):
    try:
        # Fetch user profile information
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        # Fetch user posts
        user_posts = [post.caption for post in profile.get_posts() if post.caption is not None]

        # Check if the user has any non-empty posts
        if not user_posts:
            return "No Posts", 0

        # Profile user based on sentiment analysis
        sentiments = [analyze_sentiment(post) for post in user_posts]
        average_sentiment = sum(sentiments) / len(sentiments)
        risk = average_sentiment * 100

        if risk >= 20:
            return "High Risk", risk
        elif -20 < risk < 20:
            return "Medium Risk", risk
        else:
            return "Low Risk", risk

    except instaloader.exceptions.ProfileNotExistsException as e:
        return f"Error: {e}", 0

if _name_ == "_main_":
    # Replace 'target_username' with the Instagram username you want to analyze
    username_to_analyze = 'drpiyushkumarsoni'

    # Profile the user and print the risk level
    risk_level, risk_percentage = profile_user(username_to_analyze)
    print(f"User: {username_to_analyze}")
    print(f"Risk Level: {risk_level}")
    print(f"Risk Percentage: {risk_percentage:.2f}%")