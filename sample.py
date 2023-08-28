import json

class SimpleTable(list):
    def __init__(self, headers):
        super().__init__()
        self.headers = headers

    def append(self, row):
        if len(row) != len(self.headers):
            raise ValueError("Row length does not match the number of headers.")
        super().append(row)

    def table(self):
        table_str = ""
        if len(self) > 0:
            table_str += " | ".join(self.headers) + "\n"
            table_str += "-" * (len(self.headers) * 10) + "\n"

            table_str += " | ".join(str(val) for val in self[0]) + "\n"

            for row in self[1:]:
                table_str += " | ".join(str(val) for val in row) + "\n"
        return table_str

    def _json(self):
        data = {
            "headers": self.headers,
            "rows": self
        }
        return json.dumps(data, indent=4)

# Test the SimpleTable class
headers = ["Name", "Age", "Country"]
sample_table = SimpleTable(headers)

sample_table.append(["Alice", 25, "USA"])
sample_table.append(["Bob", 30, "Canada"])
sample_table.append(["Eve", 28, "UK"])

print("Table:")
print(sample_table.table())

print("\nJSON Output:")
print(sample_table._json())
