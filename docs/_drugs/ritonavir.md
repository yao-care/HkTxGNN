---
layout: default
title: Ritonavir
parent: 中證據等級 (L3-L4)
nav_order: 765
evidence_level: L4
indication_count: 3
---

# Ritonavir
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

# Ritonavir：從 HIV 抗病毒治療到貓後天免疫缺乏症候群

## 一句話總結

Ritonavir 是 HIV 蛋白酶抑制劑，臨床上也常作為藥物動力學增強劑（抑制 CYP3A4）。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效。
目前只有 **1 個間接相關的臨床試驗**，且**無直接文獻**支持。這是獸醫疾病，並非人類老藥新用標的。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。已知 Ritonavir 抑制 HIV-1 蛋白酶，也是強效 CYP3A4 抑制劑。
貓免疫缺乏症候群由貓免疫缺乏病毒 (FIV) 引起，FIV 與 HIV 同屬慢病毒 (lentivirus)。
TxGNN 的高分很可能來自知識圖譜中共通的慢病毒生物學，以及 HIV 相關的既有註記。

不過，目前資料中沒有 FIV 蛋白酶對 Ritonavir 敏感性的證據。
與此預測並列的第二名是猴免疫缺乏病毒 (SIV) 感染，分數相同（99.92%）。
SIV 的體外研究顯示 Ritonavir 對 SIVmac239 有抑制作用（EC50 約 13 nM，HIV-1 約 25 nM），支持蛋白酶在慢病毒間的保守性。
但這屬於間接的前臨床證據，不是針對貓的療效資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | 完成 | 145 | 比較 Ritonavir 增強型 Darunavir 加 Lamivudine，與 Darunavir 加 Tenofovir/Emtricitabine（或 Lamivudine）用於未治療過的 HIV-1 感染者 |

此試驗是人類 HIV-1 研究，Ritonavir 僅作增強劑，與貓的疾病無直接關聯，不提供直接療效證據。

## 文獻證據

目前無相關文獻。

補充：同分的 SIV 預測有幾篇前臨床研究，可作為間接參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | 體外研究 | Antimicrob Agents Chemother | Ritonavir 抑制 SIVmac239 的 EC50 約 13 nM，與對 HIV-1 的活性相近 |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | 動物研究 | J Virol Methods | 口服含 Lopinavir/Ritonavir 的 HAART 用於 SHIV 感染獼猴，觀察 CD8 亞群變化 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68558 | RITONAVIR TABLETS USP 100MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-61528 | NORVIR TABLET 100MG | ABBVIE LIMITED |
| HK-68129 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG | CHEMILL PHARMA LIMITED |
| HK-65831 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-67683 | PAXLOVID TABLETS | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病是貓的獸醫疾病，不是人類適應症。唯一的臨床試驗是人類 HIV-1 的已核准用途，不能支持此預測。
- 同分的 SIV 預測只有間接的前臨床證據，沒有 Ritonavir 單獨療效的資料。

**若要推進需要：**
- 確認推進方向是否屬於獸醫用藥開發；若只針對人類老藥新用，建議不列為候選。
- 取得 Ritonavir 對 FIV 蛋白酶的體外敏感性與動物療效資料。
- 取得 DrugBank 的作用機轉資料，並下載香港衛生署仿單，補齊警語與禁忌症。

第三名預測（伴有共濟失調步態、無語言與皮質白質減少的神經發展障礙）沒有任何試驗或文獻，也找不到機轉連結，應視為模型假象，不建議投入資源。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

