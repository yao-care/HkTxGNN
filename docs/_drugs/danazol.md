---
layout: default
title: Danazol
parent: 高證據等級 (L1-L2)
nav_order: 174
evidence_level: L2
indication_count: 10
---

# Danazol
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

# Danazol：從子宮內膜異位症到閉經

## 一句話總結

Danazol 是一種合成類固醇（17α-乙炔睪酮衍生物），美國 FDA 已核准用於子宮內膜異位症、纖維囊腫性乳房疾病及遺傳性血管水腫。
TxGNN 模型預測它可能對**閉經（Amenorrhea）** 具有直接治療價值，
目前有 **20 篇文獻**支持這個方向，包含 **2 篇 RCT** 及 **1 篇系統性回顧**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 子宮內膜異位症（FDA 核准；香港無許可證） |
| 預測新適應症 | 閉經（Amenorrhea） |
| TxGNN 預測分數 | 99.9995% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Danazol 的藥理機轉在文獻中有相當清晰的描述（雖然本次 Evidence Pack 缺乏仿單原始 MOA 資料）。Danazol 藉由**抑制垂體 LH/FSH 脈衝分泌**（抗促性腺激素效應），並直接拮抗子宮內膜的雌激素與孕激素受體，造成卵巢功能抑制與子宮內膜萎縮，從而誘發閉經。

閉經在此脈絡下**並非副作用，而是明確且可預期的主要療效終點**。多項 RCT（PMID 2140996, 2523321）已將「amenorrhea 誘導率」列為核心評估指標，用於比較 Danazol 與 GnRH 類似物、gestrinone 等藥物的療效。此外，子宮內膜異位症的病理基礎正是「雌激素依賴性病變在閉經或停經狀態下退化消退」（PMID 16280355），機轉高度一致。

近年更有多中心回顧性研究（PMID 39051650, 2024）直接評估 Danazol 用於跨性別及非二元性別個體的月經抑制，進一步確認其誘導閉經的臨床應用潛力超越原適應症範疇，預測生物學合理性高。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 及 ICTRP 均無 Danazol 合併閉經的已登記試驗）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | RCT | Fertility and Sterility | Nafarelin 400 µg/d vs. Danazol 600 mg/d 雙盲 RCT（n=82）：兩者均使活動性子宮內膜異位病變顯著退化，danazol 組高比率誘導閉經 |
| [2523321](https://pubmed.ncbi.nlm.nih.gov/2523321/) | 1989 | RCT | Fertility and Sterility | Gestrinone vs. Danazol RCT（n=39）：以誘導閉經為主要療效指標，治療 6 個月後兩組療效相當，均有效抑制月經 |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Systematic Review | Archives of Gynecology and Obstetrics | Gestrinone 治療子宮內膜異位症之系統性回顧：確認抗雌激素藥物誘導子宮內膜萎縮及閉經的機轉，可與 Danazol 效果對照參考 |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Retrospective Cohort | Women's Health (London) | 多中心回顧性研究：Danazol 用於跨性別及非二元性別個體的月經抑制，FDA 核准適應症明確列出，androgenic 副作用（毛髮改變、聲音變化）在特定族群中具雙重效益 |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Clinical Review | Progress in Clinical and Biological Research | Danazol 治療子宮內膜異位症及不孕症的早期系統性回顧；明確說明藥理機轉為卵巢功能抑制並誘發閉經 |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Review | Journal of Reproductive Medicine | Danazol 多樣生物效應綜述：中樞性 LH/FSH 抑制、性腺及腎上腺固醇合成抑制、免疫調節，三重機轉共同造成閉經 |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | Journal of the Royal Army Medical Corps | 治療性閉經誘導方法比較：連續口服避孕藥、GnRH 類似物（goserelin）及 Danazol，各具療效與副作用特性 |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | 異常子宮出血藥物治療的實證回顧：Danazol 為有效選項，適用於不需保留生育力的患者 |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Review | Human Reproduction Update | 子宮內膜異位症治療進展綜述：病灶在閉經狀態下退化為核心治療概念，支持誘導閉經的臨床價值 |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | Cohort | Journal of Allergy and Clinical Immunology | 56 名遺傳性血管水腫患者接受減弱型雄激素（Danazol 最低有效劑量 200 mg/d）長達 13 年追蹤；月經不規律及閉經為最常見副作用，反映其對月經週期的系統性影響 |

---

## 香港上市資訊

Danazol 在香港目前**未上市**，衛生署藥物登記資料庫中無任何有效許可證記錄。如需於香港使用，需透過特別用藥申請途徑（Special Drug Import）或參考鄰近地區（如台灣、日本）的上市資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **重要提示**：根據現有文獻，Danazol 具以下已知安全性顧慮，使用前需完整評估：
> - 屬**妊娠禁忌藥物**（可能造成女性胎兒男性化）及哺乳期禁忌（雄激素代謝物可進入母乳）
> - 主要不良反應包括：痤瘡、體毛增多、聲音改變（不可逆）、體重增加、肝毒性（需監測肝功能）
> - 與 lovastatin 合用已有橫紋肌溶解症及胰臟炎的案例報告（PMID 18691993）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Danazol 誘導閉經的機轉清晰直接，有多項 RCT 及臨床研究支持其療效，且此為治療子宮內膜異位症及功能性月經失調時的核心藥效終點，並非新適應症的概念延伸。然而，Danazol 在香港尚未上市，本地安全性文件（仿單禁忌症與警語）需補齊，方可推進正式評估。

**若要推進需要：**
- 取得 FDA 或 EMA 完整仿單，補充禁忌症、警語及交互作用資料（對應 DG001 資料缺口）
- 補充正式 MOA 文件（DrugBank API 查詢，對應 DG002 資料缺口）
- 向衛生署評估香港藥物登記或特別用藥申請可行性
- 針對目標族群（子宮內膜異位症、功能性月經失調、跨性別月經管理）制定分層安全性監測計畫
- 評估與 GnRH 類似物、黃體素等現有替代療法的定位差異，確立 Danazol 的差異化臨床價值
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

