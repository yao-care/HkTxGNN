---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 876
evidence_level: L5
indication_count: 5
---

# Topotecan
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

# Topotecan：預測新適應症為女性乳癌（原適應症資料未提供）

## 一句話總結

Topotecan 是拓樸異構酶 I (topoisomerase I) 抑制劑類的化療藥，香港已有 3 張許可證，但本次提供的資料沒有記載其原核准適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前有 **5 個相關臨床試驗登記**和 **20 篇文獻**，但沒有確認的隨機對照試驗 (RCT)，且人體 Phase II 資料顯示的單藥活性有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3（依判定規則；詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

**證據等級說明：**
- 資料包自動評為 L2，但 L2 需有已完成的 Phase 2/3 RCT。
- 目前乳癌方向的人體研究多為單臂 Phase II，唯一的隨機試驗 (NCT02282020) 研究的是卵巢癌，且無法確認 topotecan 是否為其中一組。
- 因此本報告保守判定為 L3（有臨床研究與回顧文獻，無確認的 RCT）。

---

## 為什麼這個預測合理？

Topotecan 是拓樸異構酶 I 抑制劑，會造成 DNA 斷裂，對快速增生的腫瘤細胞有殺傷力。本次資料沒有提供詳細的作用機轉 (MOA) 與原適應症，以下推論只依據資料包中的機轉線索。

2023 年的前臨床研究 (PMID 37987734) 發現，在 MYC 驅動的癌症中抑制拓樸異構酶 I 可造成合成致死 (synthetic lethality)。MYC 活化在三陰性乳癌中相當常見，這是目前最具體的機轉連結。2025 年的研究 (PMID 40300683) 也指出 TFDP1 可能是三陰性乳癌中 topotecan 的治療標靶。

人體資料方面，CALGB Phase II (PMID 10362325)、連續輸注試驗 (PMID 9413954) 和腦轉移前導研究 (PMID 11455218) 顯示的單藥活性有限，並非決定性證據。TxGNN 的高分 (99.92%) 是模型預測，本身不代表臨床有效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | 已終止 | 未提供 | 高劑量 topotecan + ifosfamide/mesna + etoposide (TIME)，後接自體幹細胞救援，用於轉移性乳癌；topotecan 為方案成分，但試驗提早終止 |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | 完成 | 266 | Olaparib vs 醫師選擇的單藥化療，對象為 gBRCA 突變卵巢癌；topotecan 是否為對照組尚未確認，不能算直接證據 |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | 進行中（不招募） | 120 | Durvalumab + olaparib + cediranib 三合一 vs 標準化療，用於鉑類抗藥卵巢癌等；topotecan 的角色與腫瘤族群待確認 |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | 已終止 | 221 | Selinexor 搭配多種標準化療（含 topotecan）的安全性研究，未測試乳癌療效 |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | 無分期 | 未知 | 35 | 以病人來源類器官藥物篩選指引化療的研究，未特別測試 topotecan，屬間接證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II | Am J Clin Oncol | CALGB 研究，topotecan 用於已接受過一次晚期化療的乳癌患者（53 人入組，40 人可評估） |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II | Br J Cancer | 連續輸注 topotecan 用於晚期乳癌與非小細胞肺癌，未見療效提升 |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot study | Onkologie | 評估 topotecan 作為乳癌腦轉移初始化療的角色 |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase II | J Clin Oncol | Paclitaxel + topotecan 搭配 G-CSF，用於曾接受治療的 IV 期乳癌 |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynakol Geburtshilfliche Rundsch | 乳癌新藥現況與展望（德文） |
| [7910993](https://pubmed.ncbi.nlm.nih.gov/7910993/) | 1994 | Review | World J Surg | 轉移性乳癌的整體處置原則 |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | 前臨床 | Cancer Res | MYC 驅動癌症中抑制拓樸異構酶 I 可促成 R-loop 累積而合成致死 |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | 前臨床 | Int J Biol Macromol | TFDP1 促進三陰性乳癌，且可能是 topotecan 的治療標靶 |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | 前臨床 | Oncotarget | 節拍式 topotecan + pazopanib 在三陰性乳癌模型中的療效 |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | 前臨床（異種移植） | Anticancer Res | 比較 doxorubicin、cisplatin、irinotecan、topotecan 對大腸、肺、乳癌異種移植瘤的效果 |

未列出的其餘文獻多為抗藥性機轉（如 BCRP）或卵巢癌等間接證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 |
|---------|------|------|
| HK-60430 | TOPOTECAN ACTAVIS（Teva Pharmaceutical Hong Kong） | 輸注用濃縮液粉末 4mg |
| HK-67254 | TOPOCAN（Golden Billion Health Products） | 輸注用濃縮液粉末 4mg |
| HK-68935 | HYCAMCORD（Jacobson Marketing） | 輸注用濃縮液 4mg/4ml |

三張許可證的核准適應症欄位在資料中皆為空白，需查閱仿單確認。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（拓樸異構酶 I 抑制劑） |
| 骨髓抑制風險 | 高。文獻中 topotecan 的主要毒性為骨髓抑制，例如生殖細胞瘤 Phase II 試驗 (PMID 8617580) 記錄到明顯的白血球、嗜中性球、血紅素與血小板下降 |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，且有合理的機轉線索（MYC 驅動的合成致死），但乳癌方向目前沒有確認的 RCT。
- 人體 Phase II 資料多為 1990 年代的單藥研究，活性有限、非決定性，其餘多為前臨床或間接證據。
- 香港仿單的安全性資料缺漏，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症（阻斷性缺口）
- 補充 DrugBank 的作用機轉資料
- 逐一確認 NCT02282020、NCT04739800 中 topotecan 的角色與乳癌族群，並檢索乳癌專屬的 topotecan 隨機試驗
- 鎖定可能受益的亞群（例如 MYC 活化的三陰性乳癌），評估是否值得設計新試驗

**其他預測適應症（簡述）：** 成人生殖細胞瘤 (L3) 有一項 Phase II 研究 (PMID 8617580) 顯示 topotecan 對順鉑抗藥的生殖細胞瘤沒有客觀緩解，且其餘試驗多為兒童神經母細胞瘤等間接證據，建議審慎看待。睪丸卵黃囊瘤的三個亞型 (L5) 僅有模型預測，無任何試驗或文獻，維持 Hold。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

