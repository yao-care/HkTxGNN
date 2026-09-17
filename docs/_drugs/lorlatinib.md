---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 5
---

# Lorlatinib
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

Using the evidence pack as given, but flagging a judgment call up front: `predicted_indications[0]`（牙齦纖維瘤病）本身的 `repurposing_rationale` 明確寫「無實證、應予排除」，其餘除 rank 4 外皆同。若機械套版會產出誤導性報告，因此以下以「多候選總覽」呈現，並將唯一有實質證據支持的 rank 4（肺門癌）作為主要分析對象。

# Lorlatinib：從 ALK/ROS1 陽性肺癌到肺門癌等 5 項候選新適應症

## 一句話總結

Lorlatinib 是第三代 ALK/ROS1 酪胺酸激酶抑制劑，原始適應症資料本身缺失（僅能從文獻反推為 ALK/ROS1 陽性晚期非小細胞肺癌）。TxGNN 對此藥共產出 5 項高分預測，但逐一比對證據後，其中 4 項（牙齦纖維瘤病、肺纖維瘤、肺錯構瘤、肺良性腫瘤）**無實質支持或屬疾病本體誤配的偽陽性**，僅有 **肺門癌 (lung hilum carcinoma)** 有 1 篇個案報告佐證，屬既有適應症在「新輔助治療時機」與「特定解剖位置」上的延伸應用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（原始欄位空白），依文獻反推為 ALK/ROS1 陽性晚期 NSCLC |
| 預測新適應症（主要） | 肺門癌 (Lung Hilum Carcinoma) |
| TxGNN 預測分數 | 99.74%（rank 4，knowledge graph rank 5608） |
| 證據等級 | L4（單一個案報告） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

**其他 4 項候選（均建議排除，不列入以下細節章節）：**

| Rank | 預測適應症 | TxGNN 分數 | 證據 | 結論 |
|------|-----------|-----------|------|------|
| 1 | 牙齦纖維瘤病 | 99.81% | 無臨床試驗/文獻 | 機轉無關，Hold |
| 2 | 肺纖維瘤 | 99.75% | 無臨床試驗/文獻 | 機轉無關，Hold |
| 3 | 肺錯構瘤 | 99.75% | 無臨床試驗/文獻 | 機轉無關（驅動基因為 HMGA2，非 ALK），Hold |
| 5 | 肺良性腫瘤 | 99.74% | 20 篇文獻（皆為惡性 NSCLC 研究） | 疾病本體誤配偽陽性，Hold |

## 為什麼這個預測合理？（僅指肺門癌候選）

目前缺乏詳細的作用機轉資料（`original_moa` 為 Data Gap）。但綜合文獻可確認 lorlatinib 為腦滲透性第三代 ALK/ROS1 抑制劑，其既有適應症為 ALK 陽性晚期 NSCLC（CROWN 三期試驗確立之標準治療）。

唯一支持「肺門癌」候選的證據，是一篇個案報告（PMID 37934724）：一名 ALK 陽性肺癌患者接受 neoadjuvant（新輔助）lorlatinib 治療後達病理完全緩解（pCR），其腫瘤位置屬肺門區域。這並非全新分子機轉的疾病關聯，而是既有 ALK 抑制機轉，在「手術前給藥時機」與「特定解剖部位腫瘤」情境下的延伸應用 — 機轉上合理，但目前僅單一案例支持，尚未有前瞻性試驗驗證。

其餘 4 項候選經逐一檢視機轉關聯性後，均判定為 TxGNN 知識圖譜嵌入相似度導致的偽陽性（詳見上方總覽表），不建議進一步投入資源。

## 臨床試驗證據

目前無相關臨床試驗登記（5 項候選在 ClinicalTrials.gov 與 ICTRP 查詢皆為 0 筆）。

## 文獻證據（肺門癌候選）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37934724](https://pubmed.ncbi.nlm.nih.gov/37934724/) | 2023 | Case Report | The American Journal of Case Reports | ALK 陽性晚期肺癌患者接受 neoadjuvant lorlatinib 後達病理完全緩解，腫瘤位於肺門區域 |

**補充參考（既有 ALK+ NSCLC 適應症，非直接支持肺門癌候選，但顯示藥物核心療效基礎）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33207094](https://pubmed.ncbi.nlm.nih.gov/33207094/) | 2020 | RCT (NEJM) | New England Journal of Medicine | Lorlatinib 一線治療 vs crizotinib，CROWN 試驗初步結果 |
| [38819031](https://pubmed.ncbi.nlm.nih.gov/38819031/) | 2024 | RCT 5年追蹤 | Journal of Clinical Oncology | CROWN 試驗 5 年長期存活與顱內控制數據 |
| [39368244](https://pubmed.ncbi.nlm.nih.gov/39368244/) | 2024 | 系統性回顧/網絡統合分析 | Lung Cancer | Lorlatinib 與其他 ALK TKI 一線治療比較 |

## 香港上市資訊

未上市，無許可證資料。

## 細胞毒性（標靶藥物）

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（第三代 ALK/ROS1 酪胺酸激酶抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 官方仿單資料缺失，文獻回顧（PMID 38554546、30890623）主要提及高血脂、體重增加、周邊水腫、中樞神經系統副作用（認知/情緒變化），非典型骨髓抑制表現 |
| 致吐性分級 | 官方資料缺失，請參考原廠仿單 |
| 監測項目 | 依文獻建議：血脂（總膽固醇、三酸甘油酯）、體重、認知/精神狀態評估 |
| 處置防護 | 官方資料缺失，請參考原廠仿單的警語與注意事項 |

## 安全性考量

官方安全性資料（警語、禁忌症、藥物交互作用）皆為 Data Gap，安全性資訊請參考原廠仿單。文獻回顧（PMID 38554546「A pragmatic guide for management of adverse events associated with lorlatinib」）另提供不良反應處置參考，但非官方仿單資料，僅供臨床背景理解。

## 結論與下一步

**決策：Hold**

**理由：**
- 5 項 TxGNN 預測中，4 項無任何實證支持或屬疾病本體誤配之偽陽性，應排除。
- 唯一有實證的「肺門癌」候選僅有 1 篇個案報告（L4），且香港未上市、無 MOA 官方資料，證據強度不足以進入 S1 之後階段。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 補齊 DrugBank 官方 MOA 資料（DG002，High）
- 針對「neoadjuvant + 肺門部位」情境尋找更多病例系列或前瞻性研究，驗證單一個案報告之外的可重複性
- 其餘 4 項候選建議直接標記排除，不需再投入證據收集資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

