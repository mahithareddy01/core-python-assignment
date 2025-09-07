def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)
ratings_input = input("Enter ratings (1-5) separated by space: ")
ratings = list(map(int, ratings_input.split()))
result = positive_feedback_percentage(ratings)
print(f"Positive Feedback: {result}%")