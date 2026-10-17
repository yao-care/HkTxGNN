---
layout: default
title: Pemetrexed
parent: 高證據等級 (L1-L2)
nav_order: 674
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Pemetrexed：預測新適應症為惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma)（證據等級 L2）。原適應症：非小細胞肺癌、肺癌、惡性胸膜間皮瘤"
monitor_inn: "PEMETREXED"
predicted_indications: ["pleural adenomatoid tumor"]
---

# Pemetrexed
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Pemetrexed：從非小細胞肺癌與惡性胸膜間皮瘤到惡性腹膜間皮瘤

## 一句話總結

Pemetrexed 是多靶點抗葉酸藥物，原本用於非小細胞肺癌與惡性胸膜間皮瘤的治療。
TxGNN 模型預測它可能對**惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向，但多數為小型或混合族群研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌、惡性胸膜間皮瘤（香港許可證未登載適應症文字，以知識圖譜資料為準） |
| 預測新適應症 | 惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠機轉欄位為空）。依文獻與已知藥理，Pemetrexed 是多靶點抗葉酸藥物，抑制胸苷酸合成酶 (TS)、二氫葉酸還原酶 (DHFR) 與甘胺醯胺核糖核苷酸甲醯基轉移酶 (GARFT)，阻斷快速分裂腫瘤細胞的核苷酸合成。

腹膜間皮瘤與胸膜間皮瘤同樣源自間皮細胞，組織學相似，因此抗葉酸機轉在生物學上合理。胸膜間皮瘤已有第三期隨機試驗（Vogelzang 2003）證實 pemetrexed 加 cisplatin 優於單用 cisplatin。Pemetrexed 加鉑類目前已被超適應症用於腹膜間皮瘤的全身性治療。

不過，腹膜間皮瘤極為罕見，專屬的前瞻性試驗很少，現行建議多由胸膜間皮瘤的試驗外推而來，證據強度較胸膜疾病弱。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | 完成 | 48 | Pemetrexed 併用 gemcitabine 作為惡性胸膜或腹膜間皮瘤第一線治療，直接納入腹膜族群 |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | 招募中 | 66 | 隨機試驗：carboplatin、pemetrexed、bevacizumab 加或不加 atezolizumab，用於腹膜間皮瘤；尚無結果 |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | 暫停 | 66 | PIPAC 加全身化療（cisplatin + pemetrexed）對比單用全身化療；無法單獨評估 pemetrexed 貢獻 |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | 招募中 | 28 | 單臂試驗：sintilimab、bevacizumab 併用 pemetrexed 與 cisplatin |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | 招募中 | 64 | ICARuS II：減積手術與 HIPEC 後腹腔內化療對比靜脈化療；pemetrexed 非主要變因 |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | 進行中（不招募） | 30 | TRC102 併用 cisplatin 與 pemetrexed，晚期實體腫瘤混合族群 |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | 完成 | 19 | Cisplatin、pemetrexed、imatinib 用於轉移性間皮瘤的最大耐受劑量研究 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | 回溯性研究 | Jpn J Clin Oncol | Pemetrexed 加 cisplatin 作為晚期腹膜間皮瘤第一線化療的療效與安全性 |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | 回溯性研究 | Expert Rev Anticancer Ther | 第一線 pemetrexed 加 cisplatin 治療腹膜間皮瘤的療效 |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | 單一機構經驗 | Tumori | 未接受過化療患者使用 pemetrexed-cisplatin 的療效與安全性 |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | 回溯性比較 | Clin Med Insights Oncol | 比較第一線 pemetrexed-鉑類與 gemcitabine-鉑類方案 |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | 多中心研究 | Ann Surg Oncol | 腹膜間皮瘤的治療策略與預後分析 |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | 治療綜述 | J Natl Compr Canc Netw | 全身治療建議多由胸膜間皮瘤試驗外推；第一線可選 nivolumab + ipilimumab 或 pemetrexed 為基礎的化療 |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | 瀰漫性腹膜間皮瘤診療路徑；CRS + HIPEC 為最佳選擇，中位存活 34–92 個月 |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | 選定患者以減積手術加 HIPEC 為首選初始治療 |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | 惡性腹膜間皮瘤綜述 |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | 病例報告 | BMJ Case Rep | Nivolumab 用於腹膜間皮瘤個案 |

## 香港上市資訊

香港共有 17 張有效許可證，皆為單方注射用粉劑（濃縮輸注液用）。以下列出 5 張主要許可證，其核准適應症文字與劑型欄位於資料中皆未登載。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53331 | ALIMTA 500mg（Eli Lilly Asia） | 輸注用濃縮粉劑 | 資料未登載 |
| HK-58016 | ALIMTA 100mg（Eli Lilly Asia） | 輸注用濃縮粉劑 | 資料未登載 |
| HK-64687 | PEMETREXED 100mg（Chemillennium） | 輸注用濃縮粉劑 | 資料未登載 |
| HK-64688 | PEMETREXED 500mg（Chemillennium） | 輸注用濃縮粉劑 | 資料未登載 |
| HK-64649 | PEMETREXED SANDOZ 100mg | 輸注用濃縮粉劑 | 資料未登載 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸代謝拮抗劑） |
| 骨髓抑制風險 | 高。知識圖譜顯示與嗜中性白血球低下、血小板低下、貧血、顆粒球缺乏症相關 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、腎功能（知識圖譜顯示腎功能不全為禁忌相關） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **禁忌相關疾病（來自知識圖譜，非仿單文字）**：腎臟疾病、腎功能不全、血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血、巨球性貧血、膿尿輸尿管。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用：
  - 腎毒性或影響腎小管分泌的藥物：Amphotericin B（含脂質體等劑型）、Vancomycin、Kanamycin、Neomycin、Polymyxin B
  - 抗潰瘍藥物：Famotidine、Ranitidine、Cimetidine
  - 其他：Metformin、Amoxicillin、Levofloxacin、乙醯水楊酸 (Aspirin)、Mesalazine、Balsalazide、Olsalazine、Sapropterin

香港仿單的警語與禁忌尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 腹膜間皮瘤已有 1 個已完成的 Phase 2 試驗（NCT00061477，直接納入腹膜族群）及多項回溯性研究支持，證據等級為 L2。但多為小型、混合族群或進行中的試驗，且多數建議由胸膜間皮瘤外推。
- Pemetrexed 在香港已上市，且在胸膜間皮瘤已有 Phase 3 證據，機轉合理，骨髓抑制與腎功能風險可透過監測管理。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字，釐清是否屬超適應症使用
- 取得詳細作用機轉資料（原廠資料欄位目前為空）
- 追蹤進行中隨機試驗（NCT05001880、NCT06543069）的結果
- 建立血液學與腎功能監測計畫，並配合葉酸與維生素 B12 補充及交互作用審查
- 與免疫治療（nivolumab + ipilimumab）及減積手術加 HIPEC 等替代方案進行比較評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

