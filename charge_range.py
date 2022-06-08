class ChargeRangeReadings:
    def __init__(self, min_val=0, max_val=0, count=0):
        self.min = min_val
        self.max = max_val
        self.count = count

    def __str__(self):
        return f"{self.min} - {self.max}, {self.count}"

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max and self.count == other.count


def split_continuous_range(charge_values, continuous_ranges):
    range_readings = [charge_values.pop(0)]
    for index, value in enumerate(charge_values):
        if value > charge_values[index - 1] + 1:    # new range
            continuous_ranges.append(range_readings)
            range_readings = [value]
        else:
            range_readings.append(value)
    continuous_ranges.append(range_readings)


def calculate_charge_readings(continuous_ranges, charge_readings):
    for some_range in continuous_ranges:
        reading = ChargeRangeReadings()
        reading.min = some_range[0]
        reading.max = some_range[-1]
        reading.count = len(some_range)
        charge_readings.append(reading)


def capture_charge_range(charge_values, record_output):
    continuous_ranges = []
    charge_readings = []
    charge_values = sorted(charge_values)
    split_continuous_range(charge_values, continuous_ranges)
    calculate_charge_readings(continuous_ranges, charge_readings)
    record_output(charge_readings)


def display_output(charge_readings):
    print("Range, Readings")
    for reading in charge_readings:
        print(reading)


if __name__ == '__main__':
    capture_charge_range([1, 2, 2, 3, 5, 6, 7, 12, 12, 15, 16, 16], display_output)
