# 细胞高质量数据标准 v1

本仓库包含《细胞高质量数据标准v1》的完整文档，使用MkDocs构建，支持在ReadTheDocs上自动生成文档网站。

## 文档内容

- **数据集元信息规范**
- **文件元信息规范**（通用字段、空间转录组Stereo-seq适配）
- **数据标准化处理规范**（H5AD格式、质量评估）
- **数据递交规范**

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

## ReadTheDocs 配置

代码推送后，访问 https://readthedocs.org/dashboard/ 完成配置：

1. 点击 "Import a Project"
2. 选择 "Biometeor/cell-standard" 仓库
3. 点击 "Next" → 系统自动识别 `.readthedocs.yaml`
4. 构建完成后访问：https://cell-standard.readthedocs.io/

配置文件已就绪：`.readthedocs.yaml`

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
