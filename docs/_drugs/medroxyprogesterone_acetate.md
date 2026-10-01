---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 547
evidence_level: L5
indication_count: 5
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate：從（原適應症資料缺漏）到閉經（Amenorrhea）

## 一句話總結

Medroxyprogesterone acetate（MPA）是一種合成黃體素，在香港已有多款口服與注射製劑上市，但本次資料未提供原適應症。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**列於此方向，但多數為間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供 |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2（系統評分；見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Proceed with Guardrails |

> 證據等級說明：清單中僅 NCT02449161 為 Phase 3 RCT，且已提前終止、且以閉經為誘導結果而非治療目標。依本報告的 L1–L5 規則（需已完成的 Phase 2/3 RCT），嚴格來說此預測沒有直接支持的已完成 RCT，實際證據較接近 L3。沿用系統評分 L2 僅供參考，請審閱者留意。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，MPA 是合成黃體素（progestin），
可使經雌激素刺激的子宮內膜轉為分泌期，並抑制內膜增生；停藥後會引發撤退性出血。
這些作用與月經週期相關的療效指標直接相關。

需要特別注意：次發性閉經是 MPA 廣為人知的仿單適應症，
因此這個預測可能不算真正的「老藥新用」。
在把它視為新適應症之前，應先核對香港仿單的核准範圍。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | 提前終止 | 60 | 子宮內膜消融術後使用 MPA 對內膜閉經率的影響；閉經是誘導結果，非治療目標 |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | 完成 | 42 | 寡經或閉經女性在 clomiphene 排卵誘導前，是否需要黃體素引發撤退性出血 |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | 完成 | 29 | 功能性下視丘閉經的年輕女性心血管風險因子；閉經非主要終點 |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | 完成 | 184 | 產後施打 DMPA 的時機對哺乳與避孕持續率的影響；閉經僅為副作用 |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | 完成 | 1886 | Bazedoxifene/結合型雌激素對子宮內膜增生與骨質疏鬆的影響；與閉經關聯間接 |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | 招募中 | 120 | Relugolix 用於子宮肌瘤相關月經過多；與 MPA 及閉經的關聯無法確認 |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | 完成 | 108 | 荷爾蒙補充治療對停經前後紅斑性狼瘡女性的疾病活動度影響；間接相關 |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | 完成 | 79 | Tualang 蜂蜜與 HRT 對停經後女性安全性指標的影響；與閉經無關 |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | NA | 尚未招募 | 276 | 中藥方劑用於卵巢早衰；MPA 可能為對照組，尚無結果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | 隨機試驗 | Contraception | 100 位 DMPA 引起閉經的女性，改用 Cyclofem 後 6 個月內 82% 恢復出血，繼續 DMPA 者僅 10% |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT（系統歸類為 Cohort） | PLoS One | WHICH 試驗：比較 DMPA-IM 與 NET-EN 對雌二醇與月經型態的影響 |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | 系統性回顧 | Cochrane Database Syst Rev | 複合注射式避孕藥的效果與出血型態改變 |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | 臨床研究 | Acta Obstet Gynecol Scand | 比較 MPA 引起的閉經與次發性閉經女性的內膜組織學與荷爾蒙濃度 |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | DMPA 避孕的諮詢與副作用處理 |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | 產後避孕的時機與方法選擇 |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | 藥物引起的不孕症 |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Review | Int J Fertil Menopausal Stud | 長效避孕方法的比較 |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monographs | MPA 的致癌風險評估 |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | 臨床報告 | Am J Obstet Gynecol | 孕期使用 MPA 後的長期婦科與內分泌表現 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-00488 | PROVERA TAB 100 MG | — | 資料未提供 |
| HK-67226 | MEDWIN SUSPENSION FOR INJECTION IN PRE-FILLED SYRINGE 150MG/1ML | 注射懸液（預充填注射器） | 資料未提供 |
| HK-00445 | PROVERA TAB 5 MG | — | 資料未提供 |
| HK-43794 | DEPO-PROVERA CONTRACEPTIVE INJ 150MG/ML | 注射劑 | 資料未提供 |
| HK-54973 | APO-MEDROXY TAB 5MG | — | 資料未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，本次資料未取得香港衛生署仿單的警語與禁忌，且藥物交互作用查詢無結果，
因此尚無法進行安全性初篩。

## 其他預測適應症

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 重點 |
|------|------|-----------|---------|------|------|
| 2 | 乳房纖維囊腫 (Breast fibrocystic disease) | 99.95% | L3 | 研究問題 | 有小型臨床研究（如 Depo-Provera 治療乳腺病），但 HRT 研究顯示含黃體素方案可能增加乳房密度與上皮增生，作用方向不明，需排除乳房安全疑慮 |
| 3 | 良性乳腺發育不良 (Benign mammary dysplasia) | 99.92% | L4 | Hold | 與上一項本質相近，僅一篇直接相關的人體研究，其餘為犬類組織學與機轉論文，建議與纖維囊腫合併處理 |
| 4 | 子宮頸子宮內膜異位 (Cervix endometriosis) | 99.92% | L4 | Hold | 僅有病例報告、動物研究與一般性回顧，無子宮頸專屬的療效資料 |
| 5 | 皮膚疤痕子宮內膜異位 (Endometriosis in cutaneous scar) | 99.92% | L5 | Hold | 僅有模型預測，無試驗與文獻；標準處置為手術切除 |

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
MPA 的作用（分泌期轉化、撤退性出血）與閉經相關的月經週期終點有合理的機轉關聯，且有數個 Phase 2–4 試驗。
但直接證據薄弱：唯一的 Phase 3 RCT 已提前終止且非以治療閉經為目標，
而且次發性閉經可能本來就是 MPA 的既有適應症，故此案未必屬於真正的老藥新用。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症（是否已含閉經）、警語與禁忌
- 補齊 MPA 的作用機轉資料（DrugBank）
- 針對閉經（原發性 / 次發性 / 功能性下視丘）分型，尋找以治療閉經為主要終點的直接證據
- 補完藥物交互作用查詢，並依仿單建立安全性監測計畫
- 乳房相關預測（排名 2–3）需先排除乳房安全疑慮，再決定是否推進

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

