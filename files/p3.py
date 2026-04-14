# # Signal Amplitude Analyzer

# # A signal processing experiment stores signal amplitude samples in a file.Create a file named signal.txt containing 10 numerical amplitude values in different lines. Write a Python program to read the file and find the maximum and minimum amplitude.
# # with open("temperature.txt", "r") as f:
# #     amplitudes = [float(line.strip()) for line in f]
# # max_amplitude = max(amplitudes)
# # min_amplitude = min(amplitudes) 
# # print(f"Maximum amplitude: {max_amplitude}")
# # print(f"Minimum amplitude: {min_amplitude}")
# # Copy all contents from signal.txt into backup_signal.txt.
# with open("temperature.txt", "r") as f:
#     contents = f.read()
# with open("backup_signal.txt", "w") as f:
#     f.write(contents) 
# Read the sensor_config.json file. Update the max temperature value to 130.
import json
with open("sensor_config.json", "r") as f:
    config = json.load(f)
config["max_temperature"] = 130
with open("sensor_config.json", "w") as f:
    json.dump(config, f, indent=4)

    