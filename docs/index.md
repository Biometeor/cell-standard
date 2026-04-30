# **细胞高质量数据标准v1**

## 一、 总则

### 1.1 目的

为规范细胞组学测序数据的归档管理，确保数据的完整性、可用性及互操作性，特制定本标准。本标准旨在统一数据格式（H5AD）、明确元信息填报规范，并建立自动化的数据质量评估体系，以支持后续的数据挖掘与共享。本标准为和国际接轨，参考了cellxgene的字段要求。

### 1.2 适用范围

本标准适用于所有递交至本系统的以下类型测序数据：

* 单细胞转录组
* 单核转录组
* 单细胞 ATAC (scATAC-seq)
* 空间转录组

## **二**、元信息规范

适用于 scRNA-seq、snRNA-seq、scATAC-seq 及 Spatial Transcriptomics 所有数据类型。

### **1 数据集元信息**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| title | string | 是 | 数据集标题，描述数据集的简略信息 | MOSTA: Mouse Organogenesis Spatiotemporal Transcriptomic Atlas |
| summary | string | 是 | 数据集详细描述 | We have only begun to scratch the surface… |
| contributors | string | 是 | 数据集递交者 | San Zhang |
| reference | string | 推荐 | 数据集发表文献信息DOI号 | doi:10.1093/nar/gkad933 |

### **2 文件元信息**

#### **2.1 通用字段**

适用于 scRNA-seq、snRNA-seq、scATAC-seq 及 Spatial Transcriptomics 所有数据类型。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| sample\_name | string | 是 | 样本唯一标识符，作为数据相互关联的主键。我们建议这个名称和您文献描述的样本名称一致。 | PRJ001 |
| donor\_name | string | 是 | \*  供体/个体名称，用于区分生物学重复，比如关联同一病人的不同样本，自由文本：  特殊值如下：  “na” ：tissue\_type为"cell line"  "pooled"用于来自多个个体样本且无法通过解复用技术可靠地分配给单个个体的观测数据  "unknown"仅将此方法用于数据集中无法确定哪些观测数据来自同一个体的情况。 | Patient\_001 |
| sequenced\_fragment | string | 是 | 使用转录组的测序片段类型，如果没有则not applicable | 3 prime tag; 5 prime tag; probe-based; full length；not applicable |
| library\_strategy | string | 是 | 实验大类型，决定后续的处理流程。 | scRNA-seq / scATAC-seq / spatial-transcriptomics |
| development\_stage | string | 是 | 发育阶段，  tissue\_type 是"cell line"， 则为 "na"  如果不清楚可以填“unkown”  其他是描述疾病的具体字段 | 不同物种不一样：  人：[hhsaps](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/hsapdv.obo)  小鼠：[mmusdv.obo](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/mmusdv.obo) |
| development\_stage\_ontology\_term\_id | string | 是 | 发育阶段，  tissue\_type 是"cell line"， 则为 "na"  如果不清楚可以填“unkown”  其他可以查找以下标准填写  人：[hhsaps](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/hsapdv.obo)  小鼠：[mmusdv.obo](https://github.com/obophenotype/developmental-stage-ontologies/blob/master/src/ontology/components/mmusdv.obo) |  |
| library\_construction\_method | string | 是 | 文库构建方法。 | 10x 3' v1, 10x 3' v2, 10x 3' v3, 10x 3' v4, 10x 5' v1, 10x 5' v2, Smart-seq2, Smart-seq3, Drop-seq, inDrop, CEL-seq2, MARS-seq, Microwell-Seq, Seq-Well 10x Visium等 |
| tissue\_ontology\_term\_id | string | 是 | 如果 tissue\_type is "cell line 必须是Cellosaurus .  如果 tissue\_type 是 "primary cell culture", this MUST follow the requirements for cell\_type\_ontology\_term\_id.  如果tissue\_type 是 "organoid", 胚胎不能是   如果类器官是胚状体, 推荐 是  ，如果类器官是 gastruloid, 推荐值是  其他 [UBERON本体论](https://github.com/obophenotype/uberon/blob/master/uberon.obo) 或[plant-ontology](https://github.com/Planteome/plant-ontology)的一部分  ，癌症或肿瘤组织统一标注cacer和tumor | UBERON:0001828; |
| tissue | string | 是 | 易理解的组织字段 |  |
| tissue\_type | string | 是 | 组织类型,可选值如下   * "cell line" * "organoid" * "primary cell culture" * "tissue" | tissue; organoid; cell culture |
| sex | string | 是 | 样本性别,必须是下面的一部分  *雌雄同体：*  female：  male：  如果不清楚可以填写"unknown" | PATO\_0000383"；unknown" |
| disease | string | 是 | 样本疾病状态，健康样本填 Normal。 | Lung Adenocarcinoma / Normal |
| isease\_ontology\_term\_id | string | 是 | 正常或健康*：*  其他的必须是[MONDO\_0000001](https://purl.obolibrary.org/obo/mondo.owl)的一部分 | 人：[MONDO\_0000001](https://purl.obolibrary.org/obo/mondo.owl) |
|  |  |  |  |  |
| organism\_taxid | string | 是 | 物种Taid | 9606 |
| reference\_genome | string | 是 | 比对使用的参考基因组版本，决定了坐标体系。 | GRCh38 / mm10 |
| gene\_annotation\_version | string | 推荐 | 基因组注释版本 | v110; GCF\_000001405.40 |
| raw\_matrix\_file\_name | string | 是 | 原始表达矩阵文件路径。我们希望这是测序数据处理后最原始的文件，未经过任何过滤；  stereo-seq应提供bin1 matrix  scATAC应提供fragments.tsv  10x visium 应包含空间坐标 | ./data/S01\_matrix.mtx |
| raw\_matrix\_file\_type | string | 是 | 原始矩阵文件类型：  单细胞推荐：h5,gef格式；  空间推荐： h5ad格式(包含空间信息)；  scATAC 推荐 fragments.tsv |  |
| raw\_matrix\_file\_md5 | string | 是 | 原始矩阵文件的 MD5 校验码，用于完整性验证。 | a1b2c3d4e5… |
| processed\_file\_name | string | 推荐 | 用户自行分析后的 H5AD 文件路径（可选）。 | ./data/S01\_analyzed.h5ad |
| processed\_file\_md5 | string | 推荐 | 分析后文件的 MD5 校验码。 | f6e7d8c9b0… |
| obs\_cell\_type\_column | string | 是 | H5AD 文件 .obs 中存储细胞类型注释的列名。 | cell\_type / cell\_type\_major |
| obsm\_embedding\_key | string | 是 | H5AD 文件 .obsm 中存储降维坐标的键名（如 UMAP/tSNE）。 | X\_umap |

#### **2.2 空间转录组stereoseq适配**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **字段名** | **字段类型** | **必填** | **描述** | **示例** |
| stereo\_seq\_image\_file | String | 条件推荐 | Stereo-seq 特有的图像文件路径（如 .tif 格式） | data/S001/spatial/stereo\_seq\_image.tif |
| stereo\_seq\_image\_file\_MD5 | String | 条件推荐 | Stereo-seq 图像文件MD5校验值 | c3d4e5f6g7h8… |
| stereo\_seq\_cell\_bin\_file | String | 条件推荐 | Stereo-seq 细胞分割和bin映射结果文件路径 | data/S001/stereo\_seq/cell\_bin.json |
| stereo\_seq\_cell\_bin\_file\_MD5 | String | 条件推荐 | Stereo-seq 细胞bin文件MD5校验值 | d4e5f6g7h8i9… |

## **3 其他补充文件**

在研究中，很多关键信息（自定义参考基因组 GTF 文件、特殊的 QC 图片），往往不在标准矩阵字段里；该模块用于收纳非标准矩阵文件但重要的辅助文件。支持一个样本/项目递交多个补充文件。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 字段名 | 字段类型 | 必填 | 描述 | 示例 |
| supplementary\_file\_name | string | 是 | 补充文件的完整文件名（包含后缀）。建议包含样本ID前缀以示区分。 | S01\_annotation\_script.R  S01\_qc\_metrics.png  PRJ001\_custom\_gtf.gtf |
| supplementary\_file\_type | enum | 是 | 文件功能分类，便于系统自动识别和用户检索。 | Analysis Script (分析脚本)  Reference Genome (自定义参考基因组)  Image (图片)  Metadata (额外元信息表)  Other (其他) |
| supplementary\_file\_description | string | 是 | 详细描述文件内容、用途及使用的软件/版本。这是用户理解文件的关键。 | Seurat v4.0 script used for cell type annotation  Custom GTF file containing lncRNA annotations used for alignment |
| supplementary\_file\_md5 | string | 是 | 文件的 MD5 校验码，用于校验文件完整性。 | e99a18c428cb38d5f260853678922e03 |

## 三、数据标准化处理规范

系统接收用户递交的数据后，将执行标准化处理流程，将异构数据统一转换为 H5AD (AnnData) 格式，并固定内部插槽结构，以确保下游分析工具（如 Scanpy、CellxGene）的兼容性。

### 3.1 标准化输出格式

所有入库数据最终转换为 .h5ad 格式，文件命名规范为 {sample\_id}.h5ad。

### 3.2 H5AD 插槽结构规范

系统将按照以下映射逻辑填充 H5AD 内部插槽：

索引规范：

adata.obs.index：必须为 细胞条码，格式通常为 AAACATACAAAAGT-1。建议拼接样本 ID 以防止重复，如 S001\_AAACATACAAAAGT-1。

adata.var.index：必须为 基因 ID (Gene ID)（如 Ensembl ID: ENSG000001234），不建议仅使用 Gene Symbol，避免歧义。

##### **3.2.1 通用属性**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 插槽路径 | 字段名 | 数据类型 | 必选 | 说明 |
| .X | main\_matrix | Sparse/Matrix | 必选 | 主表达矩阵。归档建议存储 归一化 后的数据（如 LogNormalized, CPM），便于直接可视化和分析。 |
| .layers['raw\_counts'] | raw\_counts | Sparse/Matrix |  | 原始计数矩阵。用于封存原始数据，数值必须为整数。 |
| .obs['cell\_type'] | cell\_type | Category | 必选 | 细胞类型注释。如 CD4+ T cell, B cell。 |
| .obsm['X\_pca'] | X\_pca | Matrix | 必选 | PCA 降维结果 (通常 50 维)。 |
| .obsm['X\_umap'] | X\_umap | Matrix | 可选 | UMAP 二维坐标。这是可视化的默认选择。 |
| .obsm['X\_tsne'] | X\_tsne | Matrix | 可选 | t-SNE 二维坐标。 |

##### **3.2.2 空间属性**

| 插槽路径 | 字段名 | 数据类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| .obs[‘pixel\_x’] | pixel\_x | Float | 可选 | 像素级 X 坐标。 |
| .obs[‘pixel\_y’] | pixel\_y | Float | 可选 | 像素级 Y 坐标。 |
| .obsm[‘spatial’] | spatial | Matrix | 必选 | 空间坐标信息 |
| .uns[‘spatial’] | spatial\_info | Dictionary | 必选 | 空间相关信息，包括图像路径、尺度因子等。 |

## 四、**数据文件质控标准**

在生成标准 H5AD 文件后，系统自动计算 QC 指标，并对单个文件进行评估，

### **4.1 质控字段**

评估字段内容见下表

[请至钉钉文档查看附件《细胞质控字段及标准》。](https://alidocs.dingtalk.com/i/nodes/YndMj49yWjPnow3RCDr97wjbJ3pmz5aA?iframeQuery=anchorId%3DX02mmkokhar39w5mdbp6rd)

### 4.2 评级标准

| 等级 | 定义 | 评判标准 |
| --- | --- | --- |
| 1级 | 优质 | 所有质控指标均在可接受范围内，且 spot\_count ≥ 5000 |
| 2级 | 合格 | 核心质控指标（spot\_count, gene\_count, median\_genes\_per\_spot）在可接受范围内 |
| 3级 | 让步接受 | 部分质控指标（≤3个）超出可接受范围，但仍有分析价值 |
| 4级 | 不合格 | 多个核心质控指标（>3个）超出可接受范围，不建议使用 |

## 五、**项目数据评估打分**

系统采用多维综合评估体系。该体系不仅考量样本质量的平均水平，更引入“短板效应”（最低质量样本）与“一致性检验”（样本间离散度）指标。对于空间转录组项目，额外纳入空间信息质量维度。最终评级由“数据质量评级”与“元信息完整度修正系数”共同决定。

### **5.1 项目级统计字段**

|  |  |  |  |
| --- | --- | --- | --- |
| 维度 | 字段名 | 说明 | 适用范围 |
| 规模 | project\_total\_cells / spots | 项目总有效细胞/Spot 数（所有评级为 1-3 级的文件求和），反映项目数据规模。 | 全部 |
| 质量 | project\_avg\_score | 项目平均分（所有单文件原始 QC 分数的算术平均值），反映整体数据质量基线。 | 全部 |
| 一致性 | qc\_consistency | 质量一致性（单文件得分标准差 SD）。数值越小，表明样本批次间差异越小，一致性越高。 | 全部 |
| 元信息 | project\_meta\_integrity | 元信息完整度均值。计算所有文件的元信息填报率，包含必填项与推荐项的加权评分。 | 全部 |
| 空间信息 | avg\_spatial\_resolution | 平均空间分辨率。统计项目下所有空间样本的分辨率均值，评估空间解析能力。 | 空间组 |
| 空间信息 | avg\_tissue\_coverage | 平均组织覆盖率。评估组织切片的整体有效捕获面积。 | 空间组 |
| 空间信息 | avg\_spot\_uniformity | 平均 Spot 均匀性。评估 Spot 在组织表面的分布均匀程度，排除局部富集或稀疏现象。 | 空间组 |
| 表达质量 | avg\_mean\_genes\_per\_spot | 平均每个 Spot 的基因数（算术平均），评估捕获灵敏度。 | 空间组 |
| 表达质量 | avg\_mean\_umi\_per\_spot | 平均每个 Spot 的 UMI 数（算术平均），评估测序深度饱和度。 | 空间组 |

####

### 5.2 元信息完整度评分细则

元信息完整度不仅考察必填字段，重点评估非必要信息的填报情况，以体现数据的可复用性与挖掘价值。

1. 核心字段（决定数据是否能用、能否入库）
   生物学属性：tissue（组织）、disease（疾病）、development\_stage（发育阶段）、sex（性别）、organism\_taxid（物种）

\*实验属性\*：library\_strategy（实验类型）

2.推荐字段

donor\_name

* 计算公式：

![](data:image/png;base64...)

* 评分层级：
  + ≥ 90% (优)：核心信息完备，且补充了关键的非必要信息（如详细病理信息、自定义参考基因组等）。
  + 30% - 90% (良)：仅满足核心归档要求，缺乏辅助分析信息。
  + < 30% (差)：核心信息缺失，严重影响数据的可用性。

### 5.3 项目综合评分与评级流程

项目评级采用“质量定级 + 元信息修正”的双重机制，遵循“木桶原理”，以最低质量样本或元信息短板为限进行定级。

#### 第一步：基础质量定级

根据单文件 QC 评级结果（优质/合格/让步接受/不合格）及项目级统计指标，确定项目初始质量等级。

* A 类 (优质基线)：所有单文件均为 1 级（优质），且项目总细胞/Spot 数 > 50,000。
* B 类 (合格基线)：80% 以上单文件为 2 级（合格）及以上，无 4 级（不合格）文件。
* C 类 (风险基线)：存在 4 级（不合格）文件，或 20% 以上单文件为 3 级（让步接受）。

#### 第二步：元信息修正（降级机制）

基于 project\_meta\_integrity 对基础等级进行修正，得出最终项目等级。

|  |  |  |
| --- | --- | --- |
| 最终等级 | 定义 | 评判标准与修正规则 |
| 1级 | 优质 | [数据高质量 + 元信息完整]  基础定级为 A 类，且元信息完整度 ≥ 90%。数据极具挖掘价值，可直接用于高水平研究。 |
| 2级 | 合格 | [数据合格 或 元信息良好]  1. 基础定级为 A/B 类，但元信息完整度在 30%-90% 之间（元信息扣分）；  2. 或基础定级为 C 类，但元信息完整度 ≥ 90%（数据质量扣分）。 |
| 3级 | 让步接受 | [存在短板]  1. 基础定级为 A/B 类，但元信息完整度 < 30%（元信息严重缺失）；  2. 或基础定级为 C 类，且元信息完整度在 30%-90% 之间。数据可用性受限，需谨慎使用。 |
| 4级 | 不合格 | [完全不可用]  基础定级为 C 类，且元信息完整度 < 30%。数据质量差且缺乏关键描述，建议重新实验或不予归档。 |