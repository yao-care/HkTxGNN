---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Letermovir：預測新適應症為外陰陰道念珠菌病 (Vulvovaginal Candidiasis)（證據等級 L5）。原適應症：巨細胞病毒感染 (Cytomegalovirus infection)"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Letermovir：從巨細胞病毒感染到外陰陰道念珠菌病

## 一句話總結

Letermovir 是一種抗巨細胞病毒（CMV）藥物，原本用於治療 CMV 感染。
TxGNN 模型預測它可能對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 巨細胞病毒感染 (Cytomegalovirus infection) |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知藥理而言，Letermovir 抑制 CMV DNA 終止酶複合體（pUL56/pUL51/pUL89），這個標的是疱疹病毒特有的，在念珠菌（真菌）中沒有已知的同源物。

因此，從現有資料看不出 Letermovir 具有抗黴菌活性的合理機轉。病毒感染與黴菌感染的病原體類型、藥物標的都不同，兩者之間缺乏直接的藥理關聯。

TxGNN 的高分（0.9988）來自知識圖譜的網路結構，並沒有任何試驗或文獻佐證。它可能反映的是網路假象，例如與其他抗感染藥物的共同關聯，或與免疫功能低下患者常見疾病的關聯，而非真正的藥理效果。這個預測應謹慎看待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66124 | PREVYMIS TABLETS 240MG | — | — |
| HK-66125 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 240MG/12ML | — | — |
| HK-66122 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 480MG/24ML | — | — |
| HK-66123 | PREVYMIS TABLETS 480MG | — | — |

以上 4 張許可證皆為單一成分製劑，狀態有效，持證商為 MERCK SHARP & DOHME (ASIA) LTD。

---

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共有 100 筆交互作用紀錄，以下為部分例子：
  - **嚴重（Major）**：Eliglustat、Naloxegol、Cisapride
  - **中度（Moderate）**：Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、Omeprazole、Lansoprazole、Aprepitant、Clarithromycin、Pioglitazone、Glimepiride、Saxagliptin 等

警語與禁忌症的資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5）。
- Letermovir 的已知標的為病毒特有，對念珠菌沒有明確的藥理依據，高分很可能是知識圖譜的假象。

**若要推進需要：**
- 補充作用機轉（MOA）資料，並確認是否有任何對真菌的活性依據
- 進行體外抗念珠菌活性試驗，作為最基本的前臨床證據
- 取得香港衛生署的仿單，補齊警語與禁忌症資料
- 確認給藥途徑與劑型是否適用於陰道局部或全身治療
- 在上述證據出現之前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

