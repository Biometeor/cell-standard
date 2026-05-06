# 元信息规范

适用于 scRNA-seq、snRNA-seq、scATAC-seq 及 Spatial Transcriptomics 所有数据类型。

## 1 数据集元信息

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| title | string | 是 | 数据集标题，描述数据集的简略信息 | MOSTA: Mouse Organogenesis Spatiotemporal Transcriptomic Atlas |
| summary | string | 是 | 数据集详细描述 | We have only begun to scratch the surface… |
| contributors | string | 是 | 数据集递交者 | San Zhang |
| reference | string | 推荐 | 数据集发表文献信息DOI号 | doi:10.1093/nar/gkad933 |

## 2 文件元信息

### 2.1 通用字段

适用于 scRNA-seq、snRNA-seq、scATAC-seq 及 Spatial Transcriptomics 所有数据类型。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| sample_name | string | 是 | 样本唯一标识符，作为数据相互关联的主键。我们建议这个名称和您文献描述的样本名称一致。 | PRJ001 |
| donor_name | string | 是 | 供体/个体名称，用于区分生物学重复，比如关联同一病人的不同样本，自由文本。特殊值如下：  "na" ：tissue_type为"cell line"  "pooled"用于来自多个个体样本且无法通过解复用技术可靠地分配给单个个体的观测数据  "unknown"仅将此方法用于数据集中无法确定哪些观测数据来自同一个体的情况。 | Patient_001 |
| sequenced_fragment | string | 是 | 使用转录组的测序片段类型，如果没有则not applicable | 3 prime tag; 5 prime tag; probe-based; full length；not applicable |
| library_strategy | string | 是 | 实验大类型，决定后续的处理流程。 | scRNA-seq / scATAC-seq / spatial-transcriptomics |
| development_stage | string | 是 | 发育阶段，  tissue_type 是"cell line"， 则为 "na"  如果不清楚可以填"unknown"  其他是描述疾病的具体字段 | 不同物种不一样：  人：[hsaps](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/hsapdv.obo)  小鼠：[mmusdv.obo](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/mmusdv.obo) |
| development_stage_ontology_term_id | string | 是 | 发育阶段，  tissue_type 是"cell line"， 则为 "na"  如果不清楚可以填"unknown"  其他可以查找以下标准填写  人：[hsaps](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/hsapdv.obo)  小鼠：[mmusdv.obo](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/mmusdv.obo) |  |
| library_construction_method | string | 是 | 文库构建方法。 | 10x 3' v1, 10x 3' v2, 10x 3' v3, 10x 3' v4, 10x 5' v1, 10x 5' v2, Smart-seq2, Smart-seq3, Drop-seq, inDrop, CEL-seq2, MARS-seq, Microwell-Seq, Seq-Well 10x Visium等 |
| tissue_ontology_term_id | string | 是 | 如果 tissue_type is "cell line" 必须是Cellosaurus .  如果 tissue_type 是 "primary cell culture", this MUST follow the requirements for cell_type_ontology_term_id.  如果tissue_type 是 "organoid", 胚胎不能是   如果类器官是胚状体, 推荐 是  ，如果类器官是 gastruloid, 推荐值是  其他 [UBERON本体论](https://github.com/obophenotype/uberon/blob/master/uberon.obo) 或[plant-ontology](https://github.com/Planteome/plant-ontology)的一部分  ，癌症或肿瘤组织统一标注cacer和tumor | UBERON:0001828; |
| tissue | string | 是 | 易理解的组织字段 |  |
| tissue_type | string | 是 | 组织类型,可选值如下   * "cell line" * "organoid" * "primary cell culture" * "tissue" | tissue; organoid; cell culture |
| sex | string | 是 | 样本性别,必须是下面的一部分  *雌雄同体：*  female：  male：  如果不清楚可以填写"unknown" | unknown" |
| disease | string | 是 | 样本疾病状态，健康样本填 Normal。 | Lung Adenocarcinoma / Normal |
| disease_ontology_term_id | string | 是 | 正常或健康*：*  其他的必须是[MONDO_0000001](https://purl.obolibrary.org/obo/mondo.owl)的一部分 | 人：[MONDO_0000001](https://purl.obolibrary.org/obo/mondo.owl) |
| organism_taxid | string | 是 | 物种Taid | 9606 |
| reference_genome | string | 是 | 比对使用的参考基因组版本，决定了坐标体系。 | GRCh38 / mm10 |
| gene_annotation_version | string | 推荐 | 基因组注释版本 | v110; GCF_000001405.40 |
| raw_matrix_file_name | string | 是 | 原始表达矩阵文件路径。我们希望这是测序数据处理后最原始的文件，未经过任何过滤；  stereo-seq应提供bin1 matrix  scATAC应提供fragments.tsv  10x visium 应包含空间坐标 | ./data/S01_matrix.mtx |
| raw_matrix_file_type | string | 是 | 原始矩阵文件类型：  单细胞推荐：h5,gef格式；  空间推荐： h5ad格式(包含空间信息)；  scATAC 推荐 fragments.tsv |  |
| raw_matrix_file_md5 | string | 是 | 原始矩阵文件的 MD5 校验码，用于完整性验证。 | a1b2c3d4e5… |
| processed_file_name | string | 推荐 | 用户自行分析后的 H5AD 文件路径（可选）。 | ./data/S01_analyzed.h5ad |
| processed_file_md5 | string | 推荐 | 分析后文件的 MD5 校验码。 | f6e7d8c9b0… |
| obs_cell_type_column | string | 是 | H5AD 文件 .obs 中存储细胞类型注释的列名。 | cell_type / cell_type_major |
| obsm_embedding_key | string | 是 | H5AD 文件 .obsm 中存储降维坐标的键名（如 UMAP/tSNE）。 | X_umap |

### 2.2 空间转录组stereoseq适配

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| stereo_seq_image_file | String | 条件推荐 | Stereo-seq 特有的图像文件路径（如 .tif 格式） | data/S001/spatial/stereo_seq_image.tif |
| stereo_seq_image_file_MD5 | String | 条件推荐 | Stereo-seq 图像文件MD5校验值 | c3d4e5f6g7h8… |
| stereo_seq_cell_bin_file | String | 条件推荐 | Stereo-seq 细胞分割和bin映射结果文件路径 | data/S001/stereo_seq/cell_bin.json |
| stereo_seq_cell_bin_file_MD5 | String | 条件推荐 | Stereo-seq 细胞bin文件MD5校验值 | d4e5f6g7h8i9… |

## 3 其他补充文件

在研究中，很多关键信息（自定义参考基因组 GTF 文件、特殊的 QC 图片），往往不在标准矩阵字段里；该模块用于收纳非标准矩阵文件但重要的辅助文件。支持一个样本/项目递交多个补充文件。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 字段名 | 字段类型 | 必填 | 描述 | 示例 |
| supplementary_file_name | string | 是 | 补充文件的完整文件名（包含后缀）。建议包含样本ID前缀以示区分。 | S01_annotation_script.R  S01_qc_metrics.png  PRJ001_custom_gtf.gtf |
| supplementary_file_type | enum | 是 | 文件功能分类，便于系统自动识别和用户检索。 | Analysis Script (分析脚本)  Reference Genome (自定义参考基因组)  Image (图片)  Metadata (额外元信息表)  Other (其他) |
| supplementary_file_description | string | 是 | 详细描述文件内容、用途及使用的软件/版本。这是用户理解文件的关键。 | Seurat v4.0 script used for cell type annotation  Custom GTF file containing lncRNA annotations used for alignment |
| supplementary_file_md5 | string | 是 | 文件的 MD5 校验码，用于校验文件完整性。 | e99a18c428cb38d5f260853678922e03 |
