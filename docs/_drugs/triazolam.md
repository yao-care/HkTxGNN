---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 770
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Triazolam：適應症資料缺口下的失眠治療評估（睡眠起始與維持障礙）

## 一句話總結

> 本次 Evidence Pack 未提供 Triazolam 的原始核准適應症資料。
> TxGNN 模型預測它可能對**睡眠起始與維持障礙 (Sleep Disorder, Initiating and Maintaining Sleep)** 有效，
> 目前**無臨床試驗登記**，但有 **20 篇文獻**支持這個方向，其中多篇文獻直接以 Triazolam 作為失眠治療藥物進行討論或比較。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 未提供） |
| 預測新適應症 | 睡眠起始與維持障礙 (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN 預測分數 | 99.72% |
| 證據等級 | L3（無臨床試驗，但有多篇系統性回顧/統合分析） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Triazolam 的正式作用機轉資料（DG002，High severity，需查詢 DrugBank API 補齊）。

不過從文獻證據可以看出，Triazolam 本身在多篇文獻中被直接列為失眠治療的比較藥物，例如 PMID 9161660〈Zolpidem: distinct from triazolam?〉、PMID 1319429〈Pharmacology of benzodiazepine hypnotics〉，以及 PMID 2567741 討論其停藥後反彈性失眠現象。這些文獻顯示 Triazolam 在藥理學與臨床實務上早已被視為苯二氮平類 (benzodiazepine) 安眠藥的代表藥物之一。

因此，TxGNN 對「睡眠起始與維持障礙」的預測，性質上比較接近**驗證已知藥理用途**，而非全新機轉的推論延伸。這也部分解釋了為何目前完全沒有相關臨床試驗登記——因為此用途已是成熟臨床實務，較少會再產生新的正式試驗。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Meta-analysis | Sleep | 老年族群失眠治療藥物之療效與安全性網絡統合分析 |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Meta-analysis | Psychiatry Clin Neurosci | 各類安眠藥（含苯二氮平類）合併抗憂鬱劑治療伴隨失眠之重度憂鬱症的雙盲 RCT 統合分析 |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | 美國睡眠醫學會（AASM）成人慢性失眠藥物治療臨床指引 |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | 比較 Zolpidem 與 Triazolam 於失眠治療之療效與安全性 |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | 回顧苯二氮平類安眠藥（含 Triazolam）之藥理學發展歷程 |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Semin Neurol | 討論苯二氮平類安眠藥（含 Triazolam）於睡眠障礙治療之臨床神經藥理學 |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Review | Drug Saf | 評估短效安眠藥（含 Triazolam）之安全性 |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Original study | J Sleep Res | 研究 Triazolam 與 Zolpidem 對睡眠依賴性動作學習之逆行性影響 |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | 回顧短效苯二氮平類（含 Triazolam）停藥後之反彈性失眠現象 |
| [35802843](https://pubmed.ncbi.nlm.nih.gov/35802843/) | 2022 | Review | Med Lett Drugs Ther | 新型失眠藥物 Daridorexant（Quviviq）之藥物評論，可作為 Triazolam 之替代比較基準 |

---

## 香港上市資訊

Triazolam 目前**未在香港取得許可證**，無上市藥品資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：TFDA 仿單警語/禁忌資料目前缺失（DG001，Blocking severity），此為進入下一階段安全性初評（S1）的關鍵阻礙項目，需優先補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 文獻顯示 Triazolam 作為苯二氮平類安眠藥於失眠治療領域已有長期臨床實證，預測方向具藥理合理性；
- 但本藥目前**未在香港上市**、**缺乏仿單警語/禁忌等關鍵安全性資料（Blocking gap）**，且**無正式作用機轉紀錄**，尚不具備進入下一階段評估的條件。

**若要推進需要：**
- 取得 TFDA/仿單警語與禁忌症資料（DG001，Blocking，需下載仿單 PDF 並解析）
- 補充 DrugBank 作用機轉資料（DG002，High，需查詢 DrugBank API）
- 確認是否有意願申請香港藥物許可證及後續上市規劃
- 因無臨床試驗登記，建議進一步查詢 ICTRP 或區域試驗註冊資料庫，補強實證等級
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

