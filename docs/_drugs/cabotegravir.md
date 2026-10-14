---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

# Cabotegravir：從 HIV 感染到類風濕性關節炎

## 一句話總結

Cabotegravir 是一種 HIV 整合酶抑制劑（INSTI），在香港以 Vocabria 品牌上市，有口服錠劑與長效注射劑型。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效。
目前**沒有任何臨床試驗或文獻**支持，這僅是模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症（依藥理分類，屬 HIV 整合酶抑制劑） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cabotegravir 屬於 HIV 整合酶抑制劑，其作用是阻斷病毒 DNA 整合入宿主基因組。這個機轉與類風濕性關節炎的病理（TNF、IL-6、JAK/STAT、B/T 細胞訊號）沒有已知的直接關聯。

以目前資料，無法建立兩者之間合理的機轉連結。0.995 的分數僅反映知識圖譜上的關聯性，不能視為生物學上的證據。

TxGNN 另外預測的其他適應症（原發性硬化性膽管炎、支氣管炎、一種極罕見的遺傳發育症候群、重度非增殖性糖尿病視網膜病變）同樣沒有臨床或文獻支持，也缺乏機轉依據，分數雖高（約 99.0%–99.2%），但仍為純模型預測，證據等級均為 L5，建議均為 Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67297 | VOCABRIA PROLONGED-RELEASE SUSPENSION FOR INJECTION 600MG/3ML | 長效注射懸浮液 | 許可證資料未載明 |
| HK-67298 | VOCABRIA TABLETS 30MG | 錠劑 | 許可證資料未載明 |
| HK-67296 | VOCABRIA PROLONGED-RELEASE SUSPENSION FOR INJECTION 400MG/2ML | 長效注射懸浮液 | 許可證資料未載明 |

三張許可證皆由 GlaxoSmithKline Limited 持有，均為單方製劑且狀態有效。

---

## 安全性考量

- **藥物交互作用**：已查詢到 7 項中度交互作用，均屬含多價陽離子的抗酸劑或補充劑：
  - 碳酸鈣 (Calcium carbonate)
  - 氫氧化鋁 (Aluminum hydroxide)
  - 碳酸鎂 (Magnesium carbonate)
  - 氫氧化鎂 (Magnesium hydroxide)
  - 氧化鎂 (Magnesium oxide)
  - 碳酸氫鈉 (Sodium bicarbonate)
  - 檸檬酸鈉 (Sodium citrate)

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗、文獻或可成立的機轉依據（證據等級 L5）。
- 原適應症、作用機轉與仿單安全性資料目前也不完整，無法進一步評估。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 Cabotegravir 的作用機轉資料（如 DrugBank）
- 針對類風濕性關節炎進行文獻與臨床試驗系統性檢索，並評估是否有任何免疫調節相關的前臨床證據
- 若日後有證據出現，再評估長效注射劑型與新適應症的給藥途徑是否相容
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

