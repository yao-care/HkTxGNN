---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 673
evidence_level: L5
indication_count: 9
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-11-24
description: "Pembrolizumab：預測新適應症為牙齦纖維瘤病 (Gingival Fibromatosis)（證據等級 L5）。原適應症：知識圖譜記錄的關聯：非小細胞肺癌、肺癌、轉移性黑色素瘤"
---

# Pembrolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Pembrolizumab：從非小細胞肺癌與轉移性黑色素瘤到牙齦纖維瘤病
{: .text-alpha }

## 一句話總結

Pembrolizumab 是一種 PD-1 免疫檢查點抑制劑（單株抗體），知識圖譜中記錄的原用途為非小細胞肺癌、肺癌與轉移性黑色素瘤。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (Gingival Fibromatosis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：非小細胞肺癌、肺癌、轉移性黑色素瘤（香港許可證資料未載明適應症文字） |
| 預測新適應症 | 牙齦纖維瘤病 (Gingival Fibromatosis) |
| TxGNN 預測分數 | 0.9940 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前此預測的合理性**很有限**。Pembrolizumab 的標靶為 PD-1（PDCD1/CD279），透過阻斷 PD-1 與其配體的結合，解除 T 細胞受抑制的狀態，使免疫系統攻擊腫瘤。根據美國 FDA 核准的 Pembrolizumab 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「PD-1配體PD-L1及PD-L2與T細胞上的PD-1受體結合後，會抑制T細胞增生及細胞激素生成。部分腫瘤會出現PD-1配體上調，經由此路徑的訊號傳遞可能促成腫瘤之主動T細胞免疫監測受到抑制。[…] Pembrolizumab是一種單株抗體，可與PD-1受體結合並阻斷其與PD-L1及PD-L2的交互作用，從而解除PD-1路徑所介導的免疫反應抑制，包括抗腫瘤免疫反應。」英文原文："Binding of the PD-1 ligands, PD-L1 and PD-L2, to the PD-1 receptor found on T cells, inhibits T cell proliferation and cytokine production. Upregulation of PD-1 ligands occurs in some tumors and signaling through this pathway can contribute to inhibition of active T-cell immune surveillance of tumors. […] Pembrolizumab is a monoclonal antibody that binds to the PD-1 receptor and blocks its interaction with PD-L1 and PD-L2, releasing PD-1 pathway-mediated inhibition of the immune response, including the anti-tumor immune response."（[DailyMed: Keytruda (pembrolizumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9333c79b-d487-4538-a9f0-71b91a02b287)，版本日期 2026-10-16；查閱日期 2026-11-19）。

牙齦纖維瘤病是一種遺傳性或藥物誘發的纖維化病變，目前沒有已知的 PD-1 路徑參與。因此，我們未能找到可連結 pembrolizumab 與此疾病的機轉。高分預測來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-64228 | KEYTRUDA SOLUTION FOR INJECTION 100MG/4ML | 單一成分 | MERCK SHARP & DOHME (ASIA) LTD | 有效 |

<!-- licenses:end -->

此為單一成分許可證，廠商為 MERCK SHARP & DOHME (ASIA) LTD。

---

## 細胞毒性

Pembrolizumab 為抗腫瘤的免疫治療藥物，屬免疫檢查點抑制劑，並非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（PD-1 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：共查得 13 筆。
  - 重大等級（Major）：lenalidomide、pomalidomide、thalidomide。
  - 中度等級（Moderate）：多種皮質類固醇，包括 hydrocortisone、triamcinolone、dexamethasone、betamethasone、budesonide、prednisolone、prednisone、methylprednisolone、deflazacort。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有任何臨床試驗或文獻直接研究 pembrolizumab 用於牙齦纖維瘤病，也找不到合理的機轉連結，證據等級為 L5。
- 目前缺乏仿單層級的警語與禁忌症資料，無法進行安全性篩選。

**若要推進需要：**
- 取得 pembrolizumab 的作用機轉資料，並評估 PD-1 路徑與牙齦纖維化的任何關聯。
- 進行前臨床或機轉研究，建立生物學上的合理依據。
- 取得香港衛生署的仿單，補齊警語與禁忌症資料。
- 評估免疫相關不良反應對此族群的風險與效益。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Keytruda (pembrolizumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9333c79b-d487-4538-a9f0-71b91a02b287) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

