from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# UPDATED mock sentiment tweets for better variation
sample_tweets = {
    "AAPL": [
        "Apple stock is absolutely crushing it! 📈",
        "The new iPhone is a game changer.",
        "Apple has reported record-breaking earnings."
    ],
    "TSLA": [
        "Tesla is facing lawsuits and production delays.",
        "Elon Musk's decisions are hurting Tesla's brand.",
        "Investors are worried about Tesla's future."
    ],
    "NVDA": [
        "NVIDIA's AI chips are dominating the tech industry!",
        "Huge earnings beat by NVIDIA today.",
        "NVIDIA is a top pick for 2025 investors."
    ],
    "AMZN": [
        "Amazon sales are declining this quarter.",
        "Delivery issues are frustrating customers.",
        "Layoffs continue at Amazon HQ."
    ],
    "GOOGL": [
        "Google launches revolutionary AI tools!",
        "Alphabet's innovations are setting new standards.",
        "Search engine updates are super impressive."
    ],
    "MSFT": [
        "Microsoft is stable this quarter.",
        "Not much movement seen in Microsoft stock.",
        "Let’s wait and watch how Microsoft performs."
    ]
}

def analyze_sentiment(symbol):
    tweets = sample_tweets.get(symbol.upper(), [
        "This stock is unpredictable.",
        "It's a risky investment!",
        "Could go either way."
    ])

    analyzer = SentimentIntensityAnalyzer()
    total_score = 0

    for tweet in tweets:
        score = analyzer.polarity_scores(tweet)['compound']
        # Uncomment the line below to print tweet sentiment scores
        # print(f"Tweet: {tweet} | Score: {score}")
        total_score += score

    avg_score = total_score / len(tweets)

    # Slightly tweaked thresholds for better variation
    if avg_score > 0.05:
        return "Positive"
    elif avg_score < -0.05:
        return "Negative"
    else:
        return "Neutral"


