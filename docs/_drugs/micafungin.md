---
layout: default
title: Micafungin
parent: 中證據等級 (L3-L4)
nav_order: 495
evidence_level: L3
indication_count: 1
---

# Micafungin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# MICAFUNGIN：從抗黴菌感染到泌尿道感染

## 一句話總結

MICAFUNGIN（DB01141）是 echinocandin 類全身性抗黴菌藥物，目前尚未在台灣上市（無核准適應症紀錄）。
TxGNN 模型預測它可能對**泌尿道感染 (Urinary Tract Infection)** 中的念珠菌尿路感染有效，
目前無臨床試驗登記，但有 **13 篇文獻**（多為病例報告與回溯性研究）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（台灣未上市，無核准適應症紀錄） |
| 預測新適應症 | 泌尿道感染 (Urinary Tract Infection) |
| TxGNN 預測分數 | 99.03% |
| 證據等級 | L3 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據 DrugBank 及既有文獻，MICAFUNGIN 屬於 echinocandin 類抗黴菌藥物，
其作用是抑制真菌細胞壁 β-(1,3)-D-glucan 合成，對 *Candida* 屬（念珠菌）有殺菌活性，已廣泛用於侵襲性念珠菌感染的治療。

念珠菌尿路感染（candiduria / Candida UTI）是院內感染常見問題，尤其好發於留置導尿管、糖尿病或免疫低下患者。
傳統上 echinocandins 因尿中濃度低而不被優先建議用於 UTI，但多篇文獻（如 PMID 27424599）指出，
micafungin 在尿液中的實際濃度足以達到治療效果，對氟康唑（fluconazole）抗藥性的念珠菌菌株（如 *C. krusei*、*C. glabrata*）尤其有臨床應用價值，
這與 TxGNN 模型預測 MICAFUNGIN 可能適用於泌尿道感染的方向一致。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | 回溯性世代研究 | Antimicrob Agents Chemother | 分析 305 位住院患者的念珠菌尿路感染治療現況，指出無症狀候選病人常被過度治療 |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | 回溯性世代研究 | Pediatrics International | PICU 兒童院內念珠菌尿路感染使用 micafungin 治療的成功率分析 |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | 回溯性分析 | Int Urol Nephrol | 住院患者使用 micafungin 治療與根除念珠菌尿的成效評估 |
| [24182454](https://pubmed.ncbi.nlm.nih.gov/24182454/) | 2014 | 前瞻性監測研究 | Int J Antimicrob Agents | 美國 52 家醫院、1218 例念珠菌血流感染的物種分布與抗藥性資料，含 micafungin 敏感性 |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | 橫斷面研究 | Ther Adv Infect Dis | 越南念珠菌外陰陰道炎與泌尿道感染之菌種分布與抗黴菌藥物敏感性 |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | 病例系列 | Int J Antimicrob Agents | 6 例念珠菌尿路感染以 micafungin 成功治療，證實尿中濃度足以達治療效果 |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | 病例系列 | Med Mycol Case Rep | 5 例候選病人接受靜脈 micafungin 治療，治療 30 天內真菌消失 |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | 病例報告 | Transpl Infect Dis | 肝腎移植患者以高劑量 micafungin 成功根除慢性 *C. krusei* 尿路感染 |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | 病例報告 | Front Pediatr | 早產兒 *C. glabrata* 尿路感染以 micafungin 治療的臨床案例 |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | 病例報告 | J Pharm Health Care Sci | SGLT2 抑制劑使用患者併發 *C. glabrata* 腎盂腎炎及菌血症，以 micafungin 成功治療 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
文獻證據以病例報告與回溯性研究為主（L3），顯示 micafungin 對念珠菌尿路感染（尤其抗藥菌株）有實務治療經驗，
但目前無正式臨床試驗支持，且台灣未上市、無核准適應症與仿單安全性資料（警語、禁忌症皆缺），
安全性初評（S1）因資料缺口（DG001）而無法進行，暫不建議推進。

**若要推進需要：**
- 取得 TFDA／原廠仿單警語與禁忌症資料，補齊安全性初評所需資訊（DG001，Blocking）
- 補充完整作用機轉（MOA）資料以強化機轉關聯性分析（DG002）
- 評估是否有前瞻性臨床試驗或系統性回顧支持念珠菌尿路感染適應症
- 確認未來台灣上市規劃或現行仿單適應症範圍
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

