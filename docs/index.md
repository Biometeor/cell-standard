# 细胞高质量数据标准 v2

## 总则

为规范细胞组学测序数据的归档管理，确保数据的完整性、可用性及互操作性，特制定本标准。本标准旨在统一数据格式（H5AD）、明确元信息填报规范，并建立自动化的数据质量评估体系，以支持后续的数据挖掘与共享。本标准为和国际接轨，参考了CellxGene的字段要求。

**适用范围**：本标准适用于所有递交至本系统的以下类型测序数据：
- 单细胞转录组 (scRNA-seq)
- 单核转录组 (snRNA-seq)
- 单细胞ATAC (scATAC-seq)
- 空间转录组 (Spatial Transcriptomics)

## 文档导航

本标准分为以下核心章节：

1. **[元信息规范](metadata.md)** - 数据集元信息、文件元信息（通用字段、空间转录组Stereo-seq适配）、补充文件规范

2. **[数据标准化处理规范](standardization.md)** - H5AD格式标准、插槽结构规范（通用属性、空间属性）

3. **[数据文件质控标准](qc_standard.md)** - 质控字段、单文件评级标准（1-4级）

4. **[项目数据评估打分](project_evaluation.md)** - 项目级统计、元信息完整度评分、综合评级流程

## 快速链接

- **GitHub仓库**：https://github.com/Biometeor/cell-standard
- **自动评估工具**：`python scripts/evaluate_metadata.py <excel_file>`
- **本地预览**：`python -m mkdocs serve`

## 参考标准

本标准参考了CellxGene的字段要求，确保与国际接轨。
