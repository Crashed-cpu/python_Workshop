import time
import random
import string

def generate_random_sentence(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def default_mode():
    sentence = generate_random_sentence(50)
    print("Type the following sentence as fast as you can:")
    print(sentence)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    accuracy = sum(1 for a, b in zip(sentence, user_input) if a == b) / len(sentence) * 100
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

def custom_mode():
    num_lines = int(input("Enter the number of lines: "))
    char_variation = int(input("Enter the variation in characters: "))
    for _ in range(num_lines):
        sentence = generate_random_sentence(char_variation)
        print("Type the following sentence as fast as you can:")
        print(sentence)
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        time_taken = end_time - start_time
        accuracy = sum(1 for a, b in zip(sentence, user_input) if a == b) / len(sentence) * 100
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Accuracy: {accuracy:.2f}%")

def main():
    mode = input("Enter 'default' for default mode or 'custom' for custom mode: ").strip().lower()
    if mode == 'default':
        default_mode()
    elif mode == 'custom':
        custom_mode()
    else:
        print("Invalid mode selected. Please restart the program.")

if __name__ == "__main__":
    main()
