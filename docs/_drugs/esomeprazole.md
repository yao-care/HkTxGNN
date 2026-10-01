---
layout: default
title: Esomeprazole
parent: 中證據等級 (L3-L4)
nav_order: 335
evidence_level: L4
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Esomeprazole：從胃酸相關疾病到十二指腸胃反流

## 一句話總結

Esomeprazole（埃索美拉唑）是質子幫浦抑制劑（PPI），用於抑制胃酸分泌。
TxGNN 模型預測它可能對**十二指腸胃反流 (Duodenogastric Reflux)** 有效，
但目前僅有 **0 個臨床試驗**和 **1 篇文獻（綜述）**，且文獻並未直接針對此適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 十二指腸胃反流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.53% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過 Esomeprazole 屬於 PPI 類別，一般已知它會抑制胃壁細胞的 H+/K+-ATPase，降低胃酸分泌量。

十二指腸胃反流是十二指腸內容物（如膽汁、胰液）逆流入胃。降低胃酸可能減輕逆流物質對黏膜的刺激，緩解相關症狀。

不過，Esomeprazole 並不作用於膽汁或十二指腸逆流本身，所以兩者的關聯是間接的，只能改善症狀。TxGNN 的高分（0.995）目前沒有臨床資料支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | 綜述 PPI 的臨床用途與藥動學。PPI 是消化性潰瘍、幽門螺旋桿菌感染、胃食道逆流、NSAID 相關胃腸損傷及 Zollinger-Ellison 症候群的首選藥物。未直接討論十二指腸胃反流。 |

---

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證（資料中未載明劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64737 | EMANERA GASTRO-RESISTANT CAPSULES 40MG | TRENTON-BOMA LTD |
| HK-61717 | ESOMEPRAZOLE SANDOZ GASTRO-RESISTANT TABLETS 20MG | SANDOZ HONG KONG LIMITED |
| HK-52131 | NEXIUM PDR FOR SOLN FOR INJ/INF 40MG | ASTRAZENECA HONG KONG LIMITED |
| HK-67261 | MAXEUM GASTRO-RESISTANT TABLETS 40MG | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-68382 | PROTAPHIX GASTRO-RESISTANT TABLETS 40MG | SINO PACIFIC PHARMA COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數和一篇不直接相關的綜述支持，沒有任何臨床試驗，證據停留在 L4。
- 機轉上只能間接緩解症狀，無法處理逆流的成因。

**若要推進需要：**
- 取得針對十二指腸胃反流的臨床試驗或觀察性研究，確認 PPI 對症狀或黏膜病變的實際效果。
- 補齊 MOA 與香港衛生署仿單的警語與禁忌資料，這是進入安全性篩選的前提。
- 補上原適應症與核准適應症的資料，才能判斷是真正的新用途還是既有適應症。

**補充觀察：**
同一份資料中，排名第 3 的預測適應症「十二指腸潰瘍」有較完整的證據，包括多個已完成的 Phase 3 試驗和隨機試驗文獻，評為 L1，建議 Proceed with Guardrails。但這很可能是既有的標示適應症，屬於標示確認而非真正的老藥新用。另有數個 Phase 3 試驗標題被截斷，Esomeprazole 是受試藥還是對照藥仍需回原始紀錄查證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

