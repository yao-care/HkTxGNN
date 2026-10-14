---
layout: default
title: Ropinirole
parent: 僅模型預測 (L5)
nav_order: 786
evidence_level: L5
indication_count: 5
---

# Ropinirole
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

# Ropinirole：從不寧腿症候群與帕金森氏症到注意力不足過動症

## 一句話總結

Ropinirole 是 D2/D3 多巴胺受體促效劑，原本用於不寧腿症候群（RLS）與帕金森氏症。
TxGNN 模型預測它可能對**注意力不足過動症 (ADHD)** 有效，
目前**沒有臨床試驗登記**，但有 **8 篇文獻**，其中包含 1 篇 2026 年的疑似隨機對照試驗（需全文確認）與 1 篇兒童病例報告。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 不寧腿症候群、帕金森氏症（香港許可證未列出核准適應症文字，此為知識圖譜所列） |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold（列為研究性問題，待確認關鍵試驗） |

---

## 為什麼這個預測合理？

Ropinirole 是 D2/D3 多巴胺促效劑。ADHD 的病理與多巴胺功能失調有關，而 ADHD 與不寧腿症候群（RLS，ropinirole 的既有適應症）常同時出現。文獻推測兩者可能共享多巴胺與鐵代謝相關路徑，因此治療 RLS 的多巴胺藥物，理論上可能改善 ADHD 相關症狀。

直接證據有限：一篇兒童病例報告（PMID 15866437）顯示，一名同時有 ADHD 與 RLS 的 6 歲男童，在使用 ropinirole 後，ADHD 症狀與睡眠問題均有改善。另有一篇 2026 年研究（PMID 42640474）探討 ropinirole 作為 methylphenidate 輔助療法，其設計與結果目前僅憑標題與摘要片段，無法確認。RLS 與 ADHD 的回顧文章，以及 A11 病灶小鼠 RLS 動物模型，則提供間接支持。

需注意，0.9999 的預測分數是模型輸出，並非臨床證據。目前缺乏詳細的作用機轉資料，上述機轉連結來自 D2/D3 促效作用的一般推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [42640474](https://pubmed.ncbi.nlm.nih.gov/42640474/) | 2026 | 疑似 RCT（需全文確認） | Eur Child Adolesc Psychiatry | 66 名 6–17 歲 ADHD 門診病人，為期 8 週，比較 methylphenidate 加 ropinirole 與加安慰劑的療效與安全性；結果待確認 |
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Review | Sleep | 回顧 RLS 與 ADHD 的關聯、可能機轉，以及兩者共病時共用藥物治療的可能性 |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review（RLS，間接） | Rev Neurol | RLS 的臨床特徵與治療回顧 |
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | 病例報告 | Pediatr Neurol | 6 歲 ADHD 合併 RLS 男童，methylphenidate 療效有限，改用 ropinirole 後 ADHD 症狀與睡眠均明顯改善 |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | 臨床研究（間接） | Clin Neuropharmacol | 比較 piribedil 與 pramipexole、ropinirole 對帕金森氏症嗜睡病人警覺度的影響 |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | 前臨床 | Pharmacol Res | 多巴胺 D4 受體變異與 α2A 腎上腺素受體異聚體，與 ADHD 及衝動控制障礙相關 |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | 動物模型（RLS，間接） | J Neuropathol Exp Neurol | A11 病灶合併缺鐵的小鼠活動量增加，可作為 RLS 動物模型 |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | 安全性報告 | Cornea | 3 名使用多巴胺類藥物的病人出現角膜水腫，停藥後緩解 |

**證據等級說明：** 目前無已完成並確認的 RCT，PMID 42640474 的設計與結果尚待全文確認，故保守評為 L4（僅有病例報告、回顧與前臨床／機轉研究）。若該研究經確認為隨機對照試驗，等級可重新評估。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57966 | REQUIP PD TAB 2MG（GlaxoSmithKline） | — | — |
| HK-57965 | REQUIP PD TAB 4MG（GlaxoSmithKline） | — | — |
| HK-57964 | REQUIP PD TAB 8MG（GlaxoSmithKline） | — | — |
| HK-66674 | EVECET PROLONGED-RELEASE TABLETS 8MG（I & C） | 緩釋錠 | — |
| HK-66478 | ROLPRYNA SR PROLONGED-RELEASE TABLETS 4MG（Sino Pacific） | 緩釋錠 | — |

共 9 張有效單方許可證，此處僅列出 5 張。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：多系統萎縮、姿勢性心搏過速症候群、姿勢性低血壓、藥物誘發的異動症、肝衰竭、精神病性疾患、思覺失調樣疾患、精神疾患、情感性思覺失調症、低血壓疾患。此為知識圖譜的藥物─疾病關聯，並非仿單原文。
- **藥物交互作用**：共查得 100 筆。中度交互作用包括 Morphine、Cimetidine、Dronabinol、Obeticholic acid、Metoclopramide、Nabilone、Opium 等；另有多筆等級未明。
- **相關文獻提示的風險**：多巴胺促效劑可能增加賭博障礙風險（PMID 34061895）；與多巴胺類藥物相關的角膜水腫案例（PMID 30950895）。兒童族群使用的安全性資料有限。

香港仿單的警語與禁忌資料尚未取得，其他安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有一例兒童病例報告與一篇設計待確認的 2026 年研究，沒有臨床試驗登記，且機轉資料缺乏；預測分數不能取代臨床證據。
- 香港仿單的警語與禁忌資料缺口屬於阻擋性缺口，須補齊才能進入安全性篩選。

**若要推進需要：**
- 取得 PMID 42640474 全文，確認設計、主要療效指標、結果與不良事件，若為有效的 RCT 則重新評估證據等級與決策
- 補齊 ropinirole 的作用機轉資料（DrugBank）
- 下載並解析香港衛生署仿單，完成警語與禁忌症整理
- 評估兒童 ADHD 族群的安全性，包括衝動控制障礙、嗜睡、精神症狀與眼部不良反應
- 檢視是否有登記中或進行中的 ADHD 臨床試驗

---

*其他預測適應症（先天性顏面指趾生殖症候群、伴小腦發育不全與關節攣縮的周邊裂多小腦回症、視網膜失養症、思覺失調症）目前僅有模型預測，或僅有前臨床與間接文獻，皆建議 Hold。其中思覺失調症因完全促效劑可能加重陽性症狀，風險尤須注意。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

