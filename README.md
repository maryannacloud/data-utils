# 📊 data-utils

A lightweight, extensible Python utility library for reading, parsing, and validating structured data files — including CSV, TSV, fixed-width, and VCF formats.

> 💡 Built for data-driven QA workflows, bioinformatics pipelines, and anyone dealing with structured files at scale.

---

## 🔧 Features

- ✅ Auto-detect column boundaries in fixed-width files
- ✅ Read and write CSV/TSV with flexible options
- ✅ Parse genomic VCF (Variant Call Format) files
- ✅ Validate and inspect file structure before processing
- ✅ Easily extensible for new data formats

---

## 📦 Installation

Install via `pip` (once published):

```bash
pip install data-utils

Or install locally from source:

git clone https://github.com/your-username/data-utils.git
cd data-utils
pip install -e .

🧪 Usage Examples

➤ Parse a fixed-width file

from data_utils.fixed_width import detect_column_positions
positions = detect_column_positions("data/payment-data.txt", sample_size=10)

➤ Read a CSV
from data_utils.delimited import read_csv
rows = read_csv("data/records.csv", delimiter=",")

🗂 Project Structure
data-utils/
├── data_utils/           ← Python package with reusable modules
├── tests/                ← Unit tests
├── examples/             ← Example usage scripts
├── setup.py              ← Legacy packaging script
├── pyproject.toml        ← Modern build metadata
├── README.md             ← You’re here
└── .gitignore            ← Ignore cache/temp files

🙌 Contributing
Contributions, issues, and suggestions are welcome! Feel free to fork and submit pull requests — or open issues to propose enhancements.

📄 License
MIT License. See LICENSE file for details.

👩‍🔬 Author
Built with ❤️ by Maryna Nesterenko
Former QA Engineer at Snap eHealth and Natera, passionate about test automation, clean code, and useful tools.
