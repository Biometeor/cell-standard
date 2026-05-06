# 数据标准化处理规范

系统接收用户递交的数据后，将执行标准化处理流程，将异构数据统一转换为 H5AD (AnnData) 格式，并固定内部插槽结构，以确保下游分析工具（如 Scanpy、CellxGene）的兼容性。

## 3.1 标准化输出格式

所有入库数据最终转换为 .h5ad 格式，文件命名规范为 {sample_id}.h5ad。

## 3.2 H5AD 插槽结构规范

系统将按照以下映射逻辑填充 H5AD 内部插槽：

### 索引规范：

- **adata.obs.index**：必须为 细胞条码，格式通常为 AAACATACAAAAGT-1。建议拼接样本 ID 以防止重复，如 S001_AAACATACAAAAGT-1。

- **adata.var.index**：必须为 基因 ID (Gene ID)（如 Ensembl ID: ENSG000001234），不建议仅使用 Gene Symbol，避免歧义。

### 3.2.1 通用属性

| 插槽路径 | 字段名 | 数据类型 | 必选 | 说明 |
| --- | --- | --- | --- | --- |
| .X | main_matrix | Sparse/Matrix | 必选 | 主表达矩阵。归档建议存储 归一化 后的数据（如 LogNormalized, CPM），便于直接可视化和分析。 |
| .layers['raw_counts'] | raw_counts | Sparse/Matrix |  | 原始计数矩阵。用于封存原始数据，数值必须为整数。 |
| .obs['cell_type'] | cell_type | Category | 必选 | 细胞类型注释。如 CD4+ T cell, B cell。 |
| .obsm['X_pca'] | X_pca | Matrix | 必选 | PCA 降维结果 (通常 50 维)。 |
| .obsm['X_umap'] | X_umap | Matrix | 可选 | UMAP 二维坐标。这是可视化的默认选择。 |
| .obsm['X_tsne'] | X_tsne | Matrix | 可选 | t-SNE 二维坐标。 |

### 3.2.2 空间属性

| 插槽路径 | 字段名 | 数据类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| .obs['pixel_x'] | pixel_x | Float | 可选 | 像素级 X 坐标。 |
| .obs['pixel_y'] | pixel_y | Float | 可选 | 像素级 Y 坐标。 |
| .obsm['spatial'] | spatial | Matrix | 必选 | 空间坐标信息 |
| .uns['spatial'] | spatial_info | Dictionary | 必选 | 空间相关信息，包括图像路径、尺度因子等。 |
