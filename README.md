# Pythonic .mzML File Reader

A Python package for reading and manipulating mass spectrometry data stored in .mzML format.

```markdown
# Pythonic .mzML File Reader

## Introduction
A Python package for reading and manipulating mass spectrometry data stored in .mzML format. This package provides an intuitive interface for data scientists to work with mass spectrometry data, inspired by the alphatims package's user-friendly approach.

## Installation
```bash
pip install pyopenms
pip install pandas
pip install numpy
```



## Features
- Easy reading of .mzML files using PyOpenMS
- Data extraction in pandas DataFrame format
- Spectrum-wise data access
- Retention time information
- Flexible data slicing


### MSReader Class

#### `__init__(file_path)`
Initialize the reader with a file path.
```python
reader = MSReader("path/to/file.mzML")
```

#### `read_file()`
Read the .mzML file.
```python
success = reader.read_file()
```

#### `get_total_spectra()`
Get total number of spectra in the file.
```python
total = reader.get_total_spectra()
```

#### `get_spectrum_data(spectrum_number)`
Get data for a specific spectrum.
```python
mz, intensity, rt = reader.get_spectrum_data(0)
```

#### `get_dataframe(spectrum_number, start=0, end=None)`
Get spectrum data as pandas DataFrame.
```python
df = reader.get_dataframe(0, start=0, end=5)
```

## Example Output
```python
# DataFrame output example
           mz    intensity
0    100.0453     1234.00
1    100.5678     2345.00
2    101.1234     3456.00
3    101.6789     4567.00
4    102.2345     5678.00
```

## Complete Example
```python
from ms_reader import MSReader

def analyze_spectrum(file_path, spectrum_number):
    # Initialize reader
    reader = MSReader(file_path)
    
    # Read file
    if reader.read_file():
        # Get spectrum data
        mz, intensity, rt = reader.get_spectrum_data(spectrum_number)
        
        if mz is not None:
            print(f"Spectrum {spectrum_number}:")
            print(f"Retention time: {rt:.2f} seconds")
            print(f"Number of peaks: {len(mz)}")
            
            # Get as DataFrame
            df = reader.get_dataframe(spectrum_number, start=0, end=5)
            print("\nFirst 5 peaks:")
            print(df)
    
# Use the function
analyze_spectrum("your_file.mzML", 0)
```

## Dependencies
- contourpy==1.3.1
- cycler==0.12.1
- fonttools==4.57.0
- kiwisolver==1.4.8
- matplotlib==3.10.1
- numpy==2.2.4
- packaging==24.2
- pandas==2.2.3
- pillow==11.1.0
- pyopenms==3.3.0
- pyparsing==3.2.3
- python-dateutil==2.9.0.post0
- pytz==2025.2
- six==1.17.0
- tzdata==2025.2





