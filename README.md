# HkTxGNN - 香港：老藥新用預測

[![Website](https://img.shields.io/badge/Website-hktxgnn.yao.care-blue)](https://hktxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

使用 TxGNN 模型對香港註冊藥品進行老藥新用（drug repurposing）預測。

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議。
- 老藥新用候選需經過臨床驗證才能應用。

## 專案概覽

| 項目 | 數量 |
|------|------|
| **藥物報告** | 1,261 |
| **預測總數** | 21,717,892 |

## 預測方法

### 知識圖譜方法（Knowledge Graph）
直接查詢 TxGNN 知識圖譜中的藥物-疾病關係，基於生物醫學網絡中的現有連接識別潛在的老藥新用候選。

### 深度學習方法（Deep Learning）
使用 TxGNN 預訓練神經網絡模型計算預測分數，評估已批准藥物的新治療適應症的可能性。

## 連結

- 網站：https://hktxgnn.yao.care
- TxGNN 論文：https://doi.org/10.1038/s41591-023-02233-x
