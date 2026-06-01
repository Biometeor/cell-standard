# 元信息填写表

> **用途**：用户递交数据时填写元信息，确保数据可追溯、可复用。
> **推荐使用**：[⬇️ 下载 Excel 填写模板](元信息填写表.xlsx)（带下拉选项、颜色标识，填写更方便）

---

## 一、数据集元信息

每个项目填写一份。

| 字段名 | 类型 | 必填 | 描述与参考 | 填写值 |
| :--- | :--- | :---: | :--- | :--- |
| title | string | **是** | 数据集标题，简要描述数据集内容。格式：`<技术>_<组织/疾病>_<物种>`。示例：`MOSTA: Mouse Organogenesis Spatiotemporal Transcriptomic Atlas` | |
| summary | string | **是** | 数据集详细描述，说明实验目的、样本来源、技术平台等关键信息。建议 2-5 句话。 | |
| contributors | string | **是** | 数据集递交者姓名。多个作者用 `;` 分隔。示例：`San Zhang; Si Li` | |
| reference | string | 推荐 | 数据集的发表文献 DOI 号或 PMID。示例：`doi:10.1093/nar/gkad933` | |

---

## 二、样本级文件元信息

每个样本/文件填写一行。

### 2.1 通用字段（所有数据类型通用）

| 字段名 | 类型 | 必填 | 参考/示例 | 填写值 |
| :--- | :--- | :---: | :--- | :--- |
| **sample_name** | string | **是** | 样本唯一标识符，作为数据关联主键，建议与文献保持一致。示例：`PRJ001` | |
| **donor_name** | string | **是** | 供体/个体名称，用于区分生物学重复。<br>— `cell line` 填 `na`<br>— 多供体混合填 `pooled`<br>— 无法确定填 `unknown`<br>示例：`Patient_001` | |
| **sequenced_fragment** | string | **是** | 测序片段类型。<br>可选值：`3 prime tag` / `5 prime tag` / `probe-based` / `full length` / `not applicable` | |
| **library_strategy** | string | **是** | 实验类型，决定处理流程。<br>可选值：`scRNA-seq` / `snRNA-seq` / `scATAC-seq` / `spatial-transcriptomics` | |
| **library_construction_method** | string | **是** | 文库构建方法。<br>常见值：`10x 3' v3` / `10x 5' v2` / `Smart-seq2` / `Drop-seq` / `10x Visium` / `Stereo-seq` / `10x scATAC-seq` | |
| **development_stage** | string | **是** | 发育阶段。<br>— `cell line` 填 `na`<br>— 不清楚填 `unknown`<br>参考：[人](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/hsapdv.obo) / [小鼠](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/mmusdv.obo) | |
| **development_stage_ontology_term_id** | string | **是** | 发育阶段本体论 ID。规则同上。示例：`HsapDv:0000016` | |
| **tissue** | string | **是** | 组织名称（易理解的自然语言）。示例：`brain` / `lung` / `liver` | |
| **tissue_ontology_term_id** | string | **是** | 组织本体论 ID。<br>— `cell line` 使用 [Cellosaurus](https://www.cellosaurus.org/)<br>— 其他使用 [UBERON](https://github.com/obophenotype/uberon)<br>— 癌症/肿瘤统一标注 cancer/tumor 对应 UBERON 条目<br>示例：`UBERON:0000955`（brain） | |
| **tissue_type** | string | **是** | 组织类型。<br>可选值：`tissue` / `organoid` / `cell line` / `primary cell culture` | |
| **sex** | string | **是** | 样本性别。<br>可选值：`male` / `female` / `hermaphrodite` / `unknown` | |
| **disease** | string | **是** | 疾病状态。健康样本填 `Normal`。示例：`Lung Adenocarcinoma` / `Normal` | |
| **disease_ontology_term_id** | string | **是** | 疾病本体论 ID。<br>正常/健康填 `MONDO:0000001`<br>其他在 [MONDO](https://purl.obolibrary.org/obo/mondo.owl) 中查找。示例：`MONDO:0005069`（lung adenocarcinoma） | |
| **organism_taxid** | int | **是** | 物种 NCBI Taxonomy ID。<br>常见值：`9606`（人） / `10090`（小鼠） / `10116`（大鼠） / `7955`（斑马鱼） / `3702`（拟南芥） | |
| **reference_genome** | string | **是** | 比对使用的参考基因组版本。<br>常见值：`GRCh38` / `GRCm39` / `mm10` / `hg19` | |
| **gene_annotation_version** | string | 推荐 | 基因组注释版本。示例：`v110` / `GCF_000001405.40` / `Ensembl 110` | |
| **raw_matrix_file_name** | string | **是** | 原始表达矩阵文件路径（最原始数据）。<br>— scRNA-seq: `*.mtx` / `*.h5`<br>— Stereo-seq: `bin1` 格式 gef<br>— scATAC-seq: `fragments.tsv.gz`<br>— 10x Visium: 含空间坐标<br>示例：`./data/S01_matrix.mtx` | |
| **raw_matrix_file_type** | string | **是** | 原始矩阵文件类型。<br>推荐：`h5` / `gef` / `h5ad` / `mtx` / `fragments.tsv.gz` | |
| **raw_matrix_file_md5** | string | **是** | 原始矩阵文件的 MD5 校验码。示例：`a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6` | |
| **processed_file_name** | string | 推荐 | 用户自行分析后的 H5AD 文件路径（可选）。示例：`./data/S01_analyzed.h5ad` | |
| **processed_file_md5** | string | 推荐 | 分析后文件的 MD5 校验码。示例：`f6e7d8c9b0a1b2c3d4e5f6g7h8i9j0k1` | |
| **obs_cell_type_column** | string | 推荐 | H5AD `.obs` 中细胞类型注释列名。示例：`cell_type` / `cell_type_major` | |
| **obsm_embedding_key** | string | 推荐 | H5AD `.obsm` 中降维坐标键名。示例：`X_umap` / `X_tsne` | |

### 2.2 空间转录组适配字段（仅 Spatial 类型填写）

| 字段名 | 类型 | 必填 | 描述 | 填写值 |
| :--- | :--- | :---: | :--- | :--- |
| **image_file** | string | 条件推荐 | 组织图像文件路径，支持 `tif` / `png` / `jpg` 格式。示例：`data/S001/spatial/image.tif` | |
| **image_file_md5** | string | 条件推荐 | 图像文件 MD5 校验值 | |
| **cell_bin_file** | string | 条件推荐 | 细胞分割/bin 结果文件路径。示例：`data/S001/cell_bin.json` | |
| **cell_bin_file_md5** | string | 条件推荐 | 细胞 bin 文件 MD5 校验值 | |

---

## 三、补充文件

当有额外辅助文件需要递交时填写，每个文件一行。

| 字段名 | 类型 | 必填 | 描述与示例 | 填写值 |
| :--- | :--- | :---: | :--- | :--- |
| **supplementary_file_name** | string | **是** | 补充文件的完整文件名（含后缀）。建议含样本 ID 前缀。示例：`S01_annotation_script.R` / `S01_qc_metrics.png` | |
| **supplementary_file_type** | enum | **是** | 文件功能分类。<br>可选值：`Analysis Script` / `Reference Genome` / `Image` / `Metadata` / `Other` | |
| **supplementary_file_description** | string | **是** | 文件内容与用途说明。包括使用的软件版本。示例：`Seurat v4.0 script used for cell type annotation` | |
| **supplementary_file_md5** | string | **是** | 文件的 MD5 校验码 | |

---

## 四、填写示例

### 示例 1：scRNA-seq 样本

| 字段名 | 填写值 |
| :--- | :--- |
| sample_name | PRJ001 |
| donor_name | Patient_001 |
| sequenced_fragment | 3 prime tag |
| library_strategy | scRNA-seq |
| library_construction_method | 10x 3' v3 |
| development_stage | adult |
| development_stage_ontology_term_id | HsapDv:0000016 |
| tissue | lung |
| tissue_ontology_term_id | UBERON:0002048 |
| tissue_type | tissue |
| sex | male |
| disease | Lung Adenocarcinoma |
| disease_ontology_term_id | MONDO:0005069 |
| organism_taxid | 9606 |
| reference_genome | GRCh38 |
| gene_annotation_version | Ensembl v110 |
| raw_matrix_file_name | ./data/PRJ001_matrix.mtx.gz |
| raw_matrix_file_type | mtx |
| raw_matrix_file_md5 | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6 |
| obs_cell_type_column | cell_type |
| obsm_embedding_key | X_umap |

### 示例 2：Spatial 样本（Stereo-seq）

| 字段名 | 填写值 |
| :--- | :--- |
| sample_name | MOB_S001 |
| library_strategy | spatial-transcriptomics |
| library_construction_method | Stereo-seq |
| ... | *（同上省略通用字段）* |
| raw_matrix_file_name | ./data/MOB_S001.bin1.gef |
| raw_matrix_file_type | gef |
| image_file | ./data/MOB_S001/spatial/stereo_seq_image.tif |
| cell_bin_file | ./data/MOB_S001/cell_bin.json |

---

> **提交方式**：填写完整后将此表（Excel 或 CSV 格式）与数据文件一并递交。系统会自动解析并校验必填项完整性。
