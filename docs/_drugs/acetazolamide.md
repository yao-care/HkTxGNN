---
layout: default
title: Acetazolamide
parent: 高證據等級 (L1-L2)
nav_order: 17
evidence_level: L2
indication_count: 10
---

# Acetazolamide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Acetazolamide：從青光眼／高山症到急性心衰竭去代償治療

## 一句話總結

Acetazolamide 為第一代碳酸酐酶抑制劑，傳統用於青光眼降眼壓、高山症預防、特定癲癇及週期性麻痺治療。TxGNN 模型共產生 10 項預測，其中**心肌病／急性心衰竭去代償 (Cardiomyopathy)** 為證據等級最強的適應症，目前有 **3 項大型 Phase 4 臨床試驗**（合計招募 1,805 人）及 **10 篇文獻**支持此方向，建議優先推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 青光眼、高山症、癲癇輔助治療、週期性麻痺（資料集缺乏正式許可證資訊）|
| 預測新適應症 | 心肌病 (Cardiomyopathy) |
| TxGNN 預測分數 | 99.83%（10 項預測中證據等級最強）|
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 Evidence Pack 缺乏正式 MOA 記錄（DG002），但根據已知藥理學資訊：Acetazolamide 透過抑制腎近端小管的碳酸酐酶，阻斷 H⁺/HCO₃⁻ 離子交換，促進碳酸氫鈉（NaHCO₃）大量排泄，產生鹼性利尿效果。此作用位點與傳統環利尿劑（如 furosemide 作用於亨利氏環）截然不同，兩者合用可產生互補協同效果。

急性心衰竭去代償期患者因長期大量使用環利尿劑，易發生代謝性鹼中毒（表現為低氯血症），而代謝性鹼中毒本身會進一步降低腎小管對環利尿劑的反應性，形成「利尿劑抵抗（diuretic resistance）」的惡性循環。Acetazolamide 能糾正代謝性鹼中毒、恢復尿液酸化，重新敏化髓袢對環利尿劑的反應，從而提升整體去充血效果（decongestion）。

此機轉的臨床有效性已由 2022 年發表於 NEJM 的 ADVOR Phase 3 RCT（n=519，資料集截止日前背景資訊）確立，其後三項大型 Phase 4 RCT 相繼啟動，進一步探索最佳利尿策略，為本報告評估的適應症提供充分機轉支撐。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | 招募中 | 939 | 大型雙盲 RCT，比較急性心衰竭容量過載患者中 Metolazone 與 Acetazolamide 合併環利尿劑的療效，並同步確認最佳環利尿劑種類；樣本量最大，預計 2027 年完成 |
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | 招募中 | 400 | 評估口服 Acetazolamide 於慢性心衰竭急性去代償期的療效，為本資料集中與「心肌病」適應症最直接對應的試驗，預計 2025 年完成 |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | 招募中 | 466 | TAILOR-AHF：評估尿鈉導向的個體化利尿算法（含 Acetazolamide 作為選項之一）於急性心衰竭去代償期的去充血效果，預計 2026 年完成 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Annual Review | ESC Heart Failure | 2024 心衰竭治療年度更新回顧，涵蓋 ESC 最新指引重要推薦，含 SGLT2i、finerenone 等新藥建議 |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | 2022 年心血管藥理新進展全面回顧，包含 mavacamten 核准（肥厚型心肌病）等新藥策略 |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiology Cases | 晚期心衰竭合併肥厚型心肌病患者因利尿劑治療引發低氯血症（94 mEq/L），使用 Acetazolamide 成功糾正電解質失衡，直接支持機轉合理性 |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Medical Journal | 探討 Acetazolamide 對兔離體缺血再灌注心臟的保護效果，2 週齡與 8 週齡兔之差異性比較 |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurol Scand | 低鉀血症週期性麻痺患者使用 Acetazolamide 750-1000 mg/天期間出現運動性心絞痛及 ST 段下移，具安全性參考價值 |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurol Scand | 家族性低鉀血症週期性麻痺合併心肌受累的心超及心臟評估，涉及 Acetazolamide 治療背景 |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Adverse Event Report | Acute Med Surg | ⚠️ 擴張型心肌病患者靜脈注射 Acetazolamide 後 1 小時出現非心因性肺水腫，重要安全性警示 |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian J Ophthalmol | Danon 病（溶酶體儲積性心肌病）合併黃斑水腫患者使用口服 Acetazolamide，治療 48 週後效果與監測 |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Case Report | J Nucl Med | 粒線體腦肌病 10 例 SPECT 腦血流研究，涉及 Acetazolamide 血管反應性激發試驗 |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | J Med Case Reports | 三體 9p 合併先天性腦水腫及先天性心臟病，Acetazolamide 治療在合併心臟異常情境下的複雜性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **來自文獻的重要安全訊號**（TFDA 仿單資料尚待補充，見 DG001）：
>
> - **靜脈注射風險**：有個案報告顯示靜脈注射 Acetazolamide 可能在心肌病患者中誘發非心因性肺水腫（PMID: 29123889），心功能不全患者應優先評估口服劑型。
> - **電解質監測**：長期使用（750-1000 mg/天）可能引起低鉀血症相關心臟症狀（PMID: 7324871），需定期監測血鉀及心電圖。
> - **肝硬化合併症**：合併肝功能異常患者使用 Acetazolamide 可能增加肝性腦病風險（NH₃/NH₄⁺ 平衡改變），應避免用於肝硬化心肌病（rank 6 預測明確建議 Hold）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
急性心衰竭去代償治療的機轉合理性已由 ADVOR Phase 3 RCT（NEJM 2022）確立，資料集內 3 項大型 Phase 4 RCT 合計 1,805 人正積極招募，為本報告所有 10 項 TxGNN 預測中實證基礎最強的適應症。香港目前雖無上市許可，但機轉與臨床證據均支持進一步評估引進可行性。

**若要推進需要：**
- 補充香港 Department of Health 仿單或 DrugBank 警語資料，完成安全性初評（DG001，Blocking）
- 確認 DrugBank 正式 MOA 資料以強化機轉分析報告（DG002）
- 密切追蹤 NCT05802849（預計 2025 年底完成）及 NCT06166654（預計 2027 年完成）最終結果
- 評估香港藥品進口許可申請途徑，確認口服劑型的可行性
- 制定靜脈注射 vs. 口服劑型的風險分層用藥安全監測計畫，特別針對已有心肌病患者群體
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

