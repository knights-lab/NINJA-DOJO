#!/usr/bin/env python
import os
from collections import defaultdict
from glob import glob

import click
import pandas as pd

from ninja_trebuchet.parsers import FASTA, FASTQ

from ninja_dojo.taxonomy.ncbi_tree import NCBITree
from ninja_dojo.taxonomy.maps import RefseqAssemblyMap


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-v', '--verbose', is_flag=True)
def extract_ncbi_tid(path, verbose):
    # nt = NCBITree()
    rf = RefseqAssemblyMap()
    for file in glob(os.path.join(os.path.abspath(path), '*.gold')):
    #     df = pd.read_csv(file, header=None, sep='\t')
    #     mp2_to_taxon_id = defaultdict(list)
    #     i = 0
    #     for mp2 in df[0]:
    #         for clade in iter(mp2.split()[::-1]):
    #             tid = rf.name2taxon_id[clade.replace('_', ' ')]
    #             if not 0 == tid:
    #                 mp2_to_taxon_id['metaphlan2_name'].append(mp2)
    #                 mp2_to_taxon_id['ncbi_taxon_id'].append(tid)
    #                 mp2_to_taxon_id['lineage'].append(nt.gg_lineage(tid))
    #                 break
    #             elif verbose:
    #                 print('%s not found' % clade)
    #                 i += 1
    #
    #     df_out = pd.DataFrame(mp2_to_taxon_id, index=None)
    #     df_out.to_csv(os.path.join(path, file[:file.find('.')] + '.ncbi_map.csv'))

        with open(os.path.join(path, '%s.fastq' % os.path.basename(file).split('.')[0])) as fastq_fh:
            for header, seq, qual in FASTQ(fastq_fh).read():
                print(header.split('|')[3].split('.')[0])


if __name__ == '__main__':
    extract_ncbi_tid()
