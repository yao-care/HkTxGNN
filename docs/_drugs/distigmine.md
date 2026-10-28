---
layout: default
title: Distigmine
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Distigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "fetal akinesia deformation sequence", "congenital myasthenic syndrome with tubular aggregates", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors"]
description: "Distigmine：預測新適應症為Autoimmune disease of peripheral nervous system（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Distigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Distigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## 一句話總結

Distigmine 是長效型膽鹼酯酶抑制劑，原本用於重症肌無力、神經肌肉接合部疾病等。
但目前**沒有臨床試驗與直接文獻**支持，僅有模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Autoimmune disease of peripheral nervous system |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Distigmine 屬於長效膽鹼酯酶抑制劑，已用於重症肌無力。抑制乙醯膽鹼酯酶可提升神經肌肉接合部的乙醯膽鹼濃度，因此機轉上可能對此亞型產生症狀性改善。

需注意，膽鹼酯酶抑制劑只能改善症狀，無法改變胸腺增生本身的病程。

### 其他預測適應症概覽

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 2 | 自體免疫性肢帶型肌無力 | 1.0000 | 與重症肌無力相近，機轉上合理，但無直接證據 |
| 3 | 新生兒重症肌無力 | 1.0000 | 一般臨床會用膽鹼酯酶抑制劑，但 Distigmine 半衰期長、有膽鹼性危象風險，新生兒安全性需審慎評估 |
| 4 | 周邊神經自體免疫疾病 | 1.0000 | 類別過於廣泛；脫髓鞘性神經病變無已知機轉支持 |
| 5 | 受體活性疾病 | 1.0000 | 屬非特異性分類；僅有 1 篇受體結合研究（見下），較適合作為逼尿肌低活性的研究線索 |
| 7 | 非典型溶血性尿毒症候群（B 因子異常） | 0.9996 | 屬補體媒介疾病，Distigmine 無補體作用，不支持 |
| 8 | 胎兒運動不能變形序列 | 0.9994 | 僅有鬆散的概念關聯，且涉及胎兒暴露安全疑慮 |
| 9 | 先天性肌無力症候群（管狀聚集型） | 0.9967 | 同類藥物（如 pyridostigmine）常見有效報告，但反應因基因型而異 |
| 10 | 先天性肌無力（對乙醯膽鹼酯酶抑制劑無效型） | 0.9967 | 依定義對此類藥物無效，部分亞型甚至可能惡化，預測與藥理相左，有安全疑慮 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

與本藥相關、僅有的一篇文獻出現在第 5 順位預測：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20410601](https://pubmed.ncbi.nlm.nih.gov/20410601/) | 2010 | 前臨床受體結合研究 | Biological & Pharmaceutical Bulletin | 以受體結合試驗顯示 Distigmine 可與蕈毒鹼及菸鹼受體結合，對血中乙醯膽鹼酯酶的抑制作用明顯弱於 neostigmine；研究背景為逼尿肌低活性治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-19583 | UBRETID TAB 5MG | （未載明） | （未載明） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

另依評估所得的藥理考量：
- 新生兒及胎兒族群使用的劑量與安全性尚無資料，且 Distigmine 半衰期長、有膽鹼性危象風險。
- 對乙醯膽鹼酯酶抑制劑無效的先天性肌無力亞型（如慢通道症候群、DOK7、COLQ 相關）可能因此類藥物而惡化。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測僅來自模型推論，無臨床試驗與直接文獻支持（L5），且與既有重症肌無力適應症高度重疊，新增價值有限。
- 部分高分預測（如脾功能亢進、非典型溶血性尿毒症候群、對抑制劑無效型先天性肌無力）與藥理不符，應視為模型假象。

**若要推進需要：**
- 補齊 Distigmine 的作用機轉資料與香港仿單的警語、禁忌與核准適應症
- 針對具體亞型（如胸腺增生型、肢帶型、管狀聚集型先天性肌無力）進行文獻回顧或真實世界資料蒐集
- 新生兒與胎兒暴露情境須先完成專門的安全性評估
- 可另將逼尿肌低活性（膀胱）列為獨立研究問題，延伸受體結合研究的線索
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

