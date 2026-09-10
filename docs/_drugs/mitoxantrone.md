---
layout: default
title: Mitoxantrone
parent: 高證據等級 (L1-L2)
nav_order: 504
evidence_level: L2
indication_count: 5
---

# Mitoxantrone
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

# Mitoxantrone（米托蒽醌）：從乳癌/血液腫瘤到上呼吸消化道腫瘤

## 一句話總結

Mitoxantrone 是蒽醌類（anthracenedione）細胞毒性化療藥物，文獻記載原用於**乳癌、急性白血病、非何杰金氏淋巴瘤**等血液及實體腫瘤治療。
TxGNN 模型預測它可能對**上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm)** 有效，
目前有 **1 個 Phase 3 臨床試驗**和 **10+ 篇相關文獻**支持這個方向。

> ⚠️ 本藥目前在香港**未上市**（0 張許可證），且仿單警語/禁忌症資料為阻斷性缺口（DG001），尚無法完成 S1 安全性初評。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳癌、急性白血病、非何杰金氏淋巴瘤（依文獻紀錄，香港無許可證資料可查） |
| 預測新適應症 | 上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm) |
| TxGNN 預測分數 | 99.78%（排名 4985） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

DrugBank 的正式 MOA 欄位標記為資料缺口（DG002），但依已發表文獻（PMID 3512224、3327453）與本次預測的機轉推論，Mitoxantrone 為蒽醌類似物，透過**嵌入 DNA 並抑制 Topoisomerase II**，造成 DNA 雙股斷裂，機轉與 doxorubicin 等蒽環類藥物相似，對快速分裂的上皮性及淋巴性腫瘤細胞具廣譜細胞毒性。

原適應症（乳癌、白血病、淋巴瘤）與新預測適應症「上呼吸消化道腫瘤」表面上器官系統不同，但實際上該分類涵蓋鼻咽癌、唾液腺惡性腫瘤、頭頸部鱗狀細胞癌、腺樣囊性癌，以及鼻型結外 NK/T 細胞淋巴瘤——後者本質上仍是淋巴性腫瘤，與原適應症機轉高度重疊。

更關鍵的是，米托蒽醌脂質體劑型（鹽酸米托蒽醌脂質體）**已是** NK/T 細胞淋巴瘤現行含藥方案（P-GEMD）之核心成分之一，且過去已有多項 Phase 1/2 試驗直接測試 mitoxantrone 於鼻咽癌、唾液腺癌、頭頸鱗狀細胞癌、腺樣囊性癌的療效，顯示這個預測並非全新推論，而是有臨床先例支持的機轉延伸。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Phase 3 | 尚未招募 | 60 | 比較 P-GEMD（含米托蒽醌脂質體）與 P-Gemox 方案，治療新診斷早期非上呼吸消化道型或晚期結外 NK/T 細胞淋巴瘤；尚無療效數據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Phase 1b 臨床試驗 | Oral Oncology | 米托蒽醌脂質體(PLM60)治療復發/轉移性頭頸鱗狀細胞癌，評估安全性與療效 |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase 2 試驗 | Anti-Cancer Drugs | Mitoxantrone + cisplatin 治療復發/轉移性唾液腺惡性腫瘤，14 例 |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase 2 試驗 | Anti-Cancer Drugs | Ifosfamide + mitoxantrone 治療復發/轉移性頭頸部鱗狀細胞癌，22 例 |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase 2 試驗 | Ann Oncol | EORTC 頭頸癌合作組：mitoxantrone 用於腺樣囊性癌 |
| [11269736](https://pubmed.ncbi.nlm.nih.gov/11269736/) | 2001 | Phase 1 試驗 | Cancer Chemother Pharmacol | Mitoxantrone + raltitrexed + LFA + 5-FU 用於晚期實體瘤（含頭頸癌） |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | 系統性回顧 | Bull Cancer | 頭頸部腺樣囊性癌全身性治療系統性回顧 |
| [1735075](https://pubmed.ncbi.nlm.nih.gov/1735075/) | 1992 | PK/PD 臨床研究 | Cancer | Mitoxantrone 於鼻咽癌病人之藥物動力學/藥效學研究，15 例 |
| [3512224](https://pubmed.ncbi.nlm.nih.gov/3512224/) | 1986 | 回顧文獻 | Drug Intell Clin Pharm | Mitoxantrone 機轉與活性回顧，提及頭頸癌部分反應 |
| [1985750](https://pubmed.ncbi.nlm.nih.gov/1985750/) | 1991 | 病例系列 | Cancer | Mitoxantrone 併用放療治療甲狀腺未分化巨細胞癌 |
| [39472118](https://pubmed.ncbi.nlm.nih.gov/39472118/) | 2024 | 前瞻對照研究 | 中華耳鼻咽喉頭頸外科雜誌 | Mitoxantrone 作為顯影劑用於甲狀腺癌根除術淋巴結顯影（非治療用途） |

## 香港上市資訊

目前 Mitoxantrone 在香港**未取得任何藥品許可證**（0 張），無法提供本地核准適應症與劑型資訊。

## 其他預測適應症（次要候選，未深入分析）

| 排序 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 2 | Small cell lung carcinoma | 99.43% | L3 | S1 | Research Question |
| 3 | Primary pulmonary lymphoma | 99.41% | L3 | S1 | Research Question |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | 99.37% | L5 | S0 | Hold |
| 5 | Pulmonary blastoma | 99.35% | L5 | S0 | Hold |

排序 2、3 僅有間接或小型回溯性證據（如已終止的脂質體 mitoxantrone Phase 2 試驗、單篇肺 MALT 淋巴瘤病例系列）；排序 4、5 僅有模型預測分數，無任何臨床試驗或文獻佐證，暫不建議推進。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蒽醌類 Anthracenedione，Topoisomerase II 抑制劑，機轉類似 doxorubicin） |
| 骨髓抑制風險 | 中至高（同類蒽環/蒽醌藥物常見嗜中性白血球減少，但無本產品本地毒性數據） |
| 致吐性分級 | 低至中度（依藥物類別一般分類） |
| 監測項目 | CBC（含白血球分類）、肝功能、左心室射血分數（LVEF，蒽醌類藥物有心臟毒性風險）、尿液變色（藍綠色為已知現象） |
| 處置防護 | 需依細胞毒性藥物處置規範操作（DNA 嵌入型抗腫瘤劑） |

## 安全性考量

安全性資訊請參考原廠仿單。（主要警語、禁忌症與 DDI 資料目前皆為資料缺口，其中仿單警語/禁忌症為阻斷性缺口 DG001，尚無法完成 S1 安全性初評）

## 結論與下一步

**決策：Proceed with Guardrails**（針對排序 1：上呼吸消化道腫瘤）

**理由：**
- 有 1 項 Phase 3 NK/T 細胞淋巴瘤試驗（含米托蒽醌脂質體核心成分）及多項頭頸部/鼻咽癌/唾液腺癌 Phase 1/2 歷史證據支持機轉合理性，證據等級達 L2；但關鍵試驗尚未招募，且香港本地無許可證與安全性資料。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，阻斷性缺口，優先處理）
- 補充完整 DrugBank 作用機轉資料（DG002）
- 追蹤 NCT06953739 招募進度與期中數據
- 評估香港藥品許可證申請可行性（目前 0 張許可證，未上市）
- 排序 2-5 之次要預測適應症證據不足，暫列 Hold / Research Question，待更多資料出現後再評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

