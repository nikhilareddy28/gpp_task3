import csv
import time
import random
import string
from custom_csv import CustomCsvReader, CustomCsvWriter





def generate_large_csv(filename, rows=1_000_000):
    import random, string, csv
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            row = [
                ''.join(random.choices(string.ascii_letters, k=10)),
                random.randint(1, 1000000),
                random.uniform(1.0, 9999.9)
            ]
            writer.writerow(row)

def generate_random_string(length=10):
    """Generate a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def generate_csv_file(file_path, rows=10000, cols=5):
    """Generate a CSV file with synthetic data."""
    writer = CustomCsvWriter()
    data = [[generate_random_string() for _ in range(cols)] for _ in range(rows)]
    writer.write(file_path, data)
    print(f"Generated test CSV file: {file_path}")


def benchmark_reader(file_path):
    """Benchmark custom reader vs standard csv.reader."""
    print("\n--- Reader Benchmark ---")

    # Benchmark CustomCsvReader
    start = time.time()
    for row in CustomCsvReader(file_path):
        pass
    custom_time = time.time() - start

    # Benchmark Python csv.reader
    start = time.time()
    with open(file_path, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            pass
    standard_time = time.time() - start

    print(f"Custom Reader Time:   {custom_time:.4f} sec")
    print(f"Python csv.reader:    {standard_time:.4f} sec")


def benchmark_writer(input_file, output_file):
    """Benchmark custom writer vs Python csv.writer."""
    print("\n--- Writer Benchmark ---")

    # Read data using standard csv module
    with open(input_file, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    # Custom writer
    start = time.time()
    CustomCsvWriter().write(output_file, rows)
    custom_time = time.time() - start

    # Standard writer
    start = time.time()
    with open("standard_output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    standard_time = time.time() - start

    print(f"Custom Writer Time:   {custom_time:.4f} sec")
    print(f"Python csv.writer:    {standard_time:.4f} sec")


if __name__ == "__main__":
    print("Generating sample CSV...")
    generate_csv_file("test.csv", rows=10000, cols=5)

    benchmark_reader("test.csv")
    benchmark_writer("test.csv", "custom_output.csv")

print("\nGenerating LARGE CSV (1,000,000 rows)...")
generate_large_csv("big.csv")
print("Large CSV generation done: big.csv")

# Benchmark on large file
print("\n--- Large File Reader Benchmark (1M rows) ---")
start = time.time()
for row in CustomCsvReader("big.csv"):
    pass
end = time.time()
print("Custom Reader Time:", f"{end - start:.4f} sec")

start = time.time()
with open("big.csv", newline='') as f:
    for row in csv.reader(f):
        pass
end = time.time()
print("Python csv.reader:", f"{end - start:.4f} sec")

