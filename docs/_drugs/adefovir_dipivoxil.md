---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil：從慢性 B 型肝炎到慢性 C 型肝炎

## 一句話總結

Adefovir dipivoxil 是一種核苷酸類似物抗病毒藥，原本用於治療慢性 B 型肝炎。
TxGNN 模型預測它可能對**慢性 C 型肝炎病毒感染 (Chronic Hepatitis C Virus Infection)** 有效。
但這項預測**目前沒有直接的臨床試驗**，現有 10 篇文獻多為 B 型肝炎的綜述，缺乏針對 C 型肝炎的療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎病毒感染 |
| 預測新適應症 | 慢性 C 型肝炎病毒感染 (Chronic Hepatitis C Virus Infection) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（僅有間接的文獻與機轉層面資料） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記錄。根據已知藥理，adefovir dipivoxil 是 adefovir 的前驅藥，活性代謝物（二磷酸型）可與 dATP 競爭，抑制 HBV DNA 聚合酶／反轉錄酶並造成鏈終止。

C 型肝炎病毒是 RNA 病毒，靠 NS5B RNA 依賴性 RNA 聚合酶複製，與 adefovir 的作用靶點不同。因此**機轉上沒有明確的支持依據**。

模型分數偏高，較可能是因為在知識圖譜中，C 型肝炎與 B 型肝炎距離相近，兩者都是病毒性肝炎，常出現在同一批治療文獻中。這並不代表 adefovir 對 HCV 本身有活性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻皆未提供 adefovir 對 C 型肝炎療效的直接證據。多數是 B 型肝炎或病毒性肝炎治療的綜述。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Pat Anti-infect Drug Discov | 回顧慢性 B 型肝炎的 5 種核准藥物（含 adefovir）與聚乙二醇干擾素的角色 |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | 慢性病毒性肝炎治療；adefovir 與 lamivudine 用於抑制 HBV 複製 |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Review | Expert Rev Anti Infect Ther | B 型肝炎的聚乙二醇干擾素治療，與 adefovir 單藥療法比較討論 |
| [15918324](https://pubmed.ncbi.nlm.nih.gov/15918324/) | 2004 | Review | Lijecnicki Vjesnik | 病毒性肝炎的治療與預防概述 |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Medicinal Chemistry | 新藥 bicyclol 用於 B、C 型肝炎，與 adefovir 無直接關係 |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Digestive Diseases | 病毒性肝炎的現有與新興療法；C 型肝炎使用干擾素加 ribavirin，adefovir 僅用於 B 型肝炎 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B、C 型肝炎抗病毒藥對腎功能的影響 |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orv Hetil | 匈牙利 B、C、D 型肝炎診療共識指引 |
| [24797262](https://pubmed.ncbi.nlm.nih.gov/24797262/) | 2014 | Cohort | Viral Immunol | 停用核苷（酸）類似物後，HBeAg 血清轉換相關的細胞激素特徵（B 型肝炎） |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Cohort | Cancer Manag Res | 核苷（酸）類似物抗病毒治療對 HBV 相關小肝癌存活的影響 |

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63344 | HEPTOVANCE TABLET 10MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-64175 | APO-ADEFOVIR TABLETS 10MG | HIND WING CO LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、膿尿（pyoureter）、肥胖症、單基因肥胖、脂肪肝、非酒精性脂肪肝炎、乳酸中毒
- **藥物交互作用**：共查得 25 筆，皆未分級。例如 pantoprazole、omeprazole、morphine、warfarin、heparin、ibuprofen、kanamycin、prednisolone、potassium chloride 等
- **其他已知風險**：現有文獻顯示，長期使用 adefovir 有劑量相關的腎毒性風險（PMID 27977591 的統合分析），用藥期間需監測腎功能

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- HCV 為 RNA 病毒，與 adefovir 的 HBV DNA 聚合酶靶點不同，機轉上缺乏依據。
- 沒有針對 HCV 的臨床試驗，文獻也只是 B 型肝炎的綜述。高預測分數很可能只是反映知識圖譜中與 B 型肝炎的鄰近關係。
- 目前 C 型肝炎已有直接作用抗病毒藥（DAA）等有效療法，adefovir 的腎毒性風險也使其不具優勢。

**若要推進需要：**
- 體外（HCV replicon）活性試驗，確認是否有任何抗 HCV 效果
- 取得詳細的作用機轉資料與香港仿單的警語、禁忌資料
- 在上述證據出現前，不建議投入臨床開發

**補充：**同一份預測清單中，**HIV 感染**一項已有多個已完成的 Phase 2/3 臨床試驗與隨機對照研究，證據較為充分（但因劑量相關腎毒性及 tenofovir 取代，開發受限）。若要尋找 adefovir 的新適應症，建議優先評估該方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

