---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
monitor_inn: "BUDESONIDE"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
last_modified_at: 2026-10-28
description: "Budesonide：預測新適應症為異位性皮膚炎 (atopic eczema)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Budesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Budesonide：糖皮質激素 → 異位性皮膚炎 (atopic eczema)
{: .text-alpha }

## 一句話總結

Budesonide 是一種局部作用的糖皮質激素（皮質類固醇），具有廣泛的抗發炎與免疫抑制作用。
TxGNN 模型預測它可能對**異位性皮膚炎 (atopic eczema)** 有效，
但目前**沒有登記的臨床試驗**，文獻多為間接證據，僅有 1 篇與皮膚劑型直接相關的前臨床配方研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 異位性皮膚炎 (atopic eczema) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，budesonide 屬於糖皮質激素類藥物，一般認為可抑制 Th2 細胞激素、嗜酸性白血球活化與 NF-κB 訊號，這些路徑與異位性皮膚炎的皮膚發炎有關，因此機轉上具合理性。

需要注意的是，局部皮質類固醇本來就是異位性皮膚炎的標準治療之一，因此模型的高分較可能反映整個藥物類別的效應，而非 budesonide 特有的訊號。

此外，所取得的文獻多為間接證據，例如嗜酸性食道炎的綜述、鼻用類固醇的腎上腺抑制、類固醇過敏的病例報告等。唯一直接相關的是一篇將 budesonide 製成奈米粒子水凝膠、用於局部治療異位性皮膚炎的前臨床配方研究，並不屬於人體療效研究。依規則，沒有直接研究此疾病療效的臨床試驗或文獻，證據等級定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為與此預測最相關的文獻（多為間接證據）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | 前臨床配方研究 | Gels | 將 budesonide 製成 pH 敏感奈米粒子水凝膠，用於兒童異位性皮膚炎局部治療的遞送平台 |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | 開放式縱向試驗 | Pediatric Dermatology | 以膝長測量法評估外用 budesonide 對 14 位異位性皮膚炎兒童短期生長的影響（安全性導向） |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | 細胞研究 | Int Immunopharmacol | Budesonide 會影響正常人類角質細胞的免疫功能，tacrolimus 則否 |
| [35056927](https://pubmed.ncbi.nlm.nih.gov/35056927/) | 2021 | 配方研究 | Pharmaceutics | 以環糊精與泊洛沙姆水凝膠改善 budesonide 的皮膚滯留 |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | 斑貼試驗研究 | Contact Dermatitis | 義大利斑貼試驗顯示 budesonide 過敏有下降趨勢 |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | 病例報告 | Cureus | 一名有異位性皮膚炎病史的患者出現類固醇引起的血管性水腫與蕁麻疹 |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | 氣喘患者的皮質類固醇過敏發生情形 |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | 鼻用皮質類固醇與腎上腺抑制 |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Review | J Allergy Clin Immunol | 嗜酸性食道炎的新興治療（非皮膚疾病） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68212 | NEFECON MODIFIED-RELEASE CAPSULES 4MG | — | — |
| HK-60236 | BIOSONIDE NASAL SPRAY 100MCG/DOSE | — | — |
| HK-64964 | CORTIMENT PROLONGED RELEASE TABLETS 9 MG | — | — |
| HK-51729 | BUDESONIDE PH&T 50 NASAL SPRAY 50MCG/DOSE | — | — |
| HK-64327 | BUDENA NASAL SPRAY 64 MCG/SPRAY | — | — |

本地資料中共有 20 張單一成分許可證，皆為有效狀態，以上僅列出其中 5 張，清單可能不完整。

## 安全性考量

- **藥物交互作用**：已查詢到多筆交互作用，其中較需留意的為**重大 (Major)** 等級，包括 adalimumab 與 fosamprenavir。另有多項中度交互作用，例如 zidovudine、isotretinoin、acebutolol、ketorolac、nifedipine、ibuprofen、ethinylestradiol、fluvoxamine 等；formoterol 與 salbutamol 為輕微等級。
- **皮質類固醇相關風險（來自文獻）**：包括接觸性過敏與即時型過敏反應、鼻用類固醇可能造成的腎上腺抑制，以及外用類固醇對兒童生長的潛在影響。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有登記的臨床試驗，也沒有直接評估 budesonide 治療異位性皮膚炎療效的人體研究，證據僅止於模型預測與前臨床配方研究。
- 外用皮質類固醇本就是此疾病的標準治療，模型高分較可能反映類別效應，缺乏 budesonide 的特異性訊號。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）
- 評估外用 budesonide 與現有外用類固醇相比的優勢（療效、皮膚滯留、全身暴露）
- 設計針對異位性皮膚炎的臨床試驗，特別是兒童族群，並納入生長與腎上腺抑制監測
- 確認香港是否有適用於皮膚的劑型與核准適應症
- 取得原廠仿單中的警語與禁忌症資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

