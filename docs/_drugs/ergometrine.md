---
layout: default
title: Ergometrine
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ergometrine：預測新適應症為多毛症 (hypertrichosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Ergometrine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "nephrogenic syndrome of inappropriate antidiuresis", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "migraine disorder", "migraine with brainstem aura", "leprosy", "pulmonary hypertension"]
---

# Ergometrine
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

# Ergometrine：從產科用途到毛髮過多症（預測）

## 一句話總結

Ergometrine 是麥角生物鹼類子宮收縮藥，香港目前有一張上市許可證（SYNTOMETRINE INJ），但本報告所編的資料中沒有記載其核准適應症。
TxGNN 模型預測它可能對**多毛症 (hypertrichosis)** 有效，但目前**沒有任何臨床試驗與文獻**支持，也找不到機轉上的關聯。
排名較前的預測中，只有偏頭痛有間接文獻，且其安全疑慮多於療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（許可證的核准適應症欄位為空白） |
| 預測新適應症 | 多毛症 (hypertrichosis) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ergometrine 是麥角生物鹼，主要透過血清素、α-腎上腺素與多巴胺受體作用於子宮平滑肌，產生子宮收縮。

這個機轉與毛囊調控之間找不到任何可辨識的連結。99.96% 的高分來自知識圖譜的推論，沒有任何試驗或文獻佐證，較可能是圖譜相似性造成的假象，而非真實的藥理關聯。

其他高分預測也有類似問題，例如 Ambras 型先天性全身多毛症、腎因性抗利尿不適當症候群、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常、痲瘋病，皆無合理機轉。

唯一在生物學上較說得通的是**偏頭痛**（排名第 7，分數 99.93%）。麥角類藥物如 ergotamine、二氫麥角胺和 methysergide 作用於 5-HT1B/1D 受體，造成顱內血管收縮，這是已確立的偏頭痛機轉。Ergometrine 具有相同的麥角灵骨架和 5-HT 受體活性，但主要作用是子宮收縮，並非已確立的偏頭痛藥物。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（多毛症），目前無相關文獻。

下表為次要預測「偏頭痛」與「肺高壓」的間接文獻，僅供參考，並不支持多毛症：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Methysergide（麥角衍生物）用於偏頭痛預防，屬相關藥物而非 ergometrine 本身 |
| [41844474](https://pubmed.ncbi.nlm.nih.gov/41844474/) | 2026 | Review | Int J Obstet Anesth | 心臟疾病孕婦使用子宮收縮劑的重點回顧，涉及肺高壓族群的使用風險 |
| [22731893](https://pubmed.ncbi.nlm.nih.gov/22731893/) | 2012 | Review | Anaesthesia | 子癇前症對麻醉科的處置重點 |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | 2000 | Case report | Headache | 一名有先兆偏頭痛病人產後發生腦血管病變，提示血管收縮型麥角類藥物的安全疑慮 |
| [20509463](https://pubmed.ncbi.nlm.nih.gov/20509463/) | 2009 | Review | J R Coll Physicians Edinb | 麥角 1900–1940 年的歷史回顧，無療效證據 |
| [3214444](https://pubmed.ncbi.nlm.nih.gov/3214444/) | 1988 | Preclinical (animal) | Arzneimittel-Forschung | Nilvadipine 的心血管動物研究，與 ergometrine 無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-01698 | SYNTOMETRINE INJ | 資料未載明 | 資料未載明（製造商：DCH Auriga (Hong Kong) Limited） |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜，非仿單文字）：高血壓、癲癇、腎臟病、輸尿管積膿、肝病、膽囊疾病、中風、腦血管疾病、缺血性中風易感性、腦梗塞、閉塞性動脈硬化症、HELLP 症候群。
- **藥物交互作用**：共查得 83 筆。主要（Major）等級包括 Isometheptene、Epinephrine、Lorcaserin、Clarithromycin、Ephedrine、Cobicistat。中度（Moderate）等級包括 Doxycycline、Aprepitant、Dexamethasone、Cimetidine、Miconazole 等。評估偏頭痛時，需特別留意 CYP3A4 抑制劑與 triptan 類藥物。
- **其他考量**：Ergometrine 具子宮收縮作用，圍產期以外的孕婦不宜使用。血管收縮作用也可能提高血管痙攣和缺血風險，與肺高壓的文獻警示一致。

仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（多毛症）與其餘多數高分預測皆無試驗、無文獻，也找不到機轉連結，屬圖譜推論的假象。
- 偏頭痛雖有生物學上的合理性，但現有文獻僅為相關藥物的專論與一則顯示安全疑慮的病例報告，且血管收縮與高藥物交互作用負擔使風險偏高。肺高壓則屬禁忌訊號，並非再利用機會。

**若要推進需要：**
- 取得香港衛生署的仿單，確認原適應症、警語與禁忌。
- 補充 DrugBank 的作用機轉資料。
- 若要探索偏頭痛，需先做針對 ergometrine 本身的文獻回顧，並與已確立的麥角類、triptan 類藥物比較，再評估血管缺血風險與交互作用管理計畫。
- 多毛症及其他無機轉依據的預測，除非有新的生物學證據，否則不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

