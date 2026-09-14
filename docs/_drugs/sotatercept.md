---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
---

# Sotatercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sotatercept：從肺動脈高壓到急性淋巴性白血病

## 一句話總結

Sotatercept 是 ActRIIA-Fc 融合蛋白，原本核准用於治療肺動脈高壓（商品名 Winrevair）。
TxGNN 模型預測它可能對**急性淋巴性白血病 (Acute Lymphoblastic Leukemia)** 有效，
但目前**沒有任何臨床試驗或文獻支持**，且資料本身也指出此預測與白血病增生機轉無已知直接關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺動脈高壓（據 rationale 描述，Winrevair） |
| 預測新適應症 | 急性淋巴性白血病 (Acute Lymphoblastic Leukemia) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Sotatercept 為 ActRIIA-Fc 融合蛋白，透過捕捉 activin/GDF 配體，調節 BMP/activin 訊號傳導，
目前已核准用於肺動脈高壓的治療。

急性淋巴性白血病主要由白血病細胞異常增生驅動，與 activin/BMP 訊號路徑目前**無已知直接機轉關聯**。
資料本身也明確指出：TxGNN 給出的高分「可能反映知識圖譜中共病或治療交互節點的統計關聯，非機轉驅動」，
並建議先補齊原始藥理資訊（作用機轉目前標記為資料缺口）再評估。

換句話說，這個預測目前**應視為假說階段**，而非有機轉支持的候選方向。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

Sotatercept 目前**未在香港上市**，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測候選（供參考）

本次 Evidence Pack 同時列出 10 個預測適應症，**全數為 L5（僅模型預測、無臨床試驗或文獻證據）、建議 Hold**。
值得注意的是資料本身在機轉合理性上做了分級評語：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉合理性評語 |
|------|-----------|-----------|---------------|
| 4 | Drug-induced osteoporosis | 99.65% | **十項中機轉最具合理性者**：早期開發（ACE-011）曾針對 activin A 抑制骨吸收/促進成骨進行研究 |
| 2 | Severe nonproliferative diabetic retinopathy | 99.77% | 理論上可能（TGF-β家族與血管新生），未經驗證 |
| 3 | Diabetic retinopathy | 99.72% | 同上，無直接證據 |
| 5 | Diabetic cataract | 99.49% | 無機轉關聯報導 |
| 6 | HER2 positive breast carcinoma | 99.43% | 與 HER2 特異性路徑無直接連結 |
| 7–10 | 泌尿上皮癌群集 | 99.34–99.39% | 資料標註為 KG 節點群聚效應，非獨立藥理證據 |

若後續要進一步探索，rank 4（drug-induced osteoporosis）在機轉邏輯上優於本報告主標題的 rank 1（ALL）。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（急性淋巴性白血病）無臨床試驗、無文獻，且機轉關聯性薄弱，資料本身建議先補齊藥理資訊再評估。
- 全部 10 個候選適應症皆為 L5 等級，無實質研究支持。

**若要推進需要：**
- 補齊 Sotatercept 完整作用機轉（MOA）資料（DG002）
- 取得 TFDA/原廠仿單警語與禁忌症資料，以完成 S1 安全性初評（DG001，目前為 Blocking 缺口）
- 若優先探索機轉較合理的候選（drug-induced osteoporosis），需另行收集臨床前藥理證據
- 確認香港/台灣上市登記狀態（目前 0 張許可證，未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

