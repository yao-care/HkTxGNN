---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 2
---

# Panitumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Panitumumab：從轉移性大腸直腸癌到藥物引發性骨質疏鬆症

## 一句話總結

Panitumumab 是全人源抗 EGFR 單株抗體，臨床上用於轉移性大腸直腸癌治療。
TxGNN 模型預測它可能對**藥物引發性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，
但目前**無任何臨床試驗或文獻支持**，且模型本身的機轉分析認為這是高假陽性風險的配對。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性大腸直腸癌（依機轉關聯性描述，非本地核准資料） |
| 預測新適應症 | 藥物引發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.13% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Panitumumab 詳細的作用機轉資料（原始 MOA 標註為 Data Gap）。根據 evidence pack 中的機轉分析，Panitumumab 為全人源抗 EGFR 單株抗體，臨床上用於轉移性大腸直腸癌，其機轉是阻斷 EGFR 訊號路徑抑制腫瘤增生。

EGFR 訊號路徑與骨代謝（成骨細胞/蝕骨細胞調控）確實有文獻報導的關聯，但方向多指向 **EGFR 抑制與骨密度負向變化**——也就是說，抑制 EGFR 較可能是造成骨質流失的**風險因子**，而非治療骨質疏鬆症的機轉。因此這組配對屬於 TxGNN 高分但機轉方向相反、缺乏合理性支持的預測，需以懷疑角度看待。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Panitumumab 目前未在香港上市，無許可證資料。

## 其他預測適應症（Rank 2，僅供參考）

| 疾病 | TxGNN 分數 | 證據等級 | 機轉合理性 |
|------|-----------|---------|-----------|
| Severe Nonproliferative Diabetic Retinopathy（重度非增殖性糖尿病視網膜病變） | 99.05% | L5 | 低——Panitumumab 為抗 EGFR 而非抗 VEGF 藥物，與該病常見的抗血管新生治療機轉無直接關聯，且全身性給藥有已知眼毒性疑慮 |

## 細胞毒性

Panitumumab 屬於標靶藥物（抗 EGFR 單株抗體），非傳統細胞毒性化療藥物，骨髓抑制並非其主要已知風險。詳細毒性資料請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
兩個預測適應症皆為 L5（僅模型預測），無任何臨床試驗或文獻佐證；且第一名候選（藥物引發性骨質疏鬆症）的機轉分析顯示 EGFR 抑制與骨質流失可能為同向風險關係而非治療關係，假陽性風險高。此外藥物在香港未上市，也缺乏 MOA 及仿單安全性資料。

**若要推進需要：**
- 取得 Panitumumab 完整作用機轉（MOA）資料
- 取得原廠仿單警語與禁忌症（目前為 Blocking 等級資料缺口）
- 針對 EGFR 路徑與骨代謝關聯進行文獻回顧，確認方向是否真為治療性而非致病性
- 若機轉方向確認不利，建議直接排除此候選，避免佔用後續驗證資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

