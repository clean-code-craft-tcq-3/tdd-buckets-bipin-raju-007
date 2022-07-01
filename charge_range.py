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
    return charge_readings


def display_output(charge_readings):
    print("Range, Readings")
    for reading in charge_readings:
        print(reading)


def current_from_high_fidelity_sensor(current_in_bit):
    current_in_bit = ''.join(current_in_bit)
    current_in_units = int(current_in_bit, 2)
    if 0 < current_in_units < 4095:
        current_in_amp = round(10 * current_in_units / 4094)
        return current_in_amp
    else:
        return -1


def capture_hifi_sensor_charge_range(charge_sequence):
    """-
    Takes input as sequence of charge values, where each value is represented in a 12-bit in array;
    representing a reading between 0-4094 and returns their charge range.
    """
    charge_values = []
    for value in charge_sequence:
        charge_values.append(current_from_high_fidelity_sensor(value))

    charge_readings = capture_charge_range(charge_values, display_output)
    return charge_readings


if __name__ == '__main__':
    capture_charge_range([1, 2, 2, 3, 5, 6, 7, 12, 12, 15, 16, 16], display_output)
