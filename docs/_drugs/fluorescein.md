---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein：從眼底螢光造影診斷到變異型心絞痛

## 一句話總結

Fluorescein 是一種有機螢光染劑，在臨床上主要作為眼底螢光血管攝影（FA）的診斷造影工具，本身無已登記的治療適應症。
TxGNN 模型以 **99.81% 的高分**預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，
然而目前**無任何臨床試驗或文獻**直接支持此再利用假設，高分極可能來自知識圖譜的跨域統計關聯（假陽性）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 眼底螢光血管攝影診斷劑（無核准治療適應症） |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**簡短結論：此預測缺乏生物學合理性，高度懷疑為假陽性。**

Fluorescein 是一種有機螢光化合物（分子量 332.31 Da），可吸收藍光（490 nm）並發出黃綠色螢光（514 nm）。臨床上以靜脈注射方式給予後，可在眼底血管中清晰顯影，是螢光眼底血管攝影（FFA）、角膜染色（corneal staining）及淚膜破裂時間測定（TBUT）的標準工具。其藥理機轉為被動螢光標記，**不具備任何血管舒張、鈣離子拮抗（L-type VGCC 阻斷）或一氧化氮（NO）路徑調控活性**。

變異型心絞痛（Prinzmetal angina）的核心病理為冠狀動脈平滑肌痙攣，標準治療靠鈣離子拮抗劑（如 nifedipine、diltiazem）或硝酸鹽類（NO 供體）達到冠脈舒張效果。Fluorescein 完全不具此等藥理活性，在機轉層面與本適應症毫無關聯。

TxGNN 高分（0.998）極可能源自知識圖譜的結構性偏差：Fluorescein 大量出現於涉及視網膜血管疾病的研究脈絡中，模型可能因此學到它與「心血管系統」節點之間的統計共現關係，在圖譜中形成跨域連結，但並不代表真實的藥理關聯。此為典型的 **KG 假陽性**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Fluorescein 在香港目前無已登記藥品許可證，屬未上市狀態。如需了解其診斷試劑的監管地位，請向香港衛生署查詢。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Fluorescein 為純粹診斷性螢光染劑，完全不具備治療變異型心絞痛所需的藥理機轉（血管舒張、鈣離子拮抗、NO 調控），且無任何臨床試驗或文獻支持此再利用假設。TxGNN 預測分數雖高，但屬圖譜結構性假陽性，不具研究推進價值。

**若要推進需要：**
- 確認 Fluorescein 是否具有任何尚未發現的心血管藥理活性（目前無文獻依據，建議不推進）
- 補齊 DrugBank 完整 MOA 資料（DG002），排除資料缺口導致判斷偏差
- 確認 Fluorescein 在香港的藥品監管分類（診斷試劑 vs. 藥品）
- 建議優先轉向其他 TxGNN 候選——本藥物作為再利用標靶的整體可行性極低

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。所有老藥新用候選均需經臨床驗證後方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

