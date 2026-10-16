---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Darolutamide：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：香港許可證未登載適應症文字"
monitor_inn: "Darolutamide"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "cytomegalovirus infection", "thrombotic disease", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Darolutamide
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

# Darolutamide：從前列腺癌相關治療到多發性內分泌腫瘤（預測）

## 一句話總結

Darolutamide 是一種非類固醇雄激素受體拮抗劑，已在香港取得上市許可。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，但目前僅有 **2 個相關性低的臨床試驗**，且**沒有直接文獻**支持，整體證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未登載適應症文字 |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L4（僅有間接的臨床試驗，無直接研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

> 說明：TxGNN 排名第 1 的預測為家族性高膽固醇血症（分數 99.11%），但該預測沒有任何試驗或文獻支持，機轉上也無合理關聯。本報告以有間接臨床試驗線索的「多發性內分泌腫瘤」為主要分析對象，其餘預測列於「其他預測適應症」。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Darolutamide 為非類固醇雄激素受體拮抗劑，透過阻斷雄激素受體訊號發揮作用。

多發性內分泌腫瘤（MEN1/MEN2）是由特定基因變異（如 MEN1、RET）引起的遺傳性腫瘤症候群，目前沒有證據顯示其腫瘤生長依賴雄激素受體。

TxGNN 的高分預測較可能來自知識圖譜中「腫瘤／內分泌腫瘤」的廣泛註解關聯，而非真正的雄激素受體依賴性。**整體來看，此預測缺乏機轉支持，應視為假說生成而非可行動的結論。**

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07795177](https://clinicaltrials.gov/study/NCT07795177) | Phase 2 | 尚未招募 | 40 | 以空間多組學預測轉移性荷爾蒙敏感性前列腺癌接受雄激素剝奪治療合併新一代內分泌藥物的療效；實為前列腺癌研究，與多發性內分泌腫瘤無直接關聯 |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | 已終止 | 2 | SMMART PRIME 精準腫瘤平台試驗，僅收案 2 人即終止，無可用的療效或安全性訊號 |

兩個試驗的相關性評級均為 C（低）。

---

## 文獻證據

目前無針對多發性內分泌腫瘤的相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66877 | NUBEQA TABLETS 300MG（拜耳） | 未登載 | 未登載 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶／荷爾蒙類藥物（雄激素受體拮抗劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分重點：
  - **嚴重 (Major)**：Dexamethasone、Eluxadoline、Rosuvastatin
  - **中度 (Moderate)**：Clarithromycin、Empagliflozin、Glyburide、Repaglinide、Simvastatin、Sulfasalazine、Cobicistat、Deferasirox、Eltrombopag 等
  - **輕微 (Minor)**：Aprepitant、Cimetidine、Miconazole

其他警語與禁忌症請參考原廠仿單。

---

## 其他預測適應症

以下預測皆僅有模型分數，**無臨床試驗支持**，建議決策均為 Hold：

| 排名 | 預測疾病 | 分數 | 證據等級 | 評估 |
|-----|---------|------|---------|------|
| 1 | 同合子家族性高膽固醇血症 | 99.11% | L5 | 病因為 LDL 受體路徑缺陷，無機轉關聯 |
| 3 | HIV 感染 | 99.04% | L5 | 雄激素受體拮抗無抗病毒作用；且 DDI 負擔高，不利於抗反轉錄病毒治療者 |
| 4 | 猴免疫缺陷病毒感染 | 98.70% | L5 | 可能由 HIV 節點傳遞而來，為動物疾病 |
| 5 | 貓後天免疫缺乏症候群 | 98.70% | L5 | 獸醫疾病，無支持 |
| 6 | 神經發展障礙（伴共濟失調步態、無語言等） | 98.56% | L5 | 罕見遺傳疾病，無關聯 |
| 7 | 巨細胞病毒感染 | 98.33% | L5 | 無已知抗病毒機轉 |
| 8 | 血栓性疾病 | 98.29% | L4 | 僅 1 篇個案報告（前列腺癌之副腫瘤症候群），並非藥物療效研究；血栓關聯較可能屬安全性考量 |
| 9 | 惡性卡他熱 | 98.18% | L5 | 反芻動物疾病，無支持 |
| 10 | 傳染性牛鼻氣管炎 | 98.18% | L5 | 牛疾病，無支持 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症均缺乏機轉依據，且沒有任何已完成的 RCT 或直接文獻支持。唯一的間接臨床試驗實為前列腺癌研究，與多發性內分泌腫瘤無關。
- 高 TxGNN 分數僅代表圖譜預測，不足以支持推進。

**若要推進需要：**
- 補齊作用機轉資料，並釐清雄激素受體訊號是否與預測疾病有生物學關聯
- 取得香港許可證的核准適應症與仿單警語、禁忌症
- 進行針對預測疾病的前臨床或文獻回顧，確認是否存在任何直接證據
- 若考慮用於合併多種用藥的族群，需先建立 DDI 管理方案
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

