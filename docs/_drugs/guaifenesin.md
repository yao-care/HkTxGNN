---
layout: default
title: Guaifenesin
parent: 高證據等級 (L1-L2)
nav_order: 363
evidence_level: L2
indication_count: 5
---

# Guaifenesin
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

根據 Evidence Pack，Guaifenesin 屬於呼吸道藥物（非抗腫瘤），安全性資料皆為 Data Gap，香港無上市許可。以下依格式輸出報告：

---

# Guaifenesin：從祛痰到鼻腔疾病

## 一句話總結

Guaifenesin（愈創甘油醚）是廣泛使用的祛痰劑，藉由稀釋黏液促進呼吸道分泌物排出。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 呼吸道黏液過多、祛痰（OTC 祛痰劑） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的藥物作用機轉資料（MOA Data Gap）。根據已知資訊，Guaifenesin 是廣泛使用的 OTC 祛痰劑，其作用方式為增加呼吸道黏膜分泌液量、降低黏液黏稠度，進而促進黏液引流與黏膜纖毛清除（mucociliary clearance）。

鼻腔疾病（如慢性鼻炎、鼻竇炎）的核心病理之一為鼻腔黏液滯留與引流障礙。Guaifenesin 的稀化黏液機轉可直接對應這一症狀需求——促進鼻腔分泌物液化排出，緩解鼻塞與鼻腔壓力感，具備清楚的藥理合理性。

原本用於下呼吸道（支氣管、肺部）的祛痰機轉，同樣適用於上呼吸道（鼻腔、副鼻竇），因兩者共享黏液分泌系統與纖毛清除機制。文獻中也提到 Guaifenesin 合併去充血劑可用於過敏性呼吸道病患，進一步支持此跨解剖部位的延伸應用。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | 已完成 | 30 | 14 天隨機雙盲安慰劑對照試驗，研究口服 Guaifenesin 對 7–18 歲兒童慢性鼻炎的療效，以 SN-5 評分表及鼻道容積評估症狀改善 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | 臨床回顧 | Am J Rhinology | 22 例囊性纖維化成人慢性鼻竇炎管理經驗回顧，探討手術與藥物治療策略 |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | 臨床回顧 | Logopedics Phoniatrics Vocology | 過敏性聲音患者治療策略，指出 Guaifenesin 合併去充血劑可能有助於減少鼻腔分泌物對聲帶的影響 |

---

## 香港上市資訊

Guaifenesin 目前在香港**無藥物許可證登記**，市場狀態為未上市。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 1 個針對鼻腔疾病（兒童慢性鼻炎）的已完成 Phase 2 隨機對照試驗，藥理機轉合理，且 Guaifenesin 為長期使用的 OTC 藥物，整體安全性輪廓成熟，具備推進研究的基礎條件。唯香港無現行許可證，需先確認法規路徑。

**若要推進需要：**
- 取得 NCT01364467 完整發表結果（確認療效數據與統計顯著性）
- 補充 DrugBank MOA 資料，強化機轉連結論述
- 從 TFDA/官方仿單取得完整安全性警語與禁忌資料
- 評估香港 PHARMAC 或 Department of Health 的藥物登記可行性
- 考慮擴展至成人族群的 Phase 2 研究設計
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

