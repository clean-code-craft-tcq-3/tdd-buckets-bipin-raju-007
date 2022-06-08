from charge_range import *
import mock


def test_split_continuous_range():
    continuous_ranges = []
    current_values = [1]
    split_continuous_range(current_values, continuous_ranges)
    assert(continuous_ranges == [[1]])

    continuous_ranges = []
    current_values = [1, 2, 2, 5, 6]
    split_continuous_range(current_values, continuous_ranges)
    assert(continuous_ranges == [[1, 2, 2], [5, 6]])

    continuous_ranges = []
    current_values = [1, 2, 2, 3, 5, 6, 7, 12, 12, 15, 16, 16]
    split_continuous_range(current_values, continuous_ranges)
    assert(continuous_ranges == [[1, 2, 2, 3], [5, 6, 7], [12, 12], [15, 16, 16]])


def test_calculate_charge_readings():
    charge_reading = []
    continuous_ranges = [[1]]
    calculate_charge_readings(continuous_ranges, charge_reading)
    assert(len(charge_reading) == 1)
    assert(charge_reading[0] == ChargeRangeReadings(1, 1, 1))

    charge_reading = []
    continuous_ranges = [[1, 2, 2], [5, 6]]
    calculate_charge_readings(continuous_ranges, charge_reading)
    assert(len(charge_reading) == 2)
    assert(charge_reading[0] == ChargeRangeReadings(1, 2, 3))
    assert(charge_reading[1] == ChargeRangeReadings(5, 6, 2))

    charge_reading = []
    continuous_ranges = [[1, 2, 2, 3], [5, 6, 7], [12, 12], [15, 16, 16]]
    calculate_charge_readings(continuous_ranges, charge_reading)
    assert(len(charge_reading) == 4)
    assert(charge_reading[0] == ChargeRangeReadings(1, 3, 4))
    assert(charge_reading[1] == ChargeRangeReadings(5, 7, 3))
    assert(charge_reading[2] == ChargeRangeReadings(12, 12, 2))
    assert(charge_reading[3] == ChargeRangeReadings(15, 16, 3))


def test_capture_charge_range():
    mock_output_func = mock.Mock()

    charge_values = [1]
    capture_charge_range(charge_values, mock_output_func)
    mock_output_func.assert_any_call([ChargeRangeReadings(1, 1, 1)])

    charge_values = [1, 2, 2, 5, 6]
    capture_charge_range(charge_values, mock_output_func)
    output_reading = [ChargeRangeReadings(1, 2, 3), ChargeRangeReadings(5, 6, 2)]
    mock_output_func.assert_any_call(output_reading)

    charge_values = [1, 2, 2, 3, 5, 6, 7, 12, 12, 15, 16, 16]
    capture_charge_range(charge_values, mock_output_func)
    output_reading = [ChargeRangeReadings(1, 3, 4), ChargeRangeReadings(5, 7, 3),
                      ChargeRangeReadings(12, 12, 2), ChargeRangeReadings(15, 16, 3)]
    mock_output_func.assert_any_call(output_reading)


if __name__ == '__main__':
    test_split_continuous_range()
    test_calculate_charge_readings()
    test_capture_charge_range()
