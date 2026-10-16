---
layout: default
title: Fludrocortisone
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Fludrocortisone：預測新適應症為原發性皮膚 T 細胞淋巴瘤 (primary cutaneous T-cell lymphoma)（證據等級 L5）。原適應症：資料未提供"
---

# Fludrocortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fludrocortisone：從腎上腺皮質功能不全相關用途到原發性皮膚 T 細胞淋巴瘤（預測）

> 註：本資料未提供香港許可證上的原適應症文字，標題中的「原適應症」僅依藥理類別（礦物皮質素）概述，不代表核准適應症。

## 一句話總結

Fludrocortisone 是一種合成的礦物皮質素（兼具部分糖皮質素活性）。
TxGNN 模型預測它可能對**原發性皮膚 T 細胞淋巴瘤 (primary cutaneous T-cell lymphoma)** 有效，但目前**沒有任何臨床試驗或文獻**支持此預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明適應症文字） |
| 預測新適應症 | 原發性皮膚 T 細胞淋巴瘤 (primary cutaneous T-cell lymphoma) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fludrocortisone 屬於礦物皮質素，並帶有部分糖皮質素活性。糖皮質素具有溶解淋巴細胞的效果，這可能是模型將其與淋巴瘤連結的原因。

不過，fludrocortisone 臨床上並不用於此目的。現有資料中找不到支持的機轉連結。0.996 的高分很可能來自知識圖譜中皮質類固醇類別的關聯，屬於計算預測，不能視為療效證據。

**其他預測適應症（同樣僅為模型預測）：**

| 預測適應症 | TxGNN 分數 | 證據等級 | 評估 |
|-----------|-----------|---------|------|
| 囊性畸胎瘤 (cystic teratoma) | 99.20% | L5 | 無機轉依據，可能為知識圖譜假象 |
| 脊髓皮樣囊腫 (spinal cord dermoid cyst) | 99.18% | L5 | 先天性病灶，以手術治療，無藥理依據 |
| 卵巢皮樣囊腫 (dermoid cyst of ovary) | 99.18% | L5 | 良性生殖細胞腫瘤，以手術處理，無佐證 |
| 眼眶附屬器疾病 | 99.17% | L5 | 分類過於籠統，無法評估 |
| 眼疾病 (eye disease) | 99.14% | L4 | 有間接證據（見下），需先界定具體適應症 |
| 眼眶區域疾病 | 99.13% | L5 | 分類籠統，無佐證 |
| 外生骨疣 (exostosis) | 99.08% | L5 | 無機轉依據；長期皮質類固醇反而與骨質流失相關 |

其中「眼疾病」是唯一有間接證據的預測：
- **青光眼合併低血壓**：fludrocortisone 曾用於原發性開角型青光眼患者的全身性低血壓（PMID 11008895）。其思路是低血壓可能降低視神經灌流，屬血管性而非直接眼部機轉。
- **視網膜退化**：前臨床研究顯示 fludrocortisone 具抗發炎與神經保護特性（PMID 34509498），且有一項針對地圖狀萎縮的 Phase 1B 安全性研究（PMID 36161841）。

## 臨床試驗證據

目前無相關臨床試驗登記（針對首位預測適應症：原發性皮膚 T 細胞淋巴瘤）。

## 文獻證據

針對首位預測適應症，目前無相關文獻。

以下為「眼疾病」預測的相關文獻（精選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | 臨床研究 | International Ophthalmology | 評估 fludrocortisone 對青光眼合併全身性低血壓患者的血行動力學影響 |
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B | BMJ Open Ophthalmology | 玻璃體內注射 fludrocortisone 用於地圖狀萎縮的安全性與耐受性 |
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | 前臨床 | Experimental Eye Research | 對 Müller 細胞介導的發炎細胞激素表現具抗發炎與神經保護作用 |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Review | Survey of Ophthalmology | 討論青光眼降眼壓以外的療法，包含鹽與 fludrocortisone 避免血壓下降 |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Review | Klin Monatsbl Augenheilkd | 青光眼非降眼壓療法的價值，提及 fludrocortisone |
| [15934882](https://pubmed.ncbi.nlm.nih.gov/15934882/) | 2005 | Review | Expert Opin Pharmacother | 家族性自主神經失調症的藥物治療回顧 |

其餘檢索到的文獻多為自主神經失調、帕金森氏症非運動症狀、自體免疫多腺體症候群或休格倫氏症腎小管酸中毒的報告，僅在其他情境提及 fludrocortisone，與眼疾病的關聯有限。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-00036 | FLORINEF TAB 0.1MG | 未載明 | 未載明 |
| HK-47276 | PAROTICIN OTIC DROPS | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分例子：
  - **嚴重 (Major)**：Bupropion
  - **中度 (Moderate)**：
    - 降血糖藥：Acarbose、Albiglutide、Alogliptin、Pioglitazone、Canagliflozin、Dapagliflozin、Empagliflozin、Linagliptin、Chlorpropamide、Dulaglutide
    - 其他：Amphotericin B、Aprepitant、Acetylsalicylic acid（阿斯匹靈）、Bisacodyl、Picosulfuric acid、Clarithromycin、Oxandrolone、Oxymetholone

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（皮膚 T 細胞淋巴瘤）僅有模型分數，無試驗、無文獻，也找不到合理機轉，不建議推進。
- 其餘預測中，只有「眼疾病」有間接線索，但分類太籠統，仍屬研究假設階段。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症，以完成安全性篩選
- 補齊 fludrocortisone 的作用機轉資料
- 若要探索眼科方向，須先界定具體適應症（例如青光眼合併低血壓，或地圖狀萎縮），再針對該適應症蒐集證據
- 確認給藥途徑（例如玻璃體內注射與現有口服劑型不同）的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

