---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ifosfamide：預測新適應症為女性乳癌 (female breast carcinoma)（證據等級 L5）。原適應症：資料未登載"
monitor_inn: "IFOSFAMIDE"
predicted_indications: ["female breast carcinoma", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts"]
---

# Ifosfamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ifosfamide：從（原適應症未登載）到女性乳癌

## 一句話總結

Ifosfamide（異環磷醯胺）是一種烷化劑類抗癌藥物，香港目前有 4 張有效許可證，但本報告所用資料未登載許可證的核准適應症文字。
TxGNN 模型預測它可能對**女性乳癌 (female breast carcinoma)** 有效，目前有 **6 個臨床試驗**和 **20 篇文獻**與此方向相關，其中只有 1 個試驗直接檢驗 ifosfamide 用於乳癌。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未登載（香港許可證未列核准適應症文字） |
| 預測新適應症 | 女性乳癌 (female breast carcinoma) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L2（依本報告資料編譯的評等；見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

證據等級說明：6 個試驗皆為 Phase 1/2，沒有已完成的 Phase 3 RCT。多數試驗是含 ifosfamide 的合併療法，無法單獨評估其貢獻。另有數項 Phase 2 研究與回顧文獻。嚴格依判定規則，此為 L2 至 L3 之間，這裡採用資料編譯時的 L2 評等，解讀時宜保守。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記錄。不過依文獻，ifosfamide 是烷化劑前驅藥，需經肝臟 CYP450（CYP3A4／CYP2B6）活化為 isophosphoramide mustard，與 DNA 形成交聯，誘發增生中腫瘤細胞凋亡。它是 cyclophosphamide 的類似物，已知對多種腫瘤有活性，包括軟組織肉瘤和睪丸癌。

在乳癌方面，文獻顯示單一藥物用於已治療過的患者，反應率約 7–30%。與 docetaxel、vinorelbine、mitoxantrone、paclitaxel、etoposide 等合併使用的 Phase 2 研究，報告了更具吸引力的反應率。加上 mesna 後，主要劑量限制毒性（泌尿道毒性）已大幅減輕。另有研究在乳癌組織中偵測到 CYP3A4、CYP2C9、CYP2B6 的表現，提示腫瘤內可能有局部活化。

機轉上它最可能適用於化療難治型、化生型（metaplastic）或肉瘤樣乳癌亞型，例如惡性葉狀腫瘤與乳房血管肉瘤。標準乳癌療法對這些亞型效果有限。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | 未知 | 42 | Docetaxel + ifosfamide 作為轉移性乳癌第一線化療（直接相關，無隨機對照） |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | 未知 | 未報告 | 多週期高劑量化療 vs 優化常規劑量化療用於轉移性乳癌（ifosfamide 可能為方案一部分） |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | 完成 | 33 | 高劑量 cisplatin、cyclophosphamide、etoposide、ifosfamide 等序貫療法加幹細胞支持，提供可行性與安全性資料 |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 終止 | 未報告 | 高劑量 topotecan、ifosfamide/mesna、etoposide（TIME）加自體幹細胞移植，終止且人數未報告 |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | 終止 | 12 | Samarium-153 併雙次自體骨髓移植，ifosfamide 為背景成分 |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | 終止 | 7 | 幹細胞移植後活化 T 細胞治療，ifosfamide 非試驗變項 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Cohort | Current Problems in Cancer | 化生型乳癌使用含 ifosfamide 化療的經驗 |
| [39074497](https://pubmed.ncbi.nlm.nih.gov/39074497/) | 2024 | Cohort | JNCCN | 惡性葉狀腫瘤輔助化療對長期預後的影響（傾向分數配對） |
| [14586149](https://pubmed.ncbi.nlm.nih.gov/14586149/) | 2003 | Review | Oncology | 晚期乳癌使用 ifosfamide：單藥反應率 7–30%，合併療法反應率更高 |
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | Cancer | Paclitaxel 24 小時輸注加 ifosfamide 用於蒽環類抗藥轉移性乳癌 |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 | J Clin Oncol | Ifosfamide + vinorelbine 作為轉移性乳癌第一線化療 |
| [8445421](https://pubmed.ncbi.nlm.nih.gov/8445421/) | 1993 | Phase 2 | J Clin Oncol | Ifosfamide + mitoxantrone 作為轉移性乳癌第一線化療 |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 | Tumori | Ifosfamide + etoposide 用於曾接受治療的晚期乳癌 |
| [1390313](https://pubmed.ncbi.nlm.nih.gov/1390313/) | 1992 | 回顧 | Ann Oncol | Ifosfamide 單藥乳癌研究約 20% 客觀反應，略優於 cyclophosphamide |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Review | Drugs | Ifosfamide/mesna 的抗腫瘤活性、藥動學與療效回顧 |
| [3286879](https://pubmed.ncbi.nlm.nih.gov/3286879/) | 1988 | Review | J Natl Cancer Inst | Ifosfamide 綜述，在軟組織肉瘤和睪丸癌有顯著活性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64831 | IFO-CELL N 1000 SOLUTION FOR INFUSION 1000MG | 未登載 | 未登載 |
| HK-61271 | IFOSFAMIDE POWDER FOR SOLUTION FOR INFUSION 1G (QILU HAINAN) | 未登載 | 未登載 |
| HK-01322 | HOLOXAN INJ IV | 未登載 | 未登載 |
| HK-50758 | ISOXAN FOR INJ 1000MG | 未登載 | 未登載 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氮芥類烷化劑，oxazaphosphorine） |
| 骨髓抑制風險 | 高（相關資料顯示可有白血球減少、貧血、血小板減少） |
| 致吐性分級 | 中至高（依藥物類別與劑量而異） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質（含血鉀）、尿液檢查（血尿） |
| 處置防護 | 需依細胞毒性藥物處置規範操作；常需併用 mesna 作泌尿道保護 |

詳細警語請參考原廠仿單。

## 安全性考量

- **知識圖譜標示的潛在禁忌／風險疾病**（來自藥物－疾病關聯，並非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、白血球低下、貧血（含巨球性貧血）、低血鉀、高膽紅素血症（含 Gilbert 症候群）、腎小管酸中毒、Fanconi 腎小管症候群、膿輸尿管。
- **藥物交互作用**：共查得 100 筆，以下為部分中度交互作用：
  - Amphotericin B（含脂質複合物劑型）
  - Aprepitant
  - Bupropion
  - Morphine
  - Metoclopramide
  - Kanamycin、Neomycin
  - 降血糖藥（Chlorpropamide、Glimepiride、Glipizide、Glyburide、Nateglinide、Repaglinide、Tolazamide、Acetohexamide）
  - Dronabinol、Nabilone、Scopolamine
  - 輕度：Levofloxacin

香港仿單的警語與禁忌尚未取得，詳細資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乳癌有多項 Phase 2 研究與文獻顯示 ifosfamide 具活性，TxGNN 分數很高（99.91%）。
- 但缺乏已完成的 Phase 3 RCT，多數證據是合併療法，且安全性資料有缺口，不宜直接推進。

**若要推進需要：**
- 取得香港仿單（警語、禁忌、核准適應症），這是目前阻擋安全篩查的資料缺口。
- 補齊詳細的作用機轉資料。
- 優先聚焦在難治型或特殊亞型（化生型乳癌、惡性葉狀腫瘤、乳房血管肉瘤），設計前瞻性研究。
- 建立骨髓抑制、腎毒性、神經毒性與泌尿道毒性的監測計畫，並評估與其他藥物的交互作用。

## 其他預測適應症（不建議推進）

其他排名靠前的預測均無足夠證據，建議 **Hold**：

- **未分類骨髓增生異常症候群、5q 部分缺失、兒童難治性血球減少症**：多數僅有模型預測。烷化劑本身可引起治療相關 MDS，且骨髓抑制在骨髓衰竭疾病中風險高。兒童難治性血球減少症關聯的試驗，是處理 ifosfamide 所致的血小板低下，並非支持其療效。
- **先天性低色素性貧血伴環狀鐵粒幼細胞**：無證據，且屬非惡性疾病，細胞毒性烷化劑缺乏合理的機轉，預測可能為網路關聯造成的假訊號。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

