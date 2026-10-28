---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 9
monitor_inn: "HYDROXYUREA"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Hydroxyurea：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
---

# Hydroxyurea
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

## Hydroxyurea：從黑色素瘤與鐮刀型貧血到女性乳癌
{: .text-alpha }

## 一句話總結

Hydroxyurea 是一種核糖核苷酸還原酶抑制劑，知識圖譜中記錄的相關疾病包括黑色素瘤、鐮刀型貧血與卵巢癌等。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，但目前**沒有登記的臨床試驗**，僅有 **20 篇文獻**，多為前臨床或舊的複方化療 Phase 1 研究，證據屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症；知識圖譜記錄的相關疾病包括黑色素瘤、鐮刀型貧血、卵巢癌等（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

> 說明：排名第 1 的預測為女性乳癌，本報告以此為主軸。資料中雖有文獻討論 hydroxyurea 與乳癌，但沒有一篇是在乳癌患者中直接評估其療效，因此證據等級依規則定為 L5。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，hydroxyurea 為核糖核苷酸還原酶 (ribonucleotide reductase) 抑制劑，會耗竭 dNTP 池並造成 DNA 複製壓力。這是一種廣泛的抗增殖機轉，理論上可作用於快速分裂的腫瘤細胞。

前臨床研究顯示，乳癌細胞的複製壓力反應與對 hydroxyurea 的敏感性有關，例如 EYA4 與複製壓力迴避、valproic acid 透過抑制 RPA2 過度磷酸化而增強乳癌細胞對 hydroxyurea 的敏感性，以及 ATR 抑制劑在乳癌與卵巢癌細胞株的研究。不過這些多把 hydroxyurea 當作誘發複製壓力的工具，並非直接證明臨床療效。

另有一項 2024 年的電腦模擬研究，設計 hydroxyurea 脂質conjugate 以改善其親水性過高的問題，仍屬早期設計階段。整體而言，機轉上有合理性，但缺乏乳癌的臨床療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列為與乳癌或 hydroxyurea 較相關的文獻，均無乳癌的直接臨床療效證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1 複方化療 | Cancer Chemother Pharmacol | 5-FU、leucovorin、hydroxyurea 合併遞增劑量順鉑與放療，用於多種晚期實體腫瘤，非乳癌專屬 |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 複方化療 | Am J Clin Oncol | allopurinol、5-FU、leucovorin 後接 hydroxyurea，收錄 20 名晚期胃腸道與乳癌患者 |
| [9060546](https://pubmed.ncbi.nlm.nih.gov/9060546/) | 1997 | 臨床系列 | J Clin Oncol | 含 hydroxyurea 的 TPDC-FuHu 方案用於復發性轉移性腦瘤 |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | 電腦模擬/前臨床設計 | Drug Research | 設計 hydroxyurea 脂質conjugate，標靶 PI3K/AKT/mTOR 路徑 |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | 前臨床 | Molecular Cancer | EYA4 透過避免複製壓力促進乳癌進展與轉移 |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 前臨床（細胞） | DNA Repair | Valproic acid 抑制 RPA2 過度磷酸化，使乳癌細胞對 hydroxyurea 敏感 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 前臨床（細胞） | DNA Repair | 2-hexyl-4-pentynoic acid 影響 RPA2 介導的 DNA 修復，可能作為乳癌治療候選 |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | 前臨床 | Br J Cancer | ATR 抑制劑 NU6027 在乳癌與卵巢癌細胞株的評估，hydroxyurea 作為複製壓力工具 |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | 病例報告 | Case Rep Hematol | 乳癌合併原發性血小板增多症的治療挑戰 |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | 前臨床 | Mol Pharmacol | 新型核糖核苷酸還原酶抑制劑 COH29 在 BRCA1 缺陷乳癌細胞中抑制 DNA 修復 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52895 | APO-HYDROXYUREA CAP 500MG | 膠囊（品名標示） | 資料未載明 |
| HK-66544 | HYDROXYUREA MEDAC CAPSULES 500MG | 膠囊（品名標示） | 資料未載明 |
| HK-67918 | HYDROXYCARBAMIDE TEVA CAPSULES 500MG | 膠囊（品名標示） | 資料未載明 |
| HK-67191 | HYDROXYCARBAMIDE SANDOZ CAPSULES 500MG | 膠囊（品名標示） | 資料未載明 |
| HK-66629 | HYDROXYUREA CAPSULES 500MG | 膠囊（品名標示） | 資料未載明 |

以上 5 張均為單一成分、有效的許可證。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（核糖核苷酸還原酶抑制劑，抗代謝類） |
| 骨髓抑制風險 | 高。知識圖譜記錄的禁忌關聯包括白血球低下、血小板低下與貧血 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數 (CBC)、肝腎功能 |
| 處置防護 | 建議依細胞毒性藥物處置規範操作 |

其他細節請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、輸尿管積膿、血小板低下、貧血、大球性貧血、白血球低下、皮膚血管炎。
- **藥物交互作用**：資料庫共查得 100 筆，列出者多為等級未明，其中 levofloxacin 為輕微。其餘包含 doxycycline、amphotericin B、hydrocortisone、famotidine、acetylsalicylic acid、pantoprazole、metformin、omeprazole、prednisone、simvastatin 等，臨床意義需另行評估。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳癌沒有登記的臨床試驗，文獻僅為前臨床研究與舊的複方 Phase 1 研究，缺乏直接療效證據，目前僅有模型預測支持。
- 仿單安全性資料與作用機轉資料尚缺，且藥物有明確的骨髓抑制風險。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症內容
- 補充 DrugBank 的作用機轉資料
- 在乳癌（尤其是 BRCA 缺陷或複製壓力相關亞型）進行進一步前臨床驗證，並評估是否設計單獨或合併用藥的臨床試驗
- 擬定血液學監測計畫

> 補充：資料中另有鐮刀型血紅素 SC 病（Phase 2 試驗 NCT00532883 及 2025 年 NEJM Evidence 文獻）等預測，證據較乳癌豐富，建議另行評估為優先方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

