---
layout: default
title: Axitinib
parent: 高證據等級 (L1-L2)
nav_order: 89
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Axitinib：預測新適應症為Xp11.2 易位/TFE3 基因融合型腎細胞癌（證據等級 L2）。原適應症：腎細胞癌（透明細胞腎癌等）"
monitor_inn: "Axitinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Axitinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

## Axitinib：從腎細胞癌到 Xp11.2 易位/TFE3 基因融合型腎細胞癌
{: .text-alpha }

## 一句話總結

Axitinib 是一種口服 VEGFR 抑制劑，原本用於治療腎細胞癌（含透明細胞腎癌）。
TxGNN 模型預測它可能對**Xp11.2 易位/TFE3 基因融合型腎細胞癌**有效，
目前有 **1 個直接相關的臨床試驗**（Phase 2，僅 15 人，尚無結果），另有多項腎細胞癌大型研究提供間接支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎細胞癌（透明細胞腎癌等）；香港許可證資料未載明適應症文字，此處依知識圖譜 |
| 預測新適應症 | Xp11.2 易位/TFE3 基因融合型腎細胞癌 |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位無資料）。根據已知資訊，Axitinib 是選擇性的 VEGFR1-3 抑制劑，透過阻斷 VEGF 驅動的血管新生來抑制腫瘤生長。文獻也將其描述為口服、強效且具選擇性的酪胺酸激酶抑制劑。

Xp11.2/TFE3 易位型腎細胞癌是罕見的腎細胞癌亞型，在生物學上與 VEGF 驅動的血管新生有關。原適應症同為腎細胞癌，因此 VEGFR 抑制在機轉上有合理的延伸空間。

需要注意：目前唯一的直接證據是一個很小的 Phase 2 試驗（n=15），仍在進行中且尚無發表結果。因此這只能視為假說層級的支持，而非確認療效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | 進行中（不再招募） | 15 | 隨機分配比較 Axitinib＋Nivolumab 與單用 Nivolumab，用於無法切除或已轉移的 TFE/易位型腎細胞癌；尚無結果 |

## 文獻證據

目前無針對此亞型的相關文獻。

（間接證據：Axitinib 在一般腎細胞癌的 Phase 3 RCT 已有確立的療效，包括 AXIS 試驗、KEYNOTE-426 及 JAVELIN Renal 101，但這些試驗主要納入透明細胞腎癌，不能直接推論至 TFE3 易位型。）

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62088 | INLYTA TAB 1MG（Pfizer） | 錠劑 | 請參考原廠仿單 |
| HK-62089 | INLYTA TAB 5MG（Pfizer） | 錠劑 | 請參考原廠仿單 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（VEGFR 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已檢索到 100 筆交互作用，以下為部分重點：
  - 嚴重（Major）：Clarithromycin、Dexamethasone
  - 中度（Moderate）：Aprepitant、Clotrimazole、Miconazole、Naltrexone
  - 輕微（Minor）：Famotidine、Ranitidine、Rabeprazole、Esomeprazole、Lansoprazole、Cimetidine，以及含鋁、鈣、鎂的制酸劑

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Axitinib 已在香港上市，且在腎細胞癌有 Phase 3 證據；針對 TFE3 易位型亞型的證據僅有一個小型、進行中的 Phase 2 試驗，因此建議在有條件的防護下以研究問題的方式推進，而非直接採用。

**若要推進需要：**
- 等待並追蹤 NCT03595124 的結果發表
- 取得香港仿單的警語、禁忌症與核准適應症文字
- 補充詳細的作用機轉資料
- 針對含 Clarithromycin、Dexamethasone 等強 CYP3A4 交互作用藥物的使用者，制定用藥監測計畫
- 由腫瘤專科進行個別病人的風險效益評估

---

**其他預測適應症的簡要補充**

- **集尿管癌（Collecting duct carcinoma）**：L2，有 1 個進行中的 Phase 2 試驗（NCT06211114，n=30）與少數病例報告，建議列為研究問題。
- **兒童腎細胞癌**：L4，僅有一篇回顧與一例個案報告。
- **脂肪肉瘤**：L4，僅有前臨床證據。
- **未分類腎細胞癌**：L4，僅有間接證據。
- **腎細胞癌合併神經母細胞瘤、卵巢黏液樣脂肪肉瘤、血管脂肪瘤、家族性自發性氣胸**：L5，僅有模型預測，建議暫緩（Hold）。
- **腎癌（renal carcinoma）**：屬於已核准的原適應症（L1），非真正的藥物再利用發現。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

