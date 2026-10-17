---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Plerixafor：預測新適應症為惰性漿細胞骨髓瘤 (Indolent Plasma Cell Myeloma)（證據等級 L5）。原適應症：漿細胞骨髓瘤 (plasma cell myeloma)"
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis"]
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Plerixafor：從多發性骨髓瘤到惰性漿細胞骨髓瘤

## 一句話總結

Plerixafor 是 CXCR4 拮抗劑，原本用於多發性骨髓瘤（漿細胞骨髓瘤）病人自體幹細胞移植前的造血幹細胞動員。
TxGNN 模型預測它可能對**惰性漿細胞骨髓瘤 (Indolent Plasma Cell Myeloma)** 有效。
目前**沒有臨床試驗和文獻**支持這個預測，僅有模型預測的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 漿細胞骨髓瘤 (plasma cell myeloma)；香港許可證未載明核准適應症文字 |
| 預測新適應症 | 惰性漿細胞骨髓瘤 (Indolent Plasma Cell Myeloma) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Plerixafor 是 CXCR4 拮抗劑，可阻斷 SDF-1/CXCL12 的結合。CXCR4/CXCL12 軸會把骨髓瘤細胞固定在骨髓微環境中，因此理論上把它們動員出來，可能讓它們對治療更敏感。這在生物學上是合理的。

不過要特別注意：plerixafor 目前在多發性骨髓瘤的臨床用途，是自體移植前的**造血幹細胞動員**，並不是抗骨髓瘤治療。模型分數雖高（0.9997），但主要反映的是藥物與漿細胞骨髓瘤本來就有的關聯，而不是針對「惰性」亞型的直接證據。目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位），以上機轉推論來自藥理資料與模型分析。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60176 | MOZOBIL INJ 20MG/ML（賽諾菲香港） | 注射劑 | 資料未載明 |
| HK-67839 | PLERIXAFOR SOLUTION FOR INJECTION 24MG/1.2ML（Sino Pacific Pharma） | 注射劑 | 資料未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：血小板低下症 (thrombocytopenia)、腎功能不全 (impaired renal function disease)、白血病 (leukemia)。
- **藥理交互作用**：已查詢到 2 項藥理標靶關聯，分別為 CXCR4 與 ACKR3；未提供具體的藥物間交互作用分級。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，沒有任何臨床試驗或文獻直接支持用於惰性漿細胞骨髓瘤，證據等級為 L5。
- 高分主要反映藥物與一般漿細胞骨髓瘤的既有關聯（幹細胞動員用途），並非抗腫瘤療效的證據。

**若要推進需要：**
- 釐清「惰性漿細胞骨髓瘤」的臨床定義，以及 plerixafor 在此族群的預期角色（動員、增敏或直接治療）。
- 蒐集 CXCR4/CXCL12 軸在骨髓瘤的前臨床與臨床文獻。
- 補齊 MOA 資料與香港仿單的警語及禁忌症，完成安全性篩檢。
- 評估血小板低下及腎功能不全族群的風險與劑量調整。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

