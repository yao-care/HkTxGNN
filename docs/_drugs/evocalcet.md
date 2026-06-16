---
layout: default
title: Evocalcet
parent: 中證據等級 (L3-L4)
nav_order: 301
evidence_level: L4
indication_count: 5
---

# Evocalcet
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Evocalcet：從繼發性副甲狀腺機能亢進到高磷血症

## 一句話總結

Evocalcet 是第二代口服擬鈣劑（calcimimetic），原本用於慢性腎病（CKD）患者的繼發性副甲狀腺機能亢進（SHPT）治療。
TxGNN 模型預測它可能對**高磷血症（Hyperphosphatemia）**有效，
目前有 **2 篇文獻**支持此方向，尚無相關臨床試驗登記。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 繼發性副甲狀腺機能亢進（SHPT in CKD，依文獻推斷） |
| 預測新適應症 | 高磷血症（Hyperphosphatemia） |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Evocalcet（MT-4580/KHK7580）是新一代口服擬鈣劑，透過活化鈣敏感受體（CaSR）來抑制副甲狀腺素（PTH）的分泌。相較於第一代擬鈣劑 cinacalcet，evocalcet 的胃腸道副作用顯著較少，且在體內外試驗中對 CYP 同功酶的干擾也更低——這是其開發的主要優勢所在。

在 CKD 礦物質骨骼疾病（CKD-MBD）情境下，PTH 持續過高會促進骨骼釋放磷酸鹽，同時影響腎小管對磷的重吸收調節。因此，透過 CaSR 活化抑制 PTH，理論上可間接降低血磷濃度（路徑：CaSR 活化 → PTH 抑制 → 骨骼磷酸鹽釋出減少 + 腎小管磷重吸收改變）。TxGNN 預測分數極高（99.97%），反映知識圖譜中 SHPT 與高磷血症節點的高度共病關聯。

然而，**evocalcet 並非直接降磷藥物**，高磷血症的標準治療仍為磷酸鹽結合劑。Evocalcet 對血磷的影響屬間接且輔助性的調控，不能取代主流降磷治療。此外，目前缺乏詳細的 MOA 資料（DrugBank DB12388 未取得），機轉連結的深度分析受到限制。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [29614098](https://pubmed.ncbi.nlm.nih.gov/29614098/) | 2018 | 機轉/前臨床 | PloS ONE | Evocalcet 體內外抑制副甲狀腺細胞功能，GI 副作用及 CYP 干擾均低於 cinacalcet；研究涵蓋 SHPT 中 PTH 對高磷調控的機轉討論 |
| [40471524](https://pubmed.ncbi.nlm.nih.gov/40471524/) | 2025 | 病例報告 | Clinical Journal of Gastroenterology | 先天性肝臟纖維化合併多囊腎患者，因繼發性 SHPT 快速出現瀰漫性肝臟鈣化及異位鈣化，呈現高磷血症與 SHPT 管控失控的後果 |

---

## 香港上市資訊

Evocalcet 目前在香港尚未取得任何藥品許可證，無上市記錄。

（備註：Evocalcet 於 2018 年在日本由 PMDA 核准，商品名 Orkedia，適應症為透析患者的 SHPT。如需參考臨床安全性資料，可引用日本 PMDA 核准資訊。）

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有機轉／前臨床層級的間接證據（L4），對高磷血症無任何直接臨床試驗；evocalcet 在香港尚未上市，缺乏完整安全性資料。機轉連結屬間接調控路徑，不具直接靶向高磷血症的作用，整體證據強度不足以推進再利用評估。

**若要推進需要：**
- 取得 evocalcet 在 CKD-MBD 患者中對血磷影響的原廠臨床試驗資料（如 PMDA 申請資料）
- 補充完整 MOA 資料（DrugBank DB12388）以支撐機轉關聯性分析
- 確認香港特殊進口（特患用藥）途徑的可行性，或評估是否可援引日本 PMDA 核准資料
- 補充仿單警語與禁忌資訊（目前為資料缺口，嚴重性：Blocking）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

