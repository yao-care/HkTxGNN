---
layout: default
title: Cetrorelix
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cetrorelix：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：抑制接受控制性卵巢刺激之女性的早發性 LH 高峰"
monitor_inn: "CETRORELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Cetrorelix：從控制性卵巢刺激（抑制早發性 LH 高峰）到多毛症（Hypertrichosis）
{: .text-alpha }

## 一句話總結

Cetrorelix 是一種 GnRH 受體拮抗劑，臨床上用於接受控制性卵巢刺激的女性，以抑制過早出現的 LH 高峰。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抑制接受控制性卵巢刺激之女性的早發性 LH 高峰（依藥理資料；香港許可證未載明適應症文字） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未取得）。根據藥理資料，Cetrorelix 是作用於人類 GnRH₁ 受體（GNRHR）的拮抗劑，可抑制 LH／FSH 分泌，進而降低性腺的雄性素生成。

理論上，雄性素訊號下降可能影響依賴雄性素的毛髮生長。但多數多毛症（先天性、藥物誘發或代謝性）並非雄性素依賴型，因此機轉連結薄弱且屬推測。

TxGNN 的高分來自知識圖譜的網路鄰近關係，並無臨床或文獻佐證。排名前五的預測（多毛症、Ambras 型先天性全身多毛症、牙齒／牙周畸形症候群、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常）多屬發育或結構性疾病，GnRH 拮抗並無明確的藥理依據。

在其他預測中，機轉上最合理的是**中樞性性早熟**（GnRH 軸提前活化，抑制 GnRH 軸在機轉上說得通）。目前標準治療為長效 GnRH 促效劑，Cetrorelix 屬短效劑型且缺乏兒童資料，實用性受限，且同樣僅為預測。**家族性男性限定性性早熟**的缺陷位於 GnRH／LH 下游，單用 GnRH 拮抗劑預期無效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46953 | CETROTIDE FOR INJ 0.25MG | 注射劑 | 許可證資料未載明 |
| HK-67739 | CETROTIDE POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 0.25MG | 注射劑（粉末與溶劑） | 許可證資料未載明 |

兩張許可證皆為單方、有效，持有人為 Merck Pharmaceutical (HK) Limited。

## 安全性考量

- **藥物交互作用**：目前僅有藥理層面的資料，顯示作用標的為 GnRH₁ 受體，未有具體藥物間交互作用的分級資訊。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測均無臨床試驗或文獻支持，僅有模型預測。排名第一的多毛症機轉連結薄弱，不建議推進。
- 香港許可證缺少適應症與仿單安全性資料，無法進入安全性初篩。

**若要推進需要：**
- 取得香港衛生署仿單，補齊適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 若要探索，建議優先評估**中樞性性早熟**：進行文獻回顧，並確認短效劑型與兒童用藥的可行性
- 多毛症需先釐清是否為雄性素依賴型，再決定是否有研究價值
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

