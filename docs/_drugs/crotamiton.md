---
layout: default
title: Crotamiton
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Crotamiton：預測新適應症為恙蟎皮膚侵擾症 (Trombiculiasis)（證據等級 L5）。原適應症：疥瘡、挪威疥、蟎蟲感染"
monitor_inn: "Crotamiton"
predicted_indications: ["lymph node palisaded myofibroblastoma", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "abdominal ectopic pregnancy", "disease of uterine broad ligament", "disease of retroperitoneum", "sacrum chordoma", "urethral disease", "hordeolum"]
---

# Crotamiton
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

# Crotamiton：從疥瘡到恙蟲病性皮膚炎（Trombiculiasis）

## 一句話總結

Crotamiton 是外用殺疥蟎與止癢藥，原本用於治療疥瘡（含挪威疥）及蟎蟲感染。
TxGNN 模型預測它可能對**恙蟎皮膚侵擾症 (Trombiculiasis)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持，僅屬模型預測與機轉類比的研究假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 疥瘡、挪威疥、蟎蟲感染（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 恙蟎皮膚侵擾症 (Trombiculiasis) |
| TxGNN 預測分數 | 96.24% |
| 證據等級 | L5（僅有模型預測，無實際研究；資料庫內部標記為 L4，此處依本報告規則判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold（以研究假說形式保留，待補充證據） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Crotamiton 對疥蟎 (*Sarcoptes scabiei*) 具殺蟲活性，同時具有止癢作用。其殺疥機轉未明；止癢方面，有報告指出它可能抑制皮膚與初級感覺神經元表現的 TRPV4（瞬時受體電位香草酸 4）通道。

恙蟎皮膚侵擾症是恙蟎幼蟲叮咬引起的蟎蟲性搔癢皮膚病，與疥瘡同屬蟎蟲相關的搔癢性皮膚病。Crotamiton 的殺蟎與止癢雙重特性，使這個預測在生物學上合理。高分很可能反映它與原適應症的相似性。

不過這只是間接推論，沒有試驗或文獻佐證。前 10 名預測中，其餘 9 項（如淋巴結柵欄狀肌纖維母細胞瘤、骶骨脊索瘤、異位妊娠等）缺乏合理機轉，應視為圖譜運算的假象，不建議追蹤。

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
| HK-48390 | EUROTON CREAM 10% | 未提供 | 未提供 |
| HK-23708 | EUROSIN CREAM 10% | 未提供 | 未提供 |
| HK-40775 | MECROTON CREAM 10% | 未提供 | 未提供 |
| HK-00172 | EURAX CREAM 10% | 未提供 | 未提供 |
| HK-01168 | HI VETIC SOLUTION | 未提供 | 未提供 |

另有 1 張有效許可證（HK-47770，MENTHOLATUM AD CREAM），共 6 張，皆為單方、有效。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：皮膚炎（dermatitis）。此為圖譜推論，並非仿單內容。
- **藥理交互作用**：Crotamiton 抑制 TRPV4 通道（藥理學標靶資料，非臨床藥物交互作用）。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 恙蟎皮膚侵擾症的預測在機轉上合理（殺蟎加止癢），但沒有任何臨床試驗或文獻，僅是模型預測。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，解析警語、禁忌與核准適應症。
- 補充 Crotamiton 的作用機轉資料（如 DrugBank）。
- 系統性搜尋 Crotamiton 用於恙蟎皮膚炎、蟎蟲叮咬搔癢的臨床與文獻證據。
- 評估外用劑型與恙蟎叮咬部位的適用性，以及皮膚炎患者的使用風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

