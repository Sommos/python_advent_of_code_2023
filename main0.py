def sum_calibration_values(calibration_document):
    total_sum = 0

    for line in calibration_document:
        digits = [char for char in line if char.isdigit()]
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value

    return total_sum


def read_calibration_document(file_path):
    with open(file_path, 'r') as file:
        calibration_document = [line.strip() for line in file.readlines()]
    return calibration_document


file_path = 'input.txt'

calibration_document = read_calibration_document(file_path)

result = sum_calibration_values(calibration_document)
print("The sum of calibration values is:", result)
