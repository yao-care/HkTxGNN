---
layout: default
title: Choline Salicylate
parent: 中證據等級 (L3-L4)
nav_order: 135
evidence_level: L4
indication_count: 10
---

# Choline Salicylate
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Choline Salicylate：從止痛消炎到類風濕性關節炎

## 一句話總結

Choline Salicylate 是一種非乙醯化水楊酸鹽（NSAIDs 類），屬止痛消炎藥物類別，台灣目前未上市。
TxGNN 模型共預測 10 個潛在新適應症；其中**類風濕性關節炎 (Rheumatoid Arthritis)** 具最佳現有文獻支持，
目前有 **0 個臨床試驗**和 **4 篇文獻**（均為 1977–1986 年早期臨床報告）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消炎止痛（水楊酸鹽類藥物；官方仿單資料尚待取得） |
| 主要預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis)（最佳證據等級） |
| TxGNN 預測分數 | 99.82%（排名第 2；排名第 1 為 Prinzmetal Angina 99.84%，但無支持文獻） |
| 證據等級 | L4 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 預測適應症總覽

本次 Evidence Pack 涵蓋 10 個 TxGNN 預測適應症，彙整如下：

| 排名 | 適應症 | TxGNN 分數 | 有效臨床試驗 | 文獻 | 證據等級 | 機轉方向 | 建議 |
|------|--------|------------|-------------|------|---------|---------|------|
| 1 | Prinzmetal Angina（變異性心絞痛） | 99.84% | 0 | 0 | L5 | 不利（PGI2 被抑制） | Hold |
| **2** | **Rheumatoid Arthritis（類風濕性關節炎）** | **99.82%** | **0** | **4** | **L4** | **部分支持** | **Research Question** |
| 3 | Hypertensive Disorder（高血壓症） | 99.81% | 0 ¹ | 0 | L5 | 不利（腎臟 PGE2 抑制） | Hold |
| **4** | **Migraine Disorder（偏頭痛）** | **99.80%** | **1** ² | **0** | **L4** | **間接支持（class effect）** | **Research Question** |
| 5 | 肺高壓（低氧/肺病） | 99.77% | 0 | 0 ³ | L5 | 不利（抑制 PGI2） | Hold |
| 6 | 肺高壓（多因素不明） | 99.77% | 0 | 0 | L5 | 不利 | Hold |
| 7 | Malignant Renovascular Hypertension | 99.77% | 0 | 0 | L5 | 明確負向（腎缺血加重） | Hold |
| 8 | Malignant Hypertensive Renal Disease | 99.77% | 0 | 0 | L5 | 明確負向（腎毒性風險） | Hold |
| 9 | Raynaud Disease（雷諾氏病） | 99.76% | 0 | 0 | L5 | 薄弱 | Hold |
| 10 | Pulmonary Hypertension（肺動脈高壓） | 99.75% | 0 ¹ | 0 | L5 | 不利 | Hold |

> ¹ 檢索到的臨床試驗與 choline salicylate 或目標適應症無直接關聯（關鍵字誤匹）
> ² 膽鹼能機轉相關試驗（NCT00564408，Grade B），但規模極小（12 人），無法確認直接效益
> ³ 20 篇文獻均為一般低氧機轉研究，與 choline salicylate 治療無關

---

## 為什麼類風濕性關節炎預測合理？

目前缺乏 Choline Salicylate 的官方作用機轉資料（DrugBank MOA 欄位尚未取得）。根據藥物類別知識，Choline Salicylate 為非乙醯化水楊酸鹽，透過可逆性抑制環氧化酶（COX-1/COX-2），減少前列腺素（特別是 PGE2）合成，從而發揮消炎、止痛及退燒效果。相較乙醯水楊酸（aspirin）的不可逆 COX 抑制，非乙醯化形式對胃腸道及血小板的影響理論上較輕。

在類風濕性關節炎方面，PGE2 是驅動滑膜炎症反應的重要媒介，能促進關節腫脹、疼痛及滑膜增生。COX 抑制藥物透過降低 PGE2 合成，可緩解 RA 的炎症症狀，具有明確的藥理基礎連結。

然而，現代 RA 治療標準（ACR/EULAR 指引）已以甲胺蝶呤（MTX）搭配生物製劑為主流，水楊酸鹽類藥物僅在 1970–80 年代 DMARDs 問世前作為第一線選項使用，目前臨床定位已大幅退縮。TxGNN 的預測可能反映的是歷史用途的知識圖譜連結，而非現代的再利用機會。

---

## 臨床試驗證據

類風濕性關節炎方向目前**無相關臨床試驗登記**。

**偏頭痛方向參考**（Research Question 等級，供背景參考）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00564408](https://clinicaltrials.gov/study/NCT00564408) | N/A | 完成 | 12 | 探索乙醯膽鹼類似物（carbachol）對頭痛及腦血管的影響；choline salicylate 之膽鹼成分可能涉及膽鹼能神經調控，與機轉部分吻合，但規模極小（Grade B） |
| [NCT04220606](https://clinicaltrials.gov/study/NCT04220606) | N/A | 完成 | 39 | 偏頭痛樣發作期間腦部麩胺酸濃度 MRS 測量（基礎機轉研究，無藥物干預，Grade C） |
| [NCT04256837](https://clinicaltrials.gov/study/NCT04256837) | N/A | 已終止 | 47 | 腎移植患者耳廓迷走神經電刺激研究，與偏頭痛藥物治療無直接關聯（Grade C） |

---

## 文獻證據（類風濕性關節炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [897386](https://pubmed.ncbi.nlm.nih.gov/897386/) | 1977 | 臨床觀察 | Reumatologia | Choline salicylate 用於兒童類風濕性關節炎治療的臨床效益報告 |
| [7188920](https://pubmed.ncbi.nlm.nih.gov/7188920/) | 1980 | 臨床報告 | Fysiatr Reumatol Vestn | Choline salicylate 作為抗風濕藥物的使用報告 |
| [377958](https://pubmed.ncbi.nlm.nih.gov/377958/) | 1979 | 敘述性回顧 | Am J Hosp Pharm | 抗風濕藥物綜述，涵蓋 choline salicylate 在 RA 的抗炎用途及比較 |
| [3740556](https://pubmed.ncbi.nlm.nih.gov/3740556/) | 1986 | 案例報告 | Ann Allergy | RA 患者對非乙醯化水楊酸（choline magnesium trisalicylate）的過敏反應案例，提示交叉敏感性風險 |

> **注意**：全部 4 篇文獻均為 1986 年前發表的第三類臨床研究（臨床觀察、綜述、案例報告），缺乏現代 RCT 設計；其中一篇具安全性警示意義（藥物敏感性反應）。

---

## 台灣上市資訊

Choline Salicylate 在台灣目前**未上市**，無任何藥品許可證登記資料，無法進行許可證比對。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **資料缺口提示（阻斷性）**：本次 Evidence Pack 未能取得 TFDA 仿單警語與禁忌症（資料缺口 DG001，阻斷性），尚無法進入 Stage 1 安全性初評。
>
> 根據水楊酸鹽類藥物的已知類別安全性，應特別注意以下方向（須以正式仿單資料確認）：
> - 哮喘、鼻瘜肉患者可能對非乙醯化水楊酸有交叉敏感性（參見 PMID 3740556）
> - NSAIDs 類對腎功能的影響及與 ACE 抑制劑、利尿劑的交互作用
> - 與抗凝藥物（如 warfarin）的潛在交互作用

---

## 結論與下一步

**決策：Research Question（類風濕性關節炎、偏頭痛）；Hold（其餘 8 個適應症）**

**理由：**
類風濕性關節炎方向具有藥理學上的合理性（COX 抑制 → PGE2 降低 → 滑膜炎症緩解），並有 4 篇早期臨床觀察文獻支持歷史使用，但所有文獻均為 1977–1986 年第三類證據，缺乏現代 RCT。現代 RA 治療標準已由 MTX + 生物製劑主導，水楊酸鹽類的再利用空間極為有限。各類高血壓及肺高壓適應症機轉方向不利（NSAIDs 可加重腎血流不足、抑制保護性 PGI2），不建議推進。

**若要推進需要：**

1. **（必要，優先）** 取得 TFDA 仿單警語與禁忌症（DG001）—阻斷性缺口，完成前無法進入正式安全性評估
2. **（必要）** 查詢 DrugBank 完整 MOA 資料（DG002）以強化機轉分析
3. 評估現代 RA 指引中是否仍有水楊酸鹽類輔助消炎的利基（例如：MTX 不耐受患者、老年患者短期消炎）
4. 評估偏頭痛方向的 class effect 假設是否值得設計新研究（考量 aspirin 已有 IHS Grade A 推薦）
5. 台灣藥品許可證申請可行性分析（目前 0 張許可證，須評估法規路徑）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

