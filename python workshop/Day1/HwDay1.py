# Define a list of tuples, where each tuple contains a student's name and their scores in three subjects
students_scores = [
    ("Alice", [85, 92, 78]),
    ("Bob", [79, 95, 88]),
    ("Charlie", [92, 87, 85])
]

# Create an empty dictionary to store the average scores
average_scores = {}

# Calculate the average score for each student and store it in the dictionary
for student, scores in students_scores:
    average = sum(scores) / len(scores)
    average_scores[student] = average

# Print the average scores
print("Average Scores:")
for student, average in average_scores.items():
    print(f"{student}: {average:.2f}")

# Find the student with the highest average score
top_student = max(average_scores, key=average_scores.get)
print(f"\nTop Student: {top_student} with an average score of {average_scores[top_student]:.2f}")
