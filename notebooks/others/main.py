import sys
import csv
from statistics import mean

def calculate_mean_variance(scores):
    n = len(scores)
    if n == 0:
        return 0.0, 0.0

    scores_mean = mean(scores)
    variance = sum((x - scores_mean) ** 2 for x in scores) / n
    return scores_mean, variance

def main(argv):
    if len(argv) != 1:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = argv[0]

    correct_headers = ['ID', 'Mathematics', 'Japanese']
    math_scores = []
    japanese_scores = []

    try:
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)

            # Clean and normalize headers
            headers = [header.strip() for header in headers]
            headers = ['Mathematics' if header.lower().replace(' ', '') in ['mathmatics', 'mathematics'] else header for header in headers]

            if headers != correct_headers:
                print("Error: CSV headers do not match the expected format.")
                sys.exit(1)

            for row in reader:
                math_score = row[1].strip()
                japanese_score = row[2].strip()

                if math_score != 'NULL':
                    math_scores.append(float(math_score))
                if japanese_score != 'NULL':
                    japanese_scores.append(float(japanese_score))

        math_mean, math_variance = calculate_mean_variance(math_scores)
        japanese_mean, japanese_variance = calculate_mean_variance(japanese_scores)

        print(f"math_mean: {math_mean}")
        print(f"math_variance: {math_variance}")
        print(f"japanese_mean: {japanese_mean}")
        print(f"japanese_variance: {japanese_variance}")

    except FileNotFoundError:
        print(f"Error: Could not find file {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print(sys.argv[1:])
    main(sys.argv[1:])
