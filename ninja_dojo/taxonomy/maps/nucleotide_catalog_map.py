import os
import pandas as pd
from collections import defaultdict

from ninja_utils.factory import Pickleable, download

from ... import SETTINGS, LOGGER
from ...downloaders import NucleotideCatalog


class NucleotideMap(Pickleable):
    def __init__(self, _downloaders=(NucleotideCatalog(),)):
        self._downloaders = _downloaders
        super().__init__(SETTINGS, LOGGER)
        self.df = self.parse_df()

    @download
    def _parse(self):
        return self.parse_df()

    def parse_df(self):
        df = pd.read_csv(os.path.join(self._downloaders[0].path, 'nucleotide_catalog.tsv'), sep='\t')
        return df
