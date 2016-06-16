import os
import pandas as pd
from collections import defaultdict

from ninja_trebuchet.factory import Pickleable, download

from ... import SETTINGS, LOGGER
from ...downloaders import RefseqCatalog


class RefseqCatalogMap(Pickleable):
    def __init__(self, _downloader=RefseqCatalog()):
        self._downloader = _downloader
        super().__init__(SETTINGS, LOGGER)

    @download
    def _parse(self):
        self.df = self.parse_df()
        self.taxid2refseq_accession = defaultdict(int)
        for ind, ser in self.df.iterrows():
            self.taxid2refseq_accession[ser['assembly_accession'][:ser['assembly_accession'].find('.')]] = ser['taxid']

    def parse_df(self):
        df = pd.read_csv(os.path.join(self._downloader.path, 'refseq_catalog.csv'), sep=',')
        return df

    def __getstate__(self):
        d = dict(self.__dict__)
        del d['df']
        return d

    def __setstate__(self, d):
        # TODO add try/except
        self.__dict__.update(d)
        self.df = self.parse_df()

