#!/usr/bin/env python
"""Cell Standard v2 - Metadata Evaluation Script"""

import pandas as pd
import sys
from pathlib import Path

CORE_FIELDS = [
    'organism_taxid',
    'tissue',
    'tissue_ontology_term_id',
    'disease',
    'disease_ontology_term_id',
    'sex',
    'development_stage',
    'development_stage_ontology_term_id',
]

RECOMMENDED_FIELDS = [
    'title', 'summary', 'contributors', 'reference',
    'sample_name', 'donor_name',
    'library_strategy', 'library_construction_method', 'sequenced_fragment', 'tissue_type',
    'reference_genome', 'gene_annotation_version',
    'raw_matrix_file_name', 'processed_file',
    'obs_cell_type_column', 'obsm_embedding_key',
]

def evaluate_core_fields(df):
    results = {}
    filled_core = 0
    for field in CORE_FIELDS:
        if field in df.columns:
            non_null = int(df[field].notna().sum())
            total = len(df)
            pct = (non_null / total * 100) if total > 0 else 0
            results[field] = {'filled': non_null, 'total': total, 'pct': round(pct, 1)}
            if pct >= 50:
                filled_core += 1
        else:
            results[field] = {'filled': 0, 'total': len(df), 'pct': 0}
    core_pct = (filled_core / len(CORE_FIELDS) * 100) if CORE_FIELDS else 0
    return results, core_pct

def evaluate_recommended_fields(df):
    results = {}
    filled_rec = 0
    for field in RECOMMENDED_FIELDS:
        if field in df.columns:
            has_data = bool(df[field].notna().any())
            example = str(df[field].dropna().iloc[0])[:50] if has_data else 'N/A'
            results[field] = {'present': has_data, 'example': example}
            if has_data:
                filled_rec += 1
        else:
            results[field] = {'present': False, 'example': 'Field missing'}
    rec_pct = (filled_rec / len(RECOMMENDED_FIELDS) * 100) if RECOMMENDED_FIELDS else 0
    return results, rec_pct

def calculate_rating(core_pct, rec_pct):
    if core_pct < 50:
        return '差', '核心字段缺失>=3项，数据无基本生物学价值'
    elif core_pct >= 100 and rec_pct >= 70:
        return '优', '精品数据，生物学身份清晰，实验可追溯'
    elif rec_pct < 70:
        return '良', '基础可用，但缺乏实验细节或原始文件'
    else:
        return '合格', '满足基本要求'

def evaluate_excel(file_path):
    print('\n' + '='*60)
    print('Cell Standard v2 - Metadata Evaluation')
    print('='*60 + '\n')
    
    try:
        dataset = pd.read_excel(file_path, sheet_name='dataset')
        file_meta = pd.read_excel(file_path, sheet_name='file_metadata')
    except Exception as e:
        print(f'[ERROR] Error reading file: {e}')
        return
    
    print(f'[DATA] Dataset: {dataset.shape[0]} rows x {dataset.shape[1]} cols')
    print(f'[FILE] File metadata: {file_meta.shape[0]} samples\n')
    
    file_meta.columns = [str(c).strip().lower() for c in file_meta.columns]
    
    print('='*60)
    print('1. Core Fields Evaluation (8 items)')
    print('='*60)
    core_results, core_pct = evaluate_core_fields(file_meta)
    
    for field, info in core_results.items():
        status = '[OK]' if info['pct'] >= 50 else '[X]'
        print(f'  {status} {field:35s} {info["filled"]:4d}/{info["total"]:4d} ({info["pct"]:5.1f}%)')
    
    print(f'\n  Core completeness: {core_pct:.1f}%')
    
    print('\n' + '='*60)
    print('2. Recommended Fields Evaluation (16 items)')
    print('='*60)
    rec_results, rec_pct = evaluate_recommended_fields(file_meta)
    
    for field, info in rec_results.items():
        status = '[OK]' if info['present'] else '[X]'
        print(f'  {status} {field:35s} {info["example"][:40]}')
    
    print(f'\n  Recommended completeness: {rec_pct:.1f}%')
    
    print('\n' + '='*60)
    print('3. Final Rating')
    print('='*60)
    rating, explanation = calculate_rating(core_pct, rec_pct)
    print(f'\n  Rating: [{rating}]')
    print(f'  Explanation: {explanation}')
    print(f'  Core completeness: {core_pct:.1f}%')
    print(f'  Recommended completeness: {rec_pct:.1f}%')
    
    print('\n' + '='*60)
    print('Rating Mapping Table')
    print('='*60)
    print('\n| Rating | Core     | Recommended | Explanation |')
    print('|--------|----------|-------------|-------------|')
    
    if core_pct < 50:
        print(f'| 差     | {core_pct:.1f}%   | {rec_pct:.1f}%       | Core fields missing >=3, no value |')
    elif core_pct >= 100 and rec_pct >= 70:
        print(f'| 优     | {core_pct:.1f}%   | {rec_pct:.1f}%       | Premium data, ready for research |')
    elif rec_pct < 70:
        print(f'| 良     | {core_pct:.1f}%   | {rec_pct:.1f}%       | Basic usable, needs details |')
    else:
        print(f'| 合格   | {core_pct:.1f}%   | {rec_pct:.1f}%       | Meets basic requirements |')
    
    print('\n' + '='*60)
    print('Evaluation complete!')
    print('='*60 + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python evaluate_metadata.py <excel_file>')
        print('Example: python evaluate_metadata.py hesta.xlsx')
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f'[ERROR] File not found: {file_path}')
        sys.exit(1)
    
    evaluate_excel(file_path)
