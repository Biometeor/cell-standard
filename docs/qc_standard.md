# 数据文件质控标准

在生成标准 H5AD 文件后，系统自动计算 QC 指标，并对单个文件进行评估。注意：数据文件评估值评估原始矩阵，缺失才会评估分析后数据，补充文件不进行评估。

## 4.1 质控字段

评估字段内容见下表：

[请至钉钉文档查看附件《细胞质控字段及标准》。](https://alidocs.dingtalk.com/i/nodes/YndMj49yWjPnow3RCDr97wjbJ3pmz5aA?iframeQuery=anchorId%3DX02mmkokhar39w5mdbp6rd)

## 4.2 评级标准

| 等级 | 定义 | 评判标准 |
| --- | --- | --- |
| 1级 | 优质 | 所有质控指标均在可接受范围内，且 spot_count ≥ 5000 |
| 2级 | 合格 | 核心质控指标（spot_count, gene_count, median_genes_per_spot）在可接受范围内 |
| 3级 | 让步接受 | 部分质控指标（≤3个）超出可接受范围，但仍有分析价值 |
| 4级 | 不合格 | 多个核心质控指标（>3个）超出可接受范围，不建议使用 |
