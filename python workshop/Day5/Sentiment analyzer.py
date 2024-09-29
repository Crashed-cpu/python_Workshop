from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Your existing code

Analyzer = SentimentIntensityAnalyzer()

def analyze(text):
    try:
        sentiment= Analyzer.polarity_scores(text)

        print(f"\nOverall Product is rated as ")

        if sentiment["compound"] >= 0.05:
            print("positive")

        elif sentiment["compound"] <= -0.05:
            print("Negative")

        else:
            print("Neutral")
        
        print("")
        
    except Exception as e:
        print(e)

Text = input("Please enter a text: ")

analyze(Text)