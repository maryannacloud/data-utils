from data_utils.fixed_width import detect_column_positions, parse_fixed_width_file
from pathlib import Path

def main():
    # Adjust this path if needed
    file_path = Path("data/payment-data.txt")

    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    print(f"📂 Analyzing file: {file_path}")

    column_ranges = detect_column_positions(str(file_path), sample_size=10)

    if not column_ranges:
        print("⚠️ No columns detected.")
    else:
        print("✅ Detected column positions:\n")
        for idx, (start, end) in enumerate(column_ranges, 1):
            width = end - start + 1
            print(f"  Column {idx}: Start = {start}, End = {end}, Width = {width}")

    print("\n📋 Sample parsed rows:")
    rows = parse_fixed_width_file(str(file_path), column_ranges)
    for row in rows[:5]:
        print(row)

if __name__ == "__main__":
    main()
