class Operation:
    def __init__(self, value, date, purposes, currency, operation_type):
        self.value = value
        self.date = date
        self.purpose = purposes
        self.currency = currency
        self.operation_type = operation_type

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def get_all_information(self):
        return [self.value, self.date, self.purpose.get_purpose(),
                self.currency.get_currency(), self.operation_type]


class Currency:
    def __init__(self, rate=0):
        self.rate = rate

    def get_currency(self):
        return self.rate


class Purpose:
    def __init__(self, purpose=""):
        self.purpose = purpose

    def set_purpose(self, purpose):
        self.purpose = purpose

    def get_purpose(self):
        return self.purpose
