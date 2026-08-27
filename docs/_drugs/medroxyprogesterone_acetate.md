---
layout: default
title: Medroxyprogesterone Acetate
parent: 高證據等級 (L1-L2)
nav_order: 396
evidence_level: L2
indication_count: 5
---

# Medroxyprogesterone Acetate
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

# MEDROXYPROGESTERONE ACETATE：從避孕／荷爾蒙相關用途到繼發性閉經（Amenorrhea）評估

## 一句話總結

MEDROXYPROGESTERONE ACETATE (MPA) 是一種合成黃體素（孕激素受體促效劑），臨床上長期作為避孕（如 Depo-Provera）與荷爾蒙補充治療的成分。TxGNN 模型預測它可能對**繼發性閉經 (Amenorrhea)** 有效，目前有 **10 個臨床試驗**和 **20 篇文獻**與此主題相關，但多數證據描述的是「MPA 誘發閉經」（避孕副作用／孕激素撤退試驗），而非「MPA 治療閉經」的直接療效終點，證據方向需進一步釐清。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證核准紀錄（當地未上市）；國際上慣用於避孕、荷爾蒙補充治療 |
| 預測新適應症 | 繼發性閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.9994% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 詳細的作用機轉資料（Data Gap）。根據試驗與文獻證據可以推論：MPA 為合成黃體素，其藥理作用是活化孕激素受體，長期給藥（尤其是肌肉注射劑型 DMPA）會抑制下視丘－腦下垂體－卵巢軸（HPO axis），並造成子宮內膜萎縮，臨床上早已知悉這會誘發閉經——這正是 DMPA 作為避孕藥時常見的副作用。

同時，MPA 也被廣泛用於「孕激素撤退試驗（progestin withdrawal test）」，作為鑑別次發性閉經病因的標準診斷／治療工具之一，也用於術後子宮內膜萎縮誘導（例如子宮內膜消融術後）。這是 MPA 與「閉經」這個適應症在機轉與臨床實務上最直接的連結，也支持 TxGNN 模型將兩者關聯起來的合理性。

然而必須特別指出一個重要區辨：資料庫中大部分證據描述的是 MPA「造成」閉經（避孕情境），而非以 MPA 主動「治療」閉經作為主要療效終點的直接證據。唯一直接評估此議題的 Phase 3 RCT（NCT02449161，子宮內膜消融術後 MPA 對閉經率之影響）已提前終止（TERMINATED），終止原因尚待查明，這使得預測合理性存在但證據強度有限。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | 已終止 | 60 | 子宮內膜消融術後 MPA 對閉經率影響之 RCT，已提前終止，原因待查 |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | 已完成 | 42 | 評估 Clomiphene 誘導排卵前是否需孕激素撤退性出血 |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | NA | 尚未招募 | 276 | 中藥複方（Huanjingjian 湯劑）治療卵巢早衰之 RCT，非以 MPA 為介入藥物 |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | 招募中 | 120 | Relugolix 治療子宮肌瘤相關經血過多，非以 MPA 為介入藥物 |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | 已完成 | 108 | HRT 對停經期／停經後 SLE 婦女疾病活動度、停經症狀與骨密度之影響 |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | 已撤回 (0人) | 0 | 雌二醇對厭食症患者食物恐懼消退之研究，非以 MPA 為介入藥物 |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | 已完成 | 184 | 產後 DMPA 給藥時機對哺乳持續性、避孕持續性與產後憂鬱之影響 |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | 已完成 | 29 | 功能性下視丘性閉經（低雌激素狀態）與心血管疾病風險因子之相關性研究 |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | 已完成 | 79 | Tualang 蜂蜜與 HRT 對停經後婦女安全性影響之比較 |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | 已完成 | 1886 | Bazedoxifene/結合雌激素組合對子宮內膜增生與骨質疏鬆預防之療效安全性大型 RCT |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | RCT | Contraception | 100 名 DMPA 誘發閉經婦女隨機分派改用 Cyclofem 或持續 DMPA，比較陰道出血恢復情形 |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | Cohort (RCT衍生分析) | PLoS One | DMPA-IM 與 NET-EN 對雌二醇濃度、經期與心理行為指標之比較（WHICH 試驗） |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | 比較研究 | Acta Obstet Gynecol Scand | MPA 誘發閉經婦女之子宮內膜組織學與 MPA/雌二醇/FSH/LH 濃度分析，並與次發性閉經婦女比較 |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 複方注射避孕藥（含 MPA 類）之療效與可接受度系統性回顧 |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | DMPA 使用者的諮詢重點與副作用（含閉經）處置建議 |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | 產後避孕方法選擇與產後閉經期之考量 |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | Depo-Provera 臨床應用綜述 |
| [6454820](https://pubmed.ncbi.nlm.nih.gov/6454820/) | 1981 | Review | Med J Aust | 注射型避孕藥物綜述 |
| [12222332](https://pubmed.ncbi.nlm.nih.gov/12222332/) | 1991 | Review | Entre Nous | 每月一次雌激素/黃體素複方注射劑綜述 |
| [1604074](https://pubmed.ncbi.nlm.nih.gov/1604074/) | 1992 | Review | Rev Med Liege | 荷爾蒙避孕法綜述 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本次資料收集無法取得仿單警語與禁忌症資料（Blocking Data Gap），此為推進本候選適應症前必須優先補齊的項目。

---

## 其他預測候選適應症（低優先，僅供參考）

除繼發性閉經外，本次模型另預測 4 個候選適應症，但證據強度明顯較弱：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 2 | 乳腺纖維囊性病 (Breast fibrocystic disease) | 99.95% | L3 | Research Question（僅1980年代小型治療性試驗，無現代RCT） |
| 3 | 良性乳腺增生 (Benign mammary dysplasia) | 99.92% | L4 | Hold（專屬文獻僅3篇，與排名2高度重疊） |
| 4 | 子宮頸子宮內膜異位 (Cervix endometriosis) | 99.92% | L4 | Hold（無直接針對此亞型的治療證據） |
| 5 | 皮膚疤痕子宮內膜異位 (Endometriosis in cutaneous scar) | 99.92% | L5 | Hold（無臨床試驗、無文獻，純機轉外推） |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本藥物在當地尚未上市（0 張許可證），且仿單警語／禁忌症資料缺失屬 Blocking 等級資料缺口，無法完成 S1 安全性初評。
- 頂尖候選適應症「繼發性閉經」雖有 Phase 3/4 試驗與 Cochrane 回顧支持（評為 L2），但唯一直接對應本適應症的 Phase 3 RCT 已提前終止，且多數證據描述的是「MPA 誘發閉經」而非「MPA 治療閉經」的療效終點，證據方向尚待釐清。
- 其餘 4 個候選適應症證據等級落在 L3–L5，證據明顯不足，暫不建議推進。

**若要推進需要：**
- 補齊當地衛生主管機關（或原廠）仿單之警語與禁忌症資料（解除 Blocking gap）
- 向 DrugBank 或原廠取得完整作用機轉（MOA）資料
- 查明 NCT02449161 提前終止之原因，評估是否有後續或替代試驗
- 若確立推進，需另行設計或尋找以「MPA 治療閉經」為主要療效終點的前瞻性研究
- 評估當地上市／引進之法規可行性（目前完全未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

