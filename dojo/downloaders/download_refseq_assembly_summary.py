import os

from ninja_utils.factory import Downloadable
from ninja_utils.utils import download_txt_url

from .. import SETTINGS


class RefseqAssemblySummary(Downloadable):
    def __init__(self, _refseq_summary_urls=SETTINGS.settings['refseq_summary_urls'], _refseq_summary_dir=SETTINGS.settings['refseq_summary_dir']):
        super().__init__(_refseq_summary_dir)
        self.urls = _refseq_summary_urls

    def download(self):
        for url in self.urls:
            file_name = url.split('/')[-1]
            download_txt_url(os.path.join(self.path, file_name), url)
