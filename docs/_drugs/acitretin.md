---
layout: default
title: Acitretin
parent: 中證據等級 (L3-L4)
nav_order: 20
evidence_level: L4
indication_count: 4
---

# Acitretin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Acitretin：從乾癬/角化異常到痤瘡

## 一句話總結

Acitretin 是第二代口服視網酸（retinoid），主要用於乾癬及嚴重角化異常皮膚疾病的治療。TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效，但查詢到的 **1 個臨床試驗**並非針對 acitretin 本身，**18 篇文獻**中多為 retinoid 通論或化膿性汗腺炎（acne inversa）研究，直接支持 acitretin 用於一般型痤瘡的高品質證據仍十分有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾癬、嚴重角化異常皮膚病（台灣/香港未有上市許可，資料來源為機轉分析文獻）|
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏來自 DrugBank 的官方作用機轉資料。根據文獻記載，Acitretin 是第二代芳香族視網酸，透過與細胞核受體 RAR（retinoic acid receptor）及 RXR（retinoid X receptor）結合，調控皮脂腺活性並促進角質細胞正常分化。就痤瘡而言，皮脂腺過度分泌與角質細胞分化異常（導致毛囊開口阻塞、粉刺形成）正是核心病理，因此機轉上具備理論關聯性。

然而，在 retinoid 家族中，isotretinoin（13-cis retinoic acid）才是痤瘡治療的第一線口服視網酸；acitretin 的臨床定位在乾癬及其他角化異常疾病，並非痤瘡的主流選項。現有文獻中涉及「acne」者，多描述的是化膿性汗腺炎（Hidradenitis suppurativa，HS）—— 又稱 acne inversa —— 其病理機轉與一般型面部痤瘡存在明顯差異。

值得注意的是，根據機轉分析，acitretin 具有嚴重致畸胎性（Pregnancy Category X）。痤瘡的主要患者族群為育齡女性，此安全疑慮在評估應用可行性時為關鍵限制，需特別謹慎評估風險效益比。

---

## 臨床試驗證據

目前無直接評估 acitretin 用於痤瘡的臨床試驗登記。

查詢到 1 筆試驗（NCT04663906），但研究藥物為 isotretinoin（非 acitretin），研究問題為 COVID-19 感染風險（非痤瘡療效），與本評估目標無直接相關性，故不列入正式證據表格。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Cochrane 系統回顧 | Cochrane Database Syst Rev | 評估盤狀紅斑性狼瘡（DLE）藥物治療，含 acitretin，間接提示 retinoid 在炎症性皮膚病的應用潛力 |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | 長期追蹤研究 | Br J Dermatol | Acitretin 治療化膿性汗腺炎（acne inversa）25 年長期成果，案例數據最完整的 acitretin 皮膚科研究之一 |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | 臨床指引（S1 等級）| JEADV | 歐洲化膿性汗腺炎治療指引，acitretin 被納入治療選項之一 |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | 綜述 | Hautarzt | Acne inversa（HS）藥物治療全面回顧，討論 retinoid 在系統治療中的角色 |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | 敘述性綜述 | Clin Dermatol | 維生素 A 與 retinoid 在皮膚科的全面回顧，明確列出 acitretin 的核准適應症範圍 |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | 敘述性綜述 | Drugs | 三代 retinoid 在皮膚科現況與未來潛力，含嚴重痤瘡及皮膚癌化學預防的討論 |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | 機轉綜述 | Dermatology | 探討 retinoid 抑制皮脂腺活性的實驗模型，比較 isotretinoin 與其他口服 retinoid 的預測模型適用性 |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | 病例報告 | Cutis | Acitretin 治療結節囊腫型痤瘡合併 HS 的個案，為 acitretin 直接用於痤瘡型病灶的少數紀錄之一 |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | 綜述 | Clin Pharmacokinet | Retinoid 藥物動力學與療效回顧，明確指出 acitretin 主要成功應用於乾癬 |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | 機轉研究 | Prostaglandins | 八種 retinoid（含 acitretin）對嗜酸性白血球 LTC4 釋放的抑制效果，提示抗炎機轉基礎 |

---

## 香港上市資訊

Acitretin 在香港目前**未有上市許可**，無相關藥品登記資料可供參考。

---

## 安全性考量

安全性資訊請參考原廠仿單。

**重要注意事項**（來源：機轉分析文獻）：Acitretin 具有嚴重致畸胎性，在多數痤瘡患者族群（育齡女性）中使用時，需依原廠仿單評估嚴格的避孕管理方案與用藥前後的安全性監控要求。詳細警語與禁忌請查閱原廠藥品仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前無直接評估 acitretin 用於一般型痤瘡的 RCT 或前瞻性臨床研究；現有文獻多為 retinoid 通論回顧或化膿性汗腺炎（acne inversa）研究，不能視為一般痤瘡適應症的直接支持
- 同類藥物 isotretinoin 已是痤瘡的標準療法，acitretin 用於痤瘡缺乏明確的差異化優勢，且在育齡族群中的致畸胎性安全疑慮為不可忽視的重大限制

**若要推進需要：**
- 明確釐清目標患者族群：一般型痤瘡 vs. 化膿性汗腺炎（acne inversa）vs. isotretinoin 治療失敗的特殊案例
- 補充完整 MOA 資料：查詢 DrugBank API（DB00459）取得官方作用機轉說明
- 補充安全性資料：下載原廠仿單 PDF 並解析警語、禁忌症及致畸胎性管理規範（TFDA 官網）
- 評估 isotretinoin 與 acitretin 的競爭定位，確認在何種臨床情境下 acitretin 具有替代價值
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

