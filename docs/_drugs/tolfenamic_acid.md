---
layout: default
title: Tolfenamic Acid
parent: 僅模型預測 (L5)
nav_order: 872
evidence_level: L5
indication_count: 5
---

# Tolfenamic Acid
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

# Tolfenamic Acid：從非類固醇消炎止痛藥到頭痛疾患

## 一句話總結

Tolfenamic Acid（托芬那酸）是一種 NSAID，會抑制環氧化酶（COX）並減少前列腺素合成。
TxGNN 模型預測它可能對**頭痛疾患 (Headache Disorder)** 有效，目前有 **0 個臨床試驗登記**，但有 **19 篇文獻**支持，其中包含多項偏頭痛的雙盲隨機試驗。
此預測較可能是既有適應症缺漏，而非真正的老藥新用：該藥在多個國家已用於偏頭痛，來源資料的原適應症欄位則是空白。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症 |
| 預測新適應症 | 頭痛疾患 (Headache Disorder) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L1（依據多項已發表的雙盲隨機對照試驗，非已登記的 Phase 3 試驗） |
| 香港上市 | ✓ 已上市（唯一許可證為獸醫用產品） |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 缺乏詳細的作用機轉資料。不過文獻顯示，Tolfenamic Acid 是強效的前列腺素合成抑制劑，並被報導會影響白三烯（leukotriene）路徑（PMID 7816789）。前列腺素會使痛覺受器敏感化、引起血管擴張與水腫，也參與血小板聚集和血清素釋放。這些都與偏頭痛的病理生理有關，不過前列腺素在偏頭痛中的角色目前仍屬假說。

在機轉上，COX 抑制與頭痛的連結是直接的。臨床上，偏頭痛的急性發作治療和預防性治療都有雙盲試驗，對照藥包括 paracetamol、ergotamine、propranolol、pizotifen 與 sumatriptan。

需要注意的是，原適應症與原機轉欄位在來源資料中皆為空白。該藥在多國已有偏頭痛適應症，因此這項預測較像補回遺漏的標示內容，而不是全新的用途。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | 雙盲交叉試驗，比較 tolfenamic acid（200/400 mg）與 paracetamol（500/1000 mg）用於無預兆偏頭痛（摘要未呈現結果） |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | 31 位患者，預防性治療；tolfenamic acid 與 propranolol 皆較安慰劑顯著減少發作次數、總發作時間與額外用藥 |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT | Acta Neurol Scand | 76 位患者，隨機雙盲交叉，預防性治療 tolfenamic acid vs propranolol（摘要未呈現完整結果） |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT | Medicina (Kaunas) | 192 位患者，隨機雙盲平行組，預防偏頭痛 tolfenamic acid 300 mg vs pizotifen（摘要未呈現結果） |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT | Headache | 141 位患者，急性治療；快速釋放型 tolfenamic acid 的首次發作中 77% 頭痛降為輕度或無痛，標題指出療效與 sumatriptan 相當 |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT | Lancet | 雙盲交叉；與 ergotamine 同樣能縮短發作時間、減輕強度，但噁心較少 |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | RCT | Acta Neurol Scand | 雙盲交叉；預防性治療在發作次數、總時間、嚴重度與嘔吐次數上均優於安慰劑 |
| [6984358](https://pubmed.ncbi.nlm.nih.gov/6984358/) | 1982 | 臨床研究 | Cephalalgia | 10 位患者共 60 次發作；測試 tolfenamic acid 併用咖啡因、metoclopramide 或 pyridoxine，標題指出與咖啡因併用有助益 |
| [10234467](https://pubmed.ncbi.nlm.nih.gov/10234467/) | 1999 | 回溯性研究 | Cephalalgia | 50 位患者；與 sumatriptan 併用可降低偏頭痛復發 |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacol Toxicol | 回顧 tolfenamic acid 用於偏頭痛急性與預防性治療，並討論前列腺素的角色 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50767 | TOLFEDINE TAB 20MG (VET)（廠商：ALFAMEDIC LIMITED） | 未載明 | 未載明 |

此許可證品名標示為 **VET（獸醫用）**，不是人用藥品。香港目前沒有可確認的人用 Tolfenamic Acid 許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 偏頭痛已有多項雙盲隨機對照試驗，涵蓋急性與預防性治療，機轉也直接相關，所以證據等級為 L1。
- 這些試驗多為 1980–1990 年代的小型研究，且沒有臨床試驗登記。香港唯一的許可證是獸醫用，安全性仿單資料也缺漏，因此需設下防護條件。

**其他預測適應症：**
- 類風濕性關節炎同樣有 RCT 與機轉研究支持（L1，Proceed with Guardrails），但僅為症狀緩解，不具疾病修飾作用。
- 肌腱炎、三叉自主神經性頭痛、特發性肉芽腫性肌炎僅有模型預測、無實際研究（L5，Hold）。偏頭痛的證據不應外推到三叉自主神經性頭痛。

**若要推進需要：**
- 取得香港衛生署的人用產品仿單，補齊警語與禁忌症（此為阻擋性資料缺口，未補齊前無法進入安全性篩選）。
- 確認香港是否有人用 Tolfenamic Acid 產品，以及是否核准偏頭痛適應症。
- 補查 DrugBank 的作用機轉資料。
- 評估是否有近年的對照 triptan 或現行標準治療的試驗。
- 建立 NSAID 類別的安全性監測計畫（腸胃道、腎功能、心血管風險）。

本報告結果僅供研究參考，不構成醫療建議，老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

