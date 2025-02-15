# a helper python code to compare the expected ouputs of Pow2 unit and its real outputs
# files are generated by Pow2_tb.sv
def fp8_to_real(value):
  # FP8(3,4) has:
  # - 3 integer bits
  # - 4 fractional bits
  # - Signed format

  # Extract sign bit

  # Extract integer part 
  integer = value >> 4

  # Extract fraction part
  fraction = value & 0b00001111

  #Compute real value  
  real_value = (integer + fraction / 16)

  return real_value

def compare_files(file1_path, file2_path):
    differences = []
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        for line1, line2 in zip(file1, file2):
            try:
                num1 = float(line1.strip())
                num2 = float(line2.strip())
                #num1 = fp8_to_real(num1)
                difference = abs(num1 - num2)
                differences.append(difference)
            except ValueError:
                # Handle the case where a line does not contain a valid number
                differences.append(None)

    return differences

# Example usage
file1_path = 'Pow_data2.txt'
file2_path = 'true_pow_data.txt'
differences = compare_files(file1_path, file2_path)
print(differences)
print(f"average diff = {sum(differences)/len(differences)}")
#print(f"average diff after scale down by 2^4 is: {(sum(differences)/len(differences))/2**4}")
