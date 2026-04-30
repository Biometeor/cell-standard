# 细胞高质量数据标准 v2

本仓库包含《细胞高质量数据标准v2》的完整文档，使用MkDocs构建，支持在ReadTheDocs上自动生成文档网站。

## 版本更新说明

### v2 (2026-04-30)
- **重构元信息完整度评估体系**
  - 核心字段明确为8项（物种/组织/疾病/性别/发育阶段及其ontology ID）
  - 推荐字段明确为16项（管理/样本/实验/生信/文件属性）
  - 细化评级映射表（差/良/优三级）
  - 修正错字（disease字段名统一）
  - 更新项目综合评分标准（A/B/C类定义）

### v1 (2026-04-30)
- 初始版本发布
- 包含数据集元信息规范、文件元信息规范、数据标准化处理规范
- 支持单细胞转录组、单核转录组、scATAC-seq、空间转录组

## 文档内容

- **数据集元信息规范**
- **文件元信息规范**（通用字段、空间转录组Stereo-seq适配）
- **数据标准化处理规范**（H5AD格式、质量评估）
- **数据递交规范**

## 自动评估工具

本仓库提供自动评估脚本，用于评估Excel元信息完整度：

```bash
# 评估Excel文件（基于hesta.xlsx格式）
python scripts/evaluate_metadata.py "D:/OneDrive - BGI Tech Solutions (Hongkong) Co., Ltd/个人文件/项目/2026/高质量数据集/hesta.xlsx"
```

**评估结果示例**：
```
============================================================
Cell Standard v2 - Metadata Evaluation
============================================================

[DATA] Dataset: 1 rows x 4 cols
[FILE] File metadata: 79 samples

1. Core Fields Evaluation (8 items)
  [X] organism_taxid                     0/  79 (  0.0%)
  [X] tissue                             0/  79 (  0.0%)
  ...
  Core completeness: 0.0%

2. Recommended Fields Evaluation (16 items)
  [OK] sample_name                       CS19_CS20_CS23_snRNA
  [OK] library_strategy                   snRNA-seq
  ...
  Recommended completeness: 68.8%

3. Final Rating
  Rating: [差]
  Explanation: 核心字段缺失>=3项，数据无基本生物学价值
```

## 本地预览

```bash
pip install mkdocs mkdocs-material
cd cell-standard-docs
python -m mkdocs serve
```

访问 http://127.0.0.1:8000 预览文档。

## 在线文档

- GitHub仓库：https://github.com/Biometeor/cell-standard
- ReadTheDocs文档：https://cell-standard.readthedocs.io/

**导入ReadTheDocs步骤**：
1. 访问 https://readthedocs.org/dashboard/
2. 点击 "Import a Project"
3. 选择 Biometeor/cell-standard 仓库
4. 点击 "Next" → 系统自动识别 `.readthedocs.yaml`
5. 构建完成后访问：https://cell-standard.readthedocs.io/

## 参考标准

本标准参考了CellxGene的字段要求，适用于：
- 单细胞转录组 (scRNA-seq)
- 单核转录组 (snRNA-seq)
- 单细胞ATAC (scATAC-seq)
- 空间转录组 (Spatial Transcriptomics)

## 文件格式

- 数据格式：H5AD (AnnData)
- 文档格式：Markdown
- 构建工具：MkDocs + Material Theme
- 评估工具：Python + Pandas

## 项目结构

```
cell-standard-docs/
├── mkdocs.yml              # MkDocs配置
├── .readthedocs.yaml      # ReadTheDocs配置
├── README.md             # 项目说明
├── docs/
│   ├── index.md         # 文档内容（v2）
│   └── requirements.txt
├── scripts/
│   └── evaluate_metadata.py  # 自动评估脚本
└── .gitignore
```
