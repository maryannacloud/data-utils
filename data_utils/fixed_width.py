from typing import List, Tuple

def detect_column_positions(file_path: str, sample_size: int = 10) -> List[Tuple[int, int]]:
    """
    Detects start and end character positions of columns in a fixed-width text file.

    Args:
        file_path: Path to the fixed-width text file.
        sample_size: Number of lines to analyze (default: 10).

    Returns:
        A list of (start, end) tuples representing column character positions.
    """
    positions: List[Tuple[int, int]] = []

    with open(file_path, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()[:sample_size]]

    if not lines:
        return []

    max_len = max(len(line) for line in lines)

    # Track column starts and ends
    column_ranges = []
    in_column = False
    start = 0

    for i in range(max_len):
        chars = [line[i] if i < len(line) else ' ' for line in lines]
        is_space = all(c.isspace() for c in chars)

        if not is_space and not in_column:
            start = i
            in_column = True
        elif is_space and in_column:
            column_ranges.append((start, i - 1))
            in_column = False

    if in_column:
        column_ranges.append((start, max_len - 1))

    return column_ranges

def parse_fixed_width_file(file_path: str, column_ranges: List[Tuple[int, int]]) -> List[List[str]]:
    """
    Parses a fixed-width file using the provided column character ranges.

    Args:
        file_path: Path to the fixed-width text file.
        column_ranges: List of (start, end) tuples representing column positions.

    Returns:
        A list of rows, where each row is a list of column values as strings.
    """
    parsed_rows: List[List[str]] = []

    with open(file_path, 'r') as file:
        for line in file:
            row = [
                line[start:end+1].strip()
                for (start, end) in column_ranges
            ]
            parsed_rows.append(row)

    return parsed_rows
