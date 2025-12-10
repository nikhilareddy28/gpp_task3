# custom_writer.py
"""
Custom CSV Writer
"""

class CustomCsvWriter:
    """CSV writer implementation."""

    @staticmethod
    def _escape(field: str) -> str:
        # Escape quotes, commas, newlines
        if any(x in field for x in ['"', ',', '\n']):
            field = field.replace('"', '""')
            return f"\"{field}\""
        return field

    def write(self, file_path, rows):
        with open(file_path, "w", encoding="utf-8") as f:
            for row in rows:
                escaped = [self._escape(field) for field in row]
                f.write(",".join(escaped) + "\n")


if __name__ == "__main__":
    print("Custom CSV Writer loaded.")
