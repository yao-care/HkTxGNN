---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 801
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sebelipase Alfa：預測新適應症為Scheie 症候群 (Scheie syndrome)（證據等級 L5）。原適應症：Wolman 病、溶小體酸性脂肪酶缺乏症、溶小體脂質儲積症"
monitor_inn: "Sebelipase alfa"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "cholesteryl ester storage disease", "Gaucher disease", "lysosomal storage disease with skeletal involvement", "autosomal ichthyosis syndrome with fatal disease course", "Tay-Sachs disease", "benign neoplasm of adrenal gland"]
---

# Sebelipase Alfa
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

# Sebelipase alfa：從溶小體酸性脂肪酶缺乏症（Wolman 病）到 Scheie 症候群

## 一句話總結

Sebelipase alfa 是重組人類溶小體酸性脂肪酶（LAL），原本用於溶小體酸性脂肪酶缺乏症（LAL-D，包含 Wolman 病）的酵素替代治療。
TxGNN 模型排名第一的預測是 **Scheie 症候群 (Scheie syndrome)**，但目前**沒有任何臨床試驗或文獻**支持，機轉上也缺乏依據。
在前 10 名預測中，唯一有充分證據的是**膽固醇酯儲積症 (cholesteryl ester storage disease)**，而它其實是藥物原本的核准適應症，並非真正的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Wolman 病、溶小體酸性脂肪酶缺乏症、溶小體脂質儲積症（香港許可證未登載適應症文字） |
| 預測新適應症 | Scheie 症候群 (Scheie syndrome) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

> 補充：排名第 4 的膽固醇酯儲積症（分數 99.72%）證據等級為 L1，建議 Proceed with Guardrails，但屬於既有適應症的延伸驗證。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Sebelipase alfa 是重組人類溶小體酸性脂肪酶，透過靜脈輸注補充缺乏的酵素，水解溶小體中累積的膽固醇酯與三酸甘油酯，進而改善肝功能異常與血脂異常。

Scheie 症候群（輕型黏多醣症 I 型）是由 α-L-艾杜糖醛酸酶缺乏所致，作用的受質是糖胺聚醣，與 LAL 的受質（膽固醇酯、三酸甘油酯）完全不同。兩者唯一的共通點是「溶小體酵素替代治療」這個大概念。因此，高 TxGNN 分數較可能是圖譜關聯的結果，缺乏生化上的支持。

前 10 名預測中，其他項目大致分兩類：
- **本身就是 LAL-D 的表現型**：膽固醇酯儲積症、Wolman 病（含低脂蛋白血症與棘狀紅血球變異型），屬於既有適應症。
- **機轉上缺乏連結**：Hurler 症候群、Gaucher 病、Tay-Sachs 病、其他溶小體疾病、STAT5B 相關生長激素不敏感症候群、魚鱗癬症候群及腎上腺良性腫瘤。這些疾病的缺陷酵素或病理機轉與 LAL 不同。Tay-Sachs 病另有血腦障壁問題。腎上腺腫瘤可能只是因 Wolman 病常見腎上腺鈣化而產生的圖譜關聯。

---

## 臨床試驗證據

Scheie 症候群目前無相關臨床試驗登記。

作為參考，排名第 2 的 Hurler 症候群僅有一個間接相關的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | 招募中 | 10 | 產前酵素替代治療平台試驗，涵蓋多種溶小體儲積症；無證據顯示 Sebelipase alfa 用於 Hurler 症候群 |

排名第 4 的膽固醇酯儲積症（既有適應症）有以下較直接的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Phase 3 | 完成 | 66 | 隨機、安慰劑對照，晚發型 LAL-D 每兩週 1 mg/kg 靜脈輸注的療效與安全性 |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Phase 2 | 完成 | 31 | 開放性多中心研究，廣泛 LAL-D 族群 |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Phase 2/3 | 完成 | 9 | 劑量遞增研究，LAL-D 導致生長遲緩的兒童 |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Phase 2 | 完成 | 8 | 成人 LAL-D 的長期安全性與療效延伸研究 |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Phase 1/2 | 完成 | 9 | 首個 LAL-D 人體研究，成人劑量遞增 |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Phase 2 | 已終止 | 10 | 快速進展型嬰兒 LAL-D；提前終止，解讀受限 |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | 已不可取得 | N/A | 擴大使用計畫，提供藥物可近性而非療效證據 |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | 招募中 | 10 | 產前酵素替代治療平台試驗，與既有 CESD 證據關聯較遠 |

---

## 文獻證據

Scheie 症候群目前無相關文獻。

以下為膽固醇酯儲積症／LAL-D（既有適應症）的代表性文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26352813](https://pubmed.ncbi.nlm.nih.gov/26352813/) | 2015 | Phase 3 試驗 | N Engl J Med | Sebelipase alfa 用於兒童與成人 LAL-D 的 Phase 3 試驗 |
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT | J Hepatol | ARISE 研究最終結果，≥4 歲兒童與成人 LAL-D |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | RCT | J Clin Lipidol | 改善動脈粥狀硬化相關生物標記，最長 52 週 |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Cohort | Liver Int | 國際登錄資料顯示治療後轉胺酶改善 |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Cohort | J Pediatr Gastroenterol Nutr | 兒童與成人長期治療的療效與安全性 |
| [32657505](https://pubmed.ncbi.nlm.nih.gov/32657505/) | 2020 | Cohort | Liver Int | Phase 2 延伸研究 5 年經驗 |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Cohort | Orphanet J Rare Dis | Wolman 病全國性世代，最長 10 年追蹤 |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Cohort | Orphanet J Rare Dis | 每週兩次給藥可挽救重症 Wolman 病嬰兒 |
| [28179030](https://pubmed.ncbi.nlm.nih.gov/28179030/) | 2017 | 臨床研究 | Orphanet J Rare Dis | 嬰兒 LAL-D 的存活結果（劑量遞增研究） |
| [26452566](https://pubmed.ncbi.nlm.nih.gov/26452566/) | 2015 | Review | Drugs | Sebelipase alfa 首次全球核准概述 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68733 | KANUMA CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/10ML（廠商：AstraZeneca Hong Kong Limited） | 輸注用濃縮液 | 資料中未登載 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（針對排名第一的 Scheie 症候群）**

**理由：**
- Scheie 症候群的預測只有模型分數，沒有臨床試驗與文獻；缺陷酵素與受質都與 LAL 不同，機轉上缺乏支持。
- 前 10 名中真正有證據的（膽固醇酯儲積症 L1、Wolman 病 L3）都是既有適應症，不屬於新的再利用機會。

**若要推進需要：**
- 若關注既有適應症：可針對膽固醇酯儲積症與 Wolman 病（Proceed with Guardrails）補齊香港仿單的適應症、警語與禁忌資料。
- 若關注 Scheie 症候群等新適應症：需先有生化或前臨床證據，證明 LAL 與該疾病的病理有關。
- 取得詳細的作用機轉資料與香港仿單安全性資訊。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

