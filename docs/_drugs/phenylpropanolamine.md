---
layout: default
title: Phenylpropanolamine
parent: 中證據等級 (L3-L4)
nav_order: 679
evidence_level: L3
indication_count: 5
---

# Phenylpropanolamine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Phenylpropanolamine：從原適應症未登載到鼻腔疾病

## 一句話總結

Phenylpropanolamine (PPA) 是間接作用的擬交感神經藥物，常見於複方感冒藥，但本次資料中的原適應症欄位是空的。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效。
目前有 **1 個臨床試驗**（但試驗藥物是 guaifenesin，不是 PPA）和 **3 篇文獻**，其中只有 1 篇是人體研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（香港許可證未登載適應症文字） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依現有評估，PPA 是具 α-腎上腺素受體活性的間接擬交感神經藥物。它會使鼻黏膜血管收縮、降低鼻腔阻力，因此機轉上確實可用於緩解鼻塞。

不過這個預測**不算真正的老藥新用**。「鼻腔疾病」與 PPA 歷來作為口服鼻塞緩解劑的用途非常接近，更像是把既有用途重新歸類。原適應症與 MOA 欄位都是空的，在把它當成新適應症之前，需要先補齊這兩項資料。

TxGNN 的其他預測（急性喉咽炎、酒糟性結膜炎、咽部白喉、頸椎椎間盤退化）都只有模型分數，沒有任何試驗或文獻支持，且多半找不到合理機轉，應視為知識圖譜的假訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | 完成 | 30 | 口服 guaifenesin 用於兒童慢性鼻炎的隨機、安慰劑對照先導試驗。**試驗藥物不是 PPA**，只與疾病領域相符，不能作為 PPA 的直接證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | 人體臨床比較研究 | American Journal of Rhinology | 以鼻腔聲波測量法比較 PPA 與 d-pseudoephedrine 的口服與局部鼻塞緩解效果 |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | 前臨床動物實驗 | American Journal of Rhinology | 貓鼻塞模型，以壓力與聲波鼻腔測量法評估鼻腔阻力與幾何變化。為方法學研究，非 PPA 專屬 |
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | 前臨床動物實驗 | American Journal of Rhinology | 組織胺 H1/H3 受體合併阻斷可在貓鼻塞模型產生減充血效果，不涉及 PPA 的直接證據 |

## 香港上市資訊

香港共有 20 張相關許可證，以下列出 5 張。各證的劑型與核准適應症欄位皆無資料。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-46548 | PROPALIN SYRUP 40MG/ML (VET)（獸用） | ALFAMEDIC LIMITED |
| HK-32127 | SYNCOLDTAB-M TAB (YELLOW) | SYNCO (H.K.) LIMITED |
| HK-22813 | D.P.P SYRUP | MARCHING PHARMACEUTICAL LIMITED |
| HK-09487 | DIMAXIN SYRUP | EUROPHARM LAB CO LTD |
| HK-08611 | JEM C P P TAB | JEAN-MARIE PHARMACAL CO LTD |

## 安全性考量

目前沒有仿單層級的警語、禁忌症與藥物交互作用資料（DDI 查詢無結果）。安全性資訊請參考原廠仿單。

另外，PPA 已被報告與出血性中風相關，並在多個地區被撤市或限制使用。任何後續研究都必須先完成安全性審查。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的適應症與 PPA 歷來的鼻塞緩解用途幾乎重疊，不是真正的新用途。
- 證據只有 1 篇人體比較研究，唯一的臨床試驗是 guaifenesin，與 PPA 無關。
- 出血性中風的安全疑慮是主要限制。

**若要推進需要：**
- 補齊 DrugBank 的原適應症與作用機轉資料。
- 取得香港衛生署的仿單，確認警語與禁忌症。
- 精讀 PMID 11345158 全文，確認 PPA 相對 pseudoephedrine 的效果與安全性。
- 評估是否有比 PPA 更安全的替代藥（如 pseudoephedrine）。
- 完成出血性中風風險的安全性審查，再決定是否進入下一階段。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

