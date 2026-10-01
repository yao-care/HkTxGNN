---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 911
evidence_level: L5
indication_count: 5
---

# Vandetanib
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

# Vandetanib：從甲狀腺髓質癌到腎細胞癌

## 一句話總結

Vandetanib 是口服多標靶酪胺酸激酶抑制劑，文獻指出其原本用於甲狀腺髓質癌。
TxGNN 模型預測它可能對**腎細胞癌 (Renal Cell Carcinoma)** 有效，目前有 **4 個臨床試驗**和 **6 篇文獻**與此方向相關。但其中 2 個試驗提前終止（僅收 3 人與 7 人），且沒有任何療效結果，文獻也多半不是直接研究 vandetanib。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；文獻（PMID 24451769）指出美國 FDA 核准用於甲狀腺髓質癌 |
| 預測新適應症 | 腎細胞癌 (Renal Cell Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2（依資料包評級；已有完成的 Phase 2 試驗，但未確認為隨機對照，宜保守解讀） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫的 MOA 欄位為空）。依一般藥理知識，vandetanib 是多激酶抑制劑，標靶包括 VEGFR2、EGFR 和 RET。

透明細胞腎細胞癌常見 VHL 基因失能，會使 HIF 穩定並促進 VEGF 表現，腫瘤因此高度依賴血管新生。阻斷 VEGFR 在生物學上說得通。同屬 VEGFR 標靶類的藥物（如 cabozantinib、nintedanib）已用於腎細胞癌或其他實體瘤，這也支持預測方向。

不過 0.999 的分數只是計算預測，不等於臨床有效。目前有 VHL 病、透明細胞型、HLRCC/SDH 相關腎癌的 Phase 2 試驗，但都沒有提供療效結果。現有資料只能支持繼續研究，不足以支持推薦使用。

模型另外還預測了三個腎細胞癌亞型（Xp11.2/TFE3 易位型、合併神經母細胞瘤型、未分類型），以及腎盂癌。前三者完全沒有試驗或文獻（L5）。腎盂癌僅有 1 個隨機 Phase 2 試驗（NCT01191892），其族群很可能是泌尿上皮癌，是否納入腎盂癌患者尚待確認。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 完成 | 37 | vandetanib 用於 VHL 病合併腎腫瘤；直接測試腎癌相關族群，未提供療效結果 |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | 提前終止 | 3 | 晚期透明細胞腎癌；僅收 3 人，無法判讀療效或安全性 |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | 提前終止 | 7 | vandetanib 合併 metformin 用於 HLRCC/SDH 相關腎癌或偶發性乳突狀腎癌；人數極少，且為併用，無法單獨評估 vandetanib |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | 完成 | 82 | 隨機試驗，carboplatin/gemcitabine 加或不加 vandetanib，用於不適合 cisplatin 的晚期泌尿上皮癌；與腎細胞癌僅間接相關 |

## 文獻證據

目前沒有直接評估 vandetanib 治療腎細胞癌的 RCT，下列文獻多為其他藥物的研究或前臨床資料。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Phase 2 試驗（其他藥物） | Clin Cancer Res | guadecitabine 用於 SDH 缺陷腫瘤與 HLRCC 相關腎癌；可作為這類罕見亞型的背景參考，與 vandetanib 無關 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review（nintedanib） | OncoTargets Ther | 回顧抗血管新生藥物（含 vandetanib）在實體瘤的角色 |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review（cabozantinib） | Bull Cancer | cabozantinib 抑制 VEGFR、c-MET、RET，可降低對 VEGFR 抑制劑的抗藥性 |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | 晚期甲狀腺癌的全身治療；vandetanib 為 RET 抑制劑，已獲 FDA 核准用於甲狀腺髓質癌 |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | 轉譯/前臨床 | Clin Exp Metastasis | 轉移性 FH 缺陷型腎細胞癌的代謝與表觀遺傳標靶；目前尚無標準治療 |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | 前臨床（小鼠模型） | Mol Cancer Res | TFE3 易位型腎細胞癌小鼠模型，找出新的治療標靶與診斷標記 GPNMB |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62087 | CAPRELSA TAB 300MG | SANOFI HONG KONG LIMITED |
| HK-62086 | CAPRELSA TAB 100MG | SANOFI HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多激酶抑制劑），非傳統細胞毒性化療 |

其餘項目（骨髓抑制風險、致吐性、監測項目、處置防護）請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得香港衛生署核准的仿單內容，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有 1 個完成且直接相關的腎癌 Phase 2 試驗（NCT00566995），且沒有療效結果。
- 另有 2 個腎癌試驗提前終止（n=3、n=7），不具判讀價值。
- 安全性資料缺口屬阻擋項，現階段不宜進一步推進。
- 這個預測更適合視為值得追蹤的研究問題，而不是可執行的用藥建議。

**若要推進需要：**
- 取得 NCT00566995 的試驗結果（客觀反應率、無惡化存活期、安全性），這是能否調升證據等級的關鍵。
- 確認 NCT01191892 實際納入的族群（泌尿上皮癌或腎盂癌）及其結果。
- 取得香港衛生署核准的仿單，補齊警語、禁忌症與藥物交互作用。
- 補齊作用機轉資料（例如查詢 DrugBank）。
- 與現行腎細胞癌標準治療（其他 VEGFR 標靶藥物）比較，評估 vandetanib 的相對價值。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

