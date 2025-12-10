# custom_reader.py
"""
Custom CSV Reader
"""

class CustomCsvReader:
    """Iterator-based CSV reader implementation."""

    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8")
        self.buffer = ""
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = ""
        in_quotes = False

        while True:
            char = self.file.read(1)

            # End of file
            if not char:
                if field or row:
                    row.append(field)
                    return row
                raise StopIteration

            if char == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    # Escaped quote
                    if next_char == '"':
                        field += '"'
                    else:
                        in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    in_quotes = True

            elif char == "," and not in_quotes:
                row.append(field)
                field = ""

            elif char == "\n" and not in_quotes:
                row.append(field)
                return row

            else:
                field += char


if __name__ == "__main__":
    print("Custom CSV Reader loaded.")
