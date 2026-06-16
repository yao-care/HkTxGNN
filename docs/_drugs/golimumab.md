---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 5
---

# Golimumab
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

# Golimumab：從類風濕性關節炎到類風濕性血管炎

## 一句話總結

Golimumab 是一種全人類化抗 TNF-α 單株抗體，全球已核准用於類風濕性關節炎、銀屑病關節炎及強直性脊椎炎的治療，惟在香港尚未上市。
TxGNN 模型預測它可能對**類風濕性血管炎 (Rheumatoid Vasculitis)** 有效，
目前有 **3 個臨床試驗**（均為間接相關）和 **6 篇文獻**提供背景支持，直接疾病特異性證據仍缺乏。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 全球核准適應症包含類風濕性關節炎、銀屑病關節炎、強直性脊椎炎（香港無許可證資料） |
| 預測新適應症 | 類風濕性血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L4（機轉推論 + 間接觀察研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Golimumab 為全人類化 IgG1κ 抗 TNF-α 單株抗體，透過直接中和可溶性及跨膜型 TNF-α，阻斷其與 TNF 受體（TNFR1/TNFR2）的結合，進而抑制下游 NF-κB 活化及促炎細胞因子瀑布。其抗 TNF-α 機轉已在全球多個已核准適應症的 Phase 3 RCT 中獲得充分驗證，詳細作用機轉文件目前尚待補充（MOA 資料 gap）。

類風濕性血管炎（Rheumatoid Vasculitis）是 RA 的嚴重關節外表現，見於長期血清反應陽性患者，病理核心為免疫複合物沉積於血管壁、中性球浸潤以及 TNF-α 介導的血管內皮損傷。由於 TNF-α 是此炎症過程的關鍵驅動因子，機轉上 Golimumab 抑制 TNF-α 應可降低血管炎的炎症驅力，具有生物學合理性。

文獻指出，自抗 TNF 生物製劑廣泛應用於 RA 治療後，類風濕性血管炎的臨床發生率已顯著下降（PMID 29075910）。此流行病學趨勢間接支持 TNF-α 抑制在預防或緩解此疾病中的潛在作用。然而，現有試驗均以 RA 整體族群為標的，目前仍無針對類風濕性血管炎的直接介入性試驗，機轉連結合理但缺乏疾病特異性臨床驗證。

---

## 臨床試驗證據

> ⚠️ 以下試驗均非直接針對類風濕性血管炎，為相關背景間接證據（均評級 C）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 已完成 | 184 | 多國多中心觀察性研究，評估 Tocilizumab 在 DMARD 或 biologics 反應不足的 RA 患者中的療效與安全性，未特別分析 vasculitis 次族群，僅提供 biologics 在 RA 真實世界使用的背景參考 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750,000 | 大型回顧性流行病學研究，評估使用 biologics 及免疫抑制劑的 IMID 患者新發其他 IMID 的風險，研究設計為安全性監測導向，與 vasculitis 治療療效無直接相關 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 評估風濕病患者（使用免疫抑制劑）接受全肩關節置換術前後的停藥管理策略，屬圍手術期藥物管理研究，與 vasculitis 治療目標無關聯 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-Analysis | Int J Mol Sci | 5 種 TNFi 含 Golimumab 在 RA 關節破壞抑制效果相當，支持 Golimumab 在 RA 中的整體療效定位 |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | 生物製劑在風濕性疾病中的最新進展，涵蓋抗 TNF 機轉、療效與安全性，含抗 TNF 對 RA 關節外表現的影響討論 |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatology Int | RA 患者使用 Golimumab 期間出現壞疽性膿皮病合併敗血症，文中明確指出生物製劑問世後類風濕性血管炎發生率已下降，間接支持抗 TNF 對 vasculitis 的保護效應 |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report ×2 | Joint Bone Spine | 2 例 Takayasu 動脈炎患者在抗 TNF 治療期間出現病情，提示 TNF-α 抑制對大血管炎的效應複雜，不排除誘發效應 |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocular Immunol Inflamm | Golimumab 成功治療頑治型白塞氏病相關葡萄膜炎（一種血管炎相關免疫疾病），展示其在血管炎相關疾病的 off-label 潛力 |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Retrospective Cohort | Semin Arthritis Rheum | RA 患者末期腎病的頻率、病因及治療研究，涵蓋腎臟血管炎相關討論，提供 RA 系統性血管受累的背景資料 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：本 Evidence Pack 中警語、禁忌症及藥物交互作用資料均標記為 Data Gap，建議於推進評估前向香港衛生署查詢或取得 Simponi®（Golimumab）原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有針對類風濕性血管炎的直接臨床試驗完全缺乏，現有 3 個試驗均為相關背景性間接研究（評級 C），6 篇文獻中最高等級為 Network Meta-Analysis（但並非針對 vasculitis）。整體證據等級僅達 L4，不足以支持進一步的臨床推進。此外，Golimumab 在香港完全未上市（0 張許可證），市場准入障礙顯著，應先解決市場准入問題。

值得注意的是，本次 TxGNN 預測中另有兩個適應症具備 **L1 等級證據**並建議 **Proceed with Guardrails**：**發炎性脊椎病（Inflammatory Spondylopathy，rank 3，NCT01453725 等多項已完成 Phase 3 RCT）**及**多關節型幼年特發性關節炎（Polyarticular JIA，rank 5，FDA 已於 2020 年核准 IV 劑型）**，建議優先評估這兩個候選適應症。

**若要推進類風濕性血管炎方向需要：**
- 確認 Golimumab（Simponi®）在香港的市場准入途徑（進口許可或特殊用藥申請）
- 向 DrugBank 或原廠取得完整 MOA 及安全性資料（警語、禁忌、藥物交互作用）
- 進行類風濕性血管炎亞族群的系統性文獻回顧，確認抗 TNF 治療的直接療效證據
- 若考慮設計研究：規劃 RA 血管炎患者使用 Golimumab 的觀察性登錄或病例系列研究
- 與香港風濕科專家討論 vasculitis 亞族群識別的可行性及臨床需求
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

