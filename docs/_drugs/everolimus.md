---
layout: default
title: Everolimus
parent: 高證據等級 (L1-L2)
nav_order: 300
evidence_level: L2
indication_count: 5
---

# Everolimus
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Everolimus：從 mTOR 抑制到脂肪肉瘤

## 一句話總結

Everolimus 是 mTORC1 的選擇性抑制劑，全球已核准用於多種實體腫瘤及器官移植排斥預防，但在香港尚未取得許可證。TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，目前有 **4 篇文獻**（含 1 項 Phase II 臨床試驗）支持這個方向，尚無已登記的正式臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未核准（全球核准包含腎細胞癌、乳癌等實體腫瘤） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

去分化型脂肪肉瘤（Dedifferentiated Liposarcoma, DDLPS）是脂肪肉瘤中侵襲性較強的亞型，分子特徵之一是 MDM2/CDK4 基因頻繁擴增，以及 PI3K/Akt/mTOR 訊號通路的過度活化（PMID 26518767）。Everolimus 作為 mTORC1 的選擇性抑制劑，能阻斷下游效應分子 S6K1 和 4EBP1，進而抑制腫瘤細胞的蛋白質合成與異常增殖——此機轉與 DDLPS 的核心分子病理高度吻合。

SAR-096 Phase II 試驗（PMID 37967116）進一步強化了此假說的臨床可行性：試驗採用 CDK4/6 抑制劑 Ribociclib 聯合 Everolimus，對 CDK4 擴增（mTOR 上游節點）及 mTOR 本身進行雙重阻斷，機轉互補且在多種腫瘤模型中已顯示協同增殖抑制效果，提供直接的腫瘤生物學依據。

從臨床需求角度看，軟組織肉瘤（包含脂肪肉瘤）現有化療方案（如 Doxorubicin、Gemcitabine/Docetaxel）整體療效有限，復發後尤為匱乏，使靶向 mTOR 的新治療策略具有明確的未被滿足臨床需求，支持進一步探索的合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 及 ICTRP 查詢均無結果）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II RCT | Clinical Cancer Research | Ribociclib + Everolimus 用於進展性去分化型脂肪肉瘤（DDL）及平滑肌肉瘤（LMS），驗證 CDK4/mTOR 雙重阻斷策略的臨床療效 |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | 轉譯/機轉研究 | Tumour Biology | 99 例 DDLS 標本免疫組化分析，確認 Akt/mTOR 及 MAPK 通路活化；體外試驗顯示 mTOR 抑制劑具直接抗腫瘤效果 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review（前臨床 PDOX 模型） | Frontiers in Oncology | 患者來源異種移植（PDOX）模型鑑別 CDK 抑制劑聯合 mTOR 抑制劑的協同療效，提出肉瘤個人化聯合治療策略 |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 前臨床聯合用藥研究 | Anticancer Research | Eribulin 聯合多種機轉不同抗癌藥物（含 mTOR 抑制劑）的廣譜異種移植模型抗腫瘤活性評估，涵蓋脂肪肉瘤 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（mTOR 抑制劑 / Rapalogue 類） |
| 骨髓抑制風險 | 低至中度（可能出現貧血、血小板減少、嗜中性白血球減少） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含分類）、空腹血糖、血脂、肝腎功能；警覺間質性肺炎（ILD/pneumonitis）早期症狀 |
| 處置防護 | 口服藥物，依一般抗腫瘤藥物處置規範操作；需注意口腔黏膜炎及機會性感染風險 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
SAR-096 Phase II 臨床試驗直接評估 Everolimus 聯合 CDK4/6 抑制劑用於去分化型脂肪肉瘤，加上機轉研究（PMID 26518767）明確確認 mTOR 通路在 DDLPS 中的生物學驅動角色，構成 L2 等級支持證據，科學基礎充分；但香港許可狀態（未上市）及安全性資料缺口須在推進前補足。

**若要推進需要：**
- 取得香港仿單或原廠仿單，補充警語與禁忌症（現為 Blocking 資料缺口 DG001，無法完成 S1 安全性初評）
- 查詢 DrugBank API 補充完整 MOA 資料（DG002）
- 確認 SAR-096 試驗最終療效終點（ORR、PFS）及安全性數據
- 評估在香港未核准情況下的臨床試驗申請或同情用藥途徑
- 建立包含骨髓功能、間質性肺炎及代謝指標（血糖、血脂）的患者監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

