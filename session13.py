from datetime import datetime
from collections import namedtuple
from collections import Counter


class VehicleGen:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, encoding="utf-8", errors="ignore") as f:
            col_names = next(f).strip("\n").split(",")
            self.col_names = ["_".join(x.lower().split()) for x in col_names]
            self.CarTicket = namedtuple("CarTicket", self.col_names)

    @staticmethod
    def sanitize_row_values(row):
        """
        Sanitizes rows from the csv, enforces proper data format.
        """
        row["summons_number"] = int(row["summons_number"])
        row["issue_date"] = datetime.strptime(row["issue_date"], "%m/%d/%Y").date()
        row["violation_code"] = int(row["violation_code"])
        return row

    def __iter__(self):
        return self.get_tickets()

    def get_tickets(self):
        """
        yields the car ticket namedtuple.
        """
        with open(self.filename, encoding="utf-8", errors="ignore") as f:
            next(f)
            for row in f:
                r = row.strip("\n").split(",")
                r = VehicleGen.sanitize_row_values(dict(zip(self.col_names, r)))

                yield self.CarTicket(**r)

    def count_violations(self):
        """
        returns the violations count by car make
        """
        violation_make = (p.vehicle_make for p in self)
        return Counter(violation_make)
