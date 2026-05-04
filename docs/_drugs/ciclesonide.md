---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide：從哮喘到異位性濕疹

## 一句話總結

Ciclesonide（西克松奈德）是一種吸入型皮質類固醇（ICS），在全球（FDA/EMA）已核准用於持續性哮喘的維持治療，但在香港目前尚未取得上市許可。TxGNN 模型預測它可能對**異位性濕疹 (Atopic Eczema)** 有效，預測分數高達 **99.96%**，然而目前**無臨床試驗**及**無文獻**直接支持此再利用方向，證據仍停留在純粹模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 哮喘（FDA/EMA 已核准，香港未上市） |
| 預測新適應症 | 異位性濕疹 (Atopic Eczema) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Ciclesonide 的詳細作用機轉資料（MOA 資料缺口）。根據已知藥理資訊，Ciclesonide 為前驅藥（prodrug），吸入後在肺部經酯酶活化為具活性的 des-ciclesonide，具高度肺部局部選擇性，全身性副作用（如 HPA 軸抑制、生長抑制）顯著低於老一代 ICS。其核心機轉為皮質類固醇抗炎效應：抑制嗜酸性粒細胞浸潤、減少促炎細胞激素（如 IL-4、IL-5、IL-13）釋放，進而控制過敏性炎症反應。

皮質類固醇藥物類別（glucocorticoids）確實對異位性濕疹有效，局部外用型皮質類固醇（如 mometasone furoate、betamethasone、hydrocortisone 等）正是異位性濕疹的第一線標準治療。TxGNN 的高分預測反映的是**皮質類固醇類別層級（corticosteroid class）**的抗炎效應泛化，而非 Ciclesonide 本身對皮膚疾病的特異性證據。

然而，Ciclesonide 目前僅有**吸入劑型**（定量吸入器 MDI），專為肺部局部沉積而設計，**並無皮膚外用劑型**。將吸入型 ICS 應用於皮膚疾病缺乏臨床給藥途徑的合理性；若要探索 Ciclesonide 用於異位性濕疹，需進行全新外用劑型開發，已超出標準藥物再利用框架的範疇。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Ciclesonide 在香港目前無任何核准上市的藥品許可證（共 0 張），在研究進展前須另行評估上市申請途徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 補充：本次 Evidence Pack 全部預測適應症總覽

本次共有 6 個預測適應症，以下提供完整研究視角：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 | 備註 |
|------|--------|-----------|---------|------|------|
| 1 | 異位性濕疹 (Atopic Eczema) | 99.96% | L5 | Hold | 劑型不相符（吸入型 vs. 外用型） |
| 2 | 2-HEMA 致敏 | 99.76% | L5 | Hold | 無直接治療機轉依據 |
| 3 | 異位性皮膚炎 (Atopic Dermatitis) | 99.73% | L5 | Hold | 與排名 1 為同一疾病實體 |
| 4 | 支氣管炎 (Bronchitis) | 99.70% | L4 | Research Question | 有間接 COPD 指引文獻，慢性型具生物合理性 |
| 5 | 接觸性皮膚炎 (Contact Dermatitis) | 99.25% | L4 | Hold | 唯一文獻為**負向安全性報告**：Ciclesonide 本身為致敏原 |
| **6** | **哮喘 (Asthma-related traits)** | **99.13%** | **L1** | **Proceed with Guardrails** | **實為現有核准適應症，非再利用方向** |

> ⚠️ **重要提示**：排名第 6 的哮喘（L1 等級）是 Ciclesonide（Alvesco®）已獲 FDA/EMA 核准的現有適應症，有多項 Phase 3 RCT（MAESTRO 系列）支持，並非真正的「老藥新用」候選。排名第 4 的支氣管炎/COPD 具備較實際的再利用探索價值，建議優先評估。
>
> ⚠️ 接觸性皮膚炎（排名 5）的唯一文獻（[PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)）為 Case Report，描述 Ciclesonide 作為致敏原引發全身性過敏性皮膚炎，提示安全性風險而非療效。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 對異位性濕疹的高分預測源於皮質類固醇類別效應的廣義泛化，而非 Ciclesonide 的特異性皮膚治療證據。Ciclesonide 為吸入劑型，與皮膚疾病所需的局部外用給藥途徑根本不相符，目前亦無任何臨床試驗或文獻支持此再利用方向，維持 Hold 決策。

**若要推進需要：**
- **優先評估替代方向**：支氣管炎/COPD（排名 4，L4，有間接文獻支持，ICS 在 COPD 維持治療具既定地位）
- 補充 Ciclesonide 作用機轉（MOA）詳細資料（建議查詢 DrugBank API 解決 DG002 資料缺口）
- 確認 Ciclesonide 是否有外用劑型的早期開發研究（若堅持皮膚適應症方向）
- 確認香港上市申請可行性（目前 0 張許可證，需評估 HKDH 申請途徑）
- 排除安全性疑慮：接觸性皮膚炎文獻顯示 Ciclesonide 有交叉致敏風險，需在任何適應症探索前完整評估安全性仿單（解決 DG001 資料缺口）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

