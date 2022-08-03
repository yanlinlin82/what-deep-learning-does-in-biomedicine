#!/usr/bin/python
#
# installation:
#   pip install biopython
#
import sys
import pandas as pd
from Bio import Entrez

def fetch_details(id_list):
    ids = ','.join(map(str, id_list))
    print('[DEBUG] Query:', ids, file=sys.stderr)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed', retmode='xml', id=ids)
    results = Entrez.read(handle)
    return results

def get_pub_date(d):
    if len(d) > 0:
        return "{}-{}-{}".format(d[0]['Year'], d[0]['Month'], d[0]['Day'])
    return ''

def get_doi(eloc):
    for item in eloc:
        if item.attributes['EIdType'] == 'doi':
            return item[:]
    return ''

def main():

    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<input.xlsx>")
        exit(1)

    df = pd.read_excel(sys.argv[1], na_filter=False)
    #print(df)

    papers = fetch_details(df['PMID'].values)

    #print("PMID", "DOI", "标题", "杂志", "发表日期", sep = "\t")

    df2 = pd.DataFrame(columns = ['PMID', 'DOI', '标题', '杂志', '发表日期'])
    for paper in papers['PubmedArticle']:
        df3 = pd.DataFrame({
            'PMID': [ paper['MedlineCitation']['PMID'] ],
            'DOI': [ get_doi(paper['MedlineCitation']['Article']['ELocationID']) ],
            '标题': [ paper['MedlineCitation']['Article']['ArticleTitle'] ],
            '杂志': [ paper['MedlineCitation']['Article']['Journal']['Title'] ],
            '发表日期': [ get_pub_date(paper['MedlineCitation']['Article']['ArticleDate']) ]
            })
        df2 = pd.concat([df2, df3], ignore_index = True)
    
    df3 = df.astype(str).merge(df2, on='PMID', how='left')
    df3.to_csv(sys.stdout, sep='\t', index=False, header=True)

if __name__ == '__main__':
    main()
