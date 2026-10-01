---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Goserelin：從 GnRH 促效劑到閉經 (Amenorrhea)

## 一句話總結

Goserelin 是 GnRH（促性腺激素釋放素）促效劑，在香港有 4 張許可證，但資料中未載明原核准適應症。
TxGNN 預測它可能與**閉經 (Amenorrhea)** 有關，目前有 **7 個臨床試驗**和 **20 篇文獻**。
證據多半顯示 Goserelin 是「誘發閉經、保護卵巢功能」，而不是「治療病理性閉經」，方向與預測字面意思不同。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（3 個已完成 Phase 3 試驗，但作用方向有落差） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。依一般藥理，Goserelin 持續給藥會抑制腦下垂體分泌 LH/FSH，使卵巢雌二醇下降，造成可逆的閉經（PMID 1533675）。

因此 TxGNN 的高分較可能反映「藥物與閉經」的關聯，而不是治療關係。多數 Phase 3 試驗把 Goserelin 用於兩種情境，閉經或卵巢功能都是結果指標：
- 化療期間預防卵巢衰竭
- 乳癌的卵巢抑制

「治療病理性閉經」缺乏機轉與臨床支持。若要推進，應改寫為「化療期間的卵巢保護」或「治療性誘發閉經」。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | 完成 | 400 | OPTION 試驗：停經前乳癌化療期間，比較加用 Goserelin 與不加，能否預防提早停經 |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | 完成 | 257 | 早期荷爾蒙受體陰性乳癌，化療期間使用 LHRH 類似物以降低卵巢衰竭 |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | 完成 | 98 | 停經前乳癌化療期間，隨機比較加用 Goserelin 對卵巢功能的保護效果 |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | 完成 | 32 | 比較芳香環轉化酶抑制劑與 GnRH 促效劑治療子宮腺肌症（與閉經僅間接相關） |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | 未知 | 100 | 含 Cyclophosphamide 的化療期間使用 Goserelin 保護卵巢，觀察月經結果 |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | 未知 | 300 | 停經前荷爾蒙受體陽性乳癌，Toremifene 加或不加 Goserelin（Goserelin 作為癌症治療的卵巢抑制） |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | 未分期 | 未知 | 未提供 | 單臂試驗：Zoladex 3.6mg 合併 CEF 化療作為乳癌術前輔助治療 |

## 文獻證據

註：多數摘要只呈現研究目的，未列具體結果，下表僅摘要摘要中可見的內容。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT（閉經次要分析） | J Clin Oncol | IBCSG VIII：比較化療、Goserelin 及兩者序貫治療對閉經、熱潮紅與生活品質的影響 |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA 試驗：Goserelin 對比 CMF 用於淋巴結陽性停經前乳癌，關注過早停經等長期影響 |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | 淋巴結陰性乳癌：化療後接 Goserelin，對比單一療法 |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin 對比低劑量口服避孕藥治療子宮內膜異位症骨盆痛（與閉經間接相關） |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Review/Meta-analysis | Ann Oncol | OPTION 試驗：化療期間使用 GnRH 促效劑是否降低卵巢早衰風險 |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Goserelin 誘發可逆性卵巢抑制，在荷爾蒙敏感的早期乳癌中療效至少不劣於 CMF 化療 |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | 討論以 Goserelin 誘發閉經（例如用於戰時女性人員），相較連續口服避孕藥有其優勢 |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | 停經前及更年期前乳癌輔助治療中，各種卵巢抑制方式的比較 |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | 化療後未閉經的 II/III 期荷爾蒙受體陽性乳癌，以 Goserelin 卵巢抑制的價值 |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort | J Clin Oncol | 乳癌卵巢抑制治療期間是否需要監測雌二醇 |

## 香港上市資訊

資料中未提供劑型與核准適應症，下表僅列許可證號、品名與持證商。

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-42691 | ZOLADEX LA DEPOT INJ 10.8MG | ASTRAZENECA HONG KONG LIMITED |
| HK-31178 | ZOLADEX DEPOT INJ 3.6MG | ASTRAZENECA HONG KONG LIMITED |
| HK-65753 | GOSERELIN ALVOGEN IMPLANT IN A PREFILLED SYRINGE 10.8MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-65754 | GOSERELIN ALVOGEN IMPLANT IN A PREFILLED SYRINGE 3.6MG | LOTUS PHARMACEUTICAL HK LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖有 3 個已完成的 Phase 3 試驗，但它們證明的是「Goserelin 在化療期間保護卵巢」，並非治療病理性閉經，預測字面意思缺乏支持。
- 香港仿單的警語與禁忌尚未取得（阻斷性資料缺口），無法進入安全性篩選。

**若要推進需要：**
- 將研究問題改寫為「化療期間卵巢保護」或「治療性誘發閉經」，並重新評估這個新問題的證據。
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症。
- 補齊 DrugBank 作用機轉資料。
- 評估卵巢保護情境的安全性，例如更年期樣症狀與生育相關考量。

**其他預測：** 「腎發育不全 (Renal hypoplasia)」及其雙側型（排名 2、3）分數約 99.1%，但沒有任何臨床試驗或文獻，也找不到機轉關聯，僅屬模型預測（L5），建議 Hold。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

