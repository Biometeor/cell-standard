# 数据文件质控标准

在生成标准 H5AD 文件后，系统自动计算 QC 指标，并对单个文件进行评估。注意：数据文件评估只评估原始矩阵，缺失才会评估分析后数据，补充文件不进行评估。

## 4.1 质控字段

### 4.1.1 单细胞转录组 (scRNA-seq)

| 统计字段 | 必选 | 1级 | 2级 | 3级 | 定义 |
| --- | --- | --- | --- | --- | --- |
| total_valid_cells | 必选 | < 1000 | 1000-2000 | > 2000 | 经过过滤表达值都为空后保留的细胞数。 |
| Median Genes per Cell | 必选 | 500 - 1,000 | 1,000 - 2,000 | > 2,000 | 每个细胞中检测到的基因数量的中位数。 |
| Median UMI per Cell | 必选 | 500 - 1,000 | 1,000 - 5,000 | > 5,000 | 每个细胞中检测到的UMI（分子标签）数量的中位数。 |
| Mitochondrial Fraction (%) | 必选 | — | — | — | 线粒体基因UMI数占总UMI数的比例。研究用 <10% 作为常见阈值，但会随组织/细胞类型变化，所以不做评分。 |
| Ribosomal Fraction (%) | 可选 | — | — | — | 核糖体蛋白基因 UMI / 总 UMI，也会随组织/细胞类型变化，所以不做评分，植物不涉及，动物可纳入评分。 |
| Low Quality Cell Rate (%) | 必选 | 25% - 40% | 10% - 25% | < 10% | 低质量细胞（低基因数<500）占总检测细胞的比例。 |
| Doublet Rate (Predicted) (%) | 可选 | 10% - 20% | 5% - 10% | < 5% | 预测的双细胞（两个细胞被包裹在一个液滴中）比例。 |
| Cell Cluster Separation | 可选 | < 0.1 | 0.1 - 0.25 | > 0.25 | 基于轮廓系数评估的细胞聚类分离程度。 |
| Batch Effect Removal Efficiency (R²) | 可选 | R² > 0.15 | R² 0.05 - 0.15 | R² < 0.05 | 批次效应校正后，批次因素在降维空间中的解释方差（R²越小越好）。 |
| Cell Type Annotation Rate (%) | 可选 | < 70% | 70% - 90% | > 90% | 成功注释到具体细胞类型的细胞比例。 |
| Cell Type Consistency (%) | 可选 | < 70% | 70% - 90% | > 90% | 同一细胞类型在不同样本/批次间的标签一致性。 |
| 环境RNA污染 | — | — | — | — | 环境RNA污染评估。 |
| sparsity | — | — | — | — | 矩阵零元占比，过高通常意味着测序不足或样本质量差。 |

### 4.1.2 空间转录组 (Spatial)

| 字段名 | 说明 | 可选 | 单位 | 可接受范围 | 备注 |
| --- | --- | --- | --- | --- | --- |
| spot_count | 有效 spot 数量 | 必选 | 个 | ≥ 2000 | 在组织范围内，有UMI的spot |
| gene_count | 检测到的基因数量 | 必选 | 个 | ≥ 5000 | 整个组织抓到的UMI对应unique gene种类数 |
| median_genes_per_spot | 每个 spot 的中位基因数 | 必选 | 个 | ≥ 500 |  |
| mean_genes_per_spot | 每个 spot 的平均基因数 | 必选 | 个 | ≥ 400 |  |
| median_counts_per_spot | 每个 spot 的中位计数 | 必选 | 个 | ≥ 1000 |  |
| mean_umi_per_spot | 每个 spot 的平均 UMI 数 | 必选 | 个 | ≥ 800 |  |
| Unique_Reads | 纠错后去重的Reads数 | 可选 | 个 | ≥100M | Stereo-seq Only |
| Total_Reads | 总Reads数 | 可选 | 个 | ≥1G |  |
| Valid_Barcode_Reads | 有效分子标签Reads比例 | 可选 | % | ≥75 | Stereo-seq Only |
| Unique_Mapped_Reads | 唯一比对到参考基因组的Reads比例 | 可选 | % | ≥70 | Stereo-seq Only |
| rna_mapping | 整体rna的比对率 | 可选 | % | ≥85 |  |
| mean_umi_per_Bin200 | Bin200下平均UMI数 | 可选 | 个 | ≥50000 | Stereo-seq Only |
| Mean Gene Type per Bin200 | Bin200下平均基因种类数 | 可选 | 个 | ≥5000 | Stereo-seq Only |
| mitochondrial_percentage | 线粒体基因比例 | 可选 | % | 统计但不纳入评价 | 植物中作为重要指标 |
| ribosomal_percentage | 核糖体基因比例 | 可选 | % | 统计但不纳入评价 |  |
| tissue_coverage | 组织覆盖率 | 可选 | % | ≥ 50 |  |
| fraction_of_spots_under_tissue | 组织下的 spot 比例 | 可选 | % | ≥ 70 | 组织下的spot / 有UMI的spot比例 |
| tissue_area_coverage | 组织面积覆盖率 | 可选 | % | ≥ 60 | 统计 Spot 覆盖的组织面积 / 总组织面积占比 |
| image_resolution | 图像分辨率 | 可选 | px | ≥ 1024×1024 |  |
| image_contrast | 图像对比度（PSNR） | 可选 | dB | ≥ 20 |  |
| alignment_quality | 对齐质量 | 可选 | 评分 | ≥ 0.8 | 图像与 Spot 对齐准确度，反映空间分子-影像匹配度 |
| low_information_spot_rate | 低信息 spot 率 | 可选 | % | ≤ 10 | 基因数小于50，或UMI小于100的spot |
| cluster_marker_gene_specificity | 聚类标记基因特异性 | 可选 | % | ≥ 70 | 统计 marker 基因在目标聚类区域的表达占比 |
| tissue_region_gene_expression_consistency | 组织区域-基因表达一致性 | 可选 | % | ≥ 60 | 验证已知组织区域的特征基因表达匹配度 |

### 4.1.3 单细胞ATAC (scATAC-seq)

| 评价字段 | 必选 | 1级 | 2级 | 3级 | 定义 | 级别说明 |
| --- | --- | --- | --- | --- | --- | --- |
| Estimated Number of Cells | 必选 | 实际/预期 < 40% | 40% - 70% | > 70% | 经过滤后保留的有效细胞核数量。 | ATAC实验涉及细胞核提取，3级代表核提取效率高且完整性好。 |
| Median Fragments per Cell | 必选 | 1,500 - 3,000 | 3,000 - 10,000 | > 10,000 | 每个细胞中检测到的有效Unique Fragments数量中位数。 | ATAC数据稀疏，需要足够的Fragments支持。3级适合精细的Motif分析。 |
| TSS Enrichment Score | 必选 | 1 | 1 - 3 | > 4 | 转录起始位点(TSS)附近的Fragment富集程度。 | ATAC核心质控指标。数值越高，说明染色质开放区域信号越真实，背景噪音越低。 |
| FRiP (Fraction of Reads in Peaks) | 必选 | 20% - 30% | 30% - 50% | > 50% | 落在Peak区域内的Reads占总Reads的比例。 | 衡量有效信号占比。3级表示Peak calling质量高，非特异性背景低。 |
| Nucleosome Signal | 必选 | > 2.0 | 1.5 - 2.0 | < 1.5 | 核小体信号强度。 | ATAC数据应呈现清晰的核小体条带模式。数值过高可能代表实验中存在核小体堆积或Tn5切割异常。 |
| Doublet Rate (Predicted) (%) | 必选 | 10% - 20% | 5% - 10% | < 5% | 预测的双细胞核比例。 | ATAC双细胞更难识别，低双细胞率对后续整合分析至关重要。 |
| Low Quality Cell Rate (%) | 必选 | 25% - 40% | 10% - 25% | < 10% | 低质量细胞核（低Fragment数、低TSS富集）的比例。 | 反映细胞核制备的质量。1级可能由于裂解过度或细胞核破损导致。 |
| Capture Efficiency (%) | 可选 | < 50% | 50% - 70% | > 70% | 有效细胞核捕获率。 | 3级代表转座反应和液滴生成过程高效稳定。 |
| Cell Cluster Separation | 可选 | < 0.1 | 0.1 - 0.2 | > 0.2 | 聚类轮廓系数。 | ATAC数据高维稀疏，聚类分离度通常低于RNA。3级代表亚群特征Peak差异明显。 |
| Batch Effect Removal Efficiency (R²) | 可选 | R² > 0.15 | R² 0.05 - 0.15 | R² < 0.05 | 批次效应在低维嵌入空间中的解释方差。 | 评估Harmony、LSI等校正方法的效果。 |
| Cell Type Annotation Rate (%) | 可选 | < 70% | 70% - 90% | > 90% | 基于基因活性或Peak特征成功注释的细胞比例。 | ATAC注释难于RNA，3级通常需要高质量的参考数据集或整合分析。 |
| Cell Type Consistency (%) | 可选 | < 70% | 70% - 90% | > 90% | 细胞类型标签在样本间的一致性。 | 3级证明染色质开放特征在不同个体间具有高度可重复性。 |

## 4.2 评级标准

| 等级 | 定义 | 评判标准 |
| --- | --- | --- |
| 1级 | 优质 | 所有质控指标均在可接受范围内，且 spot_count ≥ 5000 |
| 2级 | 合格 | 核心质控指标（spot_count, gene_count, median_genes_per_spot）在可接受范围内 |
| 3级 | 让步接受 | 部分质控指标（≤3个）超出可接受范围，但仍有分析价值 |
| 4级 | 不合格 | 多个核心质控指标（>3个）超出可接受范围，不建议使用 |
