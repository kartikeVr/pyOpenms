import pyopenms as oms
import pandas as pd
import numpy as np


class MSReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.exp = oms.MSExperiment()

    def read_file(self):
        """Read mzML file"""
        try:
            oms.MzMLFile().load(self.file_path, self.exp)
            return True
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return False

    def get_total_spectra(self):
        """Return total number of spectra"""
        return self.exp.size()

    def get_spectrum_data(self, spectrum_number):
        """Get mz, intensity and retention time for a spectrum"""
        try:
            spectrum = self.exp[spectrum_number]
            mz, intensity = spectrum.get_peaks()
            rt = spectrum.getRT()
            return mz, intensity, rt
        except Exception as e:
            print(f"Error getting spectrum {spectrum_number}: {str(e)}")
            return None, None, None

    def get_dataframe(self, spectrum_number, start=0, end=None):
        """Return spectrum data as pandas DataFrame"""
        mz, intensity, rt = self.get_spectrum_data(spectrum_number)
        if mz is None:
            return None

        if end is None:
            end = len(mz)

        data = {
            'mz': mz[start:end],
            'intensity': intensity[start:end]
        }
        return pd.DataFrame(data)