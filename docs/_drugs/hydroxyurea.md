---
layout: default
title: Hydroxyurea
parent: 中證據等級 (L3-L4)
nav_order: 440
evidence_level: L4
indication_count: 5
---

# Hydroxyurea
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Hydroxyurea：從抗腫瘤／血液疾病用藥到女性乳癌

## 一句話總結

Hydroxyurea（羥基脲）是口服抗腫瘤藥物，文獻中也用於白血病、鐮刀型貧血等疾病。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前**沒有登記中的臨床試驗**，只有 **20 篇文獻**，多為前臨床研究與 1990 年代的多藥合併方案早期試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺漏。根據 Evidence Pack 的機轉推論與文獻，Hydroxyurea 抑制核糖核苷酸還原酶 (ribonucleotide reductase, RNR)，使 dNTP 池耗竭並造成 DNA 複製壓力 (replication stress)。

這個機轉與乳癌細胞的弱點有關。前臨床研究顯示，乳癌細胞的複製壓力迴避機制 (EYA4)、ATR 訊號和 RPA2 過度磷酸化修復路徑，都與癌細胞對 Hydroxyurea 或 RNR 抑制劑的敏感性有關。因此，Hydroxyurea 在乳癌上的作用有機轉上的合理性。

要注意的是，TxGNN 分數只是模型預測，不是臨床證據。1990 年代的合併方案（PMID 1957839、7914447）都是多藥組合，無法分離出 Hydroxyurea 單獨的效果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II 類型研究 | Bone Marrow Transplant | 26 位轉移性乳癌女性，在 cyclophosphamide + thiotepa 加上 18 g/m² Hydroxyurea，並搭配自體幹細胞救援，作為鞏固化療 |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | Am J Clin Oncol | 20 位晚期消化道與乳癌患者，5-FU/leucovorin 後接 Hydroxyurea，並以 allopurinol 保護（HALF 方案） |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | 前臨床（電腦模擬） | Drug Res | 設計 Hydroxyurea 脂質藥物複合物，以提高親脂性與細胞攝取，標靶 PI3K/AKT/mTOR 路徑 |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | 前臨床（機轉） | Mol Cancer | EYA4 透過迴避複製壓力促進乳癌進展與轉移 |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 前臨床 | DNA Repair | Valproic acid 抑制 RPA2 過度磷酸化的修復路徑，使乳癌細胞對 Hydroxyurea 更敏感 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 前臨床 | DNA Repair | 以其他化合物影響 RPA2 機轉，其背景是 Valproic acid 可使乳癌細胞對 Hydroxyurea 增敏 |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | 前臨床 | Naunyn Schmiedebergs Arch Pharmacol | Hydroxyurea 負載奈米粒子，評估 pH 依賴性藥物釋放、細胞週期停滯及 p53、lincRNA-p21 表現 |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | 前臨床 | Br J Cancer | 在乳癌與卵巢癌細胞株中評估 ATR 抑制劑 NU6027，Hydroxyurea 為複製壓力的背景 |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | 前臨床 | Mol Pharmacol | 新型 RNR 抑制劑 COH29 抑制 DNA 修復，對象為 BRCA1 缺陷乳癌細胞 |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | 病例報告 | Case Rep Hematol | 乳癌合併原發性血小板增多症 (ET) 的治療處理 |

## 香港上市資訊

資料未提供劑型與核准適應症文字，以下由品名可見劑型為 500 mg 膠囊。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-52895 | APO-HYDROXYUREA CAP 500MG | HIND WING CO LTD |
| HK-66544 | HYDROXYUREA MEDAC CAPSULES 500MG | HONBASE TRADING LIMITED |
| HK-67918 | HYDROXYCARBAMIDE TEVA CAPSULES 500MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-67191 | HYDROXYCARBAMIDE SANDOZ CAPSULES 500MG | SANDOZ HONG KONG LIMITED |
| HK-66629 | HYDROXYUREA CAPSULES 500MG | HEALTHCARE PHARMASCIENCE LIMITED |

## 細胞毒性

Evidence Pack 沒有 Hydroxyurea 的毒性資料，下表為依藥物類別的一般藥理知識整理，請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗代謝、RNR 抑制劑） |
| 骨髓抑制風險 | 高（骨髓抑制為主要劑量限制毒性；相關文獻也提到血小板低下） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類與血小板）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳癌適應症目前沒有任何登記的臨床試驗。
- 文獻多為前臨床研究，以及無法分離 Hydroxyurea 效果的 1990 年代多藥合併早期試驗，證據等級僅 L4。
- TxGNN 分數雖高，仍只是模型預測。
- 同一份 Evidence Pack 中，預測適應症第 2 名「鐮刀型血球-血紅素 C 疾病 (HbSC)」證據較強（L2，建議 Proceed with Guardrails），建議另案評估。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料（目前為阻斷性缺口）。
- 補充 DrugBank 的作用機轉資料。
- 進一步的前臨床驗證，例如 Hydroxyurea 單藥或合併治療（如 ATR 抑制劑、HDAC 抑制劑）在不同乳癌亞型的療效。
- 設計並登記乳癌臨床試驗，以隔離 Hydroxyurea 的獨立貢獻。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

