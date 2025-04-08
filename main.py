from ms_reader import MSReader

# Create reader and load file
reader = MSReader("XMLFILE.mzML")
reader.read_file()

# Get data from first spectrum
mz, intensity, rt = reader.get_spectrum_data(0)
df = reader.get_dataframe(spectrum_number=0, start=0, end=10)

print(f"Retention time: {rt}")
print(f"First m/z value: {mz[0]}")