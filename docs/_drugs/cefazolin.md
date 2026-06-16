---
layout: default
title: Cefazolin
parent: 中證據等級 (L3-L4)
nav_order: 145
evidence_level: L3
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **8** 個
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

# Cefazolin：從外科預防感染到感染性中耳炎

## 一句話總結

Cefazolin 是一種第一代頭孢菌素類抗生素，在國際上廣泛用於外科手術預防感染及皮膚軟組織細菌感染，目前在香港並無上市許可。TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，目前有 **1 個臨床試驗**和 **3 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未取得香港許可（國際通用適應症：外科預防感染、皮膚軟組織感染） |
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏 Cefazolin 詳細的作用機轉資料（MOA Data Gap）。根據已知藥理知識，Cefazolin 屬於第一代頭孢菌素，作用機轉為抑制細菌細胞壁肽聚糖合成（β-lactam 機轉），對革蘭氏陽性菌——特別是 MSSA（甲氧西林敏感性金黃色葡萄球菌）和 *Streptococcus pyogenes*——具有強效殺菌活性；對部分革蘭氏陰性菌的覆蓋則相對有限。

感染性中耳炎的主要病原菌為 *Streptococcus pneumoniae*、*Haemophilus influenzae* 及 *Moraxella catarrhalis*。Cefazolin 對其中鏈球菌屬具有一定覆蓋，但**對 *H. influenzae* 和 *M. catarrhalis* 的覆蓋明顯不足**，而這兩者恰恰是急性中耳炎最常見的病原之一。

因此，雖然 TxGNN 模型基於藥-疾病知識圖譜關聯性給出了高達 99.44% 的預測分數，但從實際抗菌譜和臨床指引角度評估，Cefazolin 並非感染性中耳炎的理想治療選擇。現行國際指引（如 AAP AOM 指引）優先推薦 amoxicillin 或第二代以上頭孢菌素（如 cefuroxime、cefdinir），機轉合理性有限，需審慎對待模型預測結果。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2 | 提前終止 | 520 | 多中心雙盲安慰劑對照 RCT，比較 6–23 個月幼兒急性中耳炎短療程（5 天）vs 標準療程（10 天）抗生素治療的療效與對抗藥性的影響；試驗提前終止，且名稱未確認 Cefazolin 為主要介入藥物，整體信心度下降 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Report | Ann Otol Rhinol Laryngol | Ceftazidime + Cefazolin 合併作為兒童 Gradenigo 症候群（急性中耳炎罕見顱內併發症）的經驗性治療；文獻中 Cefazolin 扮演輔助抗菌角色，並非單藥主角 |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | South Med J | 頭孢菌素類藥物在兒科感染的應用回顧，涵蓋中耳炎等耳鼻喉感染情境，提及對青黴素過敏患者的替代選項；為老舊文獻，現代指引已有更佳替代方案 |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Series | Clinical Pharmacy | Stevens-Johnson 症候群個案，患者病程包含中耳炎並接受多種抗生素序貫治療；屬間接相關文獻，與 Cefazolin 療效評估關聯性低 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：TFDA/香港衞生署仿單警語、禁忌症及藥物交互作用資料尚未取得（Data Gap DG001），無法進行完整安全性初評，為本報告的重要限制。

---

## 結論與下一步

**決策：Research Question（建議暫緩，需釐清研究問題）**

**理由：**
TxGNN 給出高預測分數（99.44%），但 Cefazolin 對感染性中耳炎兩大核心病原（*H. influenzae*、*M. catarrhalis*）抗菌覆蓋不足，唯一的臨床試驗（Phase 2b）已提前終止，現有文獻均為間接證據或個案報告（最高僅 Tier 3），機轉合理性有限。此外，香港目前並無 Cefazolin 上市許可，進入臨床應用的准入門檻更高。

**若要推進需要：**
- 取得 Cefazolin 完整 MOA 及抗菌譜資料（DrugBank API，對應 Data Gap DG002）
- 補齊香港衞生署仿單安全性資料，包含警語、禁忌症與藥物交互作用（Data Gap DG001）
- 評估是否轉換研究方向至「**耳科手術圍術期預防性用藥**」情境——本 Evidence Pack 中 Rank 3「中耳疾病 (Middle Ear Disease)」在此情境下已有較強支持，建議決策為 **Proceed with Guardrails**（L3 證據等級），Cefazolin 對 MSSA 和 Streptococci 的預防效果已具一定文獻基礎
- 如聚焦治療性適應症，建議改為評估第二代或第三代頭孢菌素（如 cefuroxime、cefdinir），或以 Cefazolin 作為過敏患者替代選項的利基市場分析
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

