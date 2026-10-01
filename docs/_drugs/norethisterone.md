---
layout: default
title: Norethisterone
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 1
---

# Norethisterone
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

# Norethisterone：從原適應症未載明到閉經 (Amenorrhea)

## 一句話總結

Norethisterone 是一種合成黃體素 (progestogen)，在香港有 12 張上市許可證，但本次資料未載明其原適應症。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效，預測分數很高。
目前有 **8 個臨床試驗**和 **20 篇文獻**，但都只是間接證據，沒有單獨以 Norethisterone 治療閉經的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證資料中沒有適應症文字） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L4（資料包評定；Phase 3 試驗皆為含 Norethisterone 的複方，屬間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Norethisterone 是合成黃體素類藥物。黃體素能穩定並抑制子宮內膜，因此機轉上可能影響月經週期。

但這個關聯目前只是推論，尚未驗證。TxGNN 分數雖然很高，但它只是知識圖譜的預測結果。本資料包缺少原適應症與作用機轉，所以無法確認預測與藥物原有用途之間的關係。

現有試驗中，Norethisterone acetate 只是 relugolix／estradiol／norethisterone 複方中的「add-back」成分。這些試驗治療的是子宮肌瘤引起的經血過多，閉經只是次要的出血結果，並非要治療的疾病。

另一個要留意的方向問題：在避孕相關研究中，閉經常被當成黃體素類藥物造成的月經變化（副作用）。例如 1981 年的 Phase I 試驗就記錄了閉經、點狀出血等月經異常的發生率。因此「誘發閉經」和「治療閉經」是不同的臨床問題，不能混為一談。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Phase 3 | 完成 | 388 | LIBERTY 1：Relugolix 併用 estradiol 與 norethindrone acetate，對照安慰劑，用於子宮肌瘤相關經血過多（24 週）。為複方證據，非單用 Norethisterone |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Phase 3 | 完成 | 382 | LIBERTY 2：與 LIBERTY 1 設計相同的重複試驗，同樣為複方間接證據 |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Phase 3 | 完成 | 477 | LIBERTY 延伸試驗：開放標示、單組，提供複方 28 週長期療效與安全性，無對照組 |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | 完成 | 229 | 隨機停藥試驗：評估 relugolix 複方（含 norethindrone acetate）最長 104 週的長期療效與安全性，目標疾病並非閉經 |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | 未知 | 312 | BG2109 單用或併用 add-back 治療，對照安慰劑，用於子宮肌瘤經血過多。與 Norethisterone 及閉經的關聯無法從現有欄位確認 |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2 | 完成 | 571 | Elagolix 單用或併用 add-back，用於子宮肌瘤經血過多。主藥為 Elagolix，直接相關性低 |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | 完成 | 271 | Elagolix 對照安慰劑的概念驗證試驗。Norethisterone 並非試驗藥物，相關性極低 |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | 不適用 | 招募中 | 111 | MySaturn：以超音波觀察 relugolix／estradiol／norethisterone 治療期間肌瘤外觀變化，屬影像學終點，尚無結果 |

## 文獻證據

多數文獻缺少摘要，「主要發現」僅依標題與現有資訊整理。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | 隨機試驗 | PLoS One | WHICH 試驗：比較 DMPA-IM 與 NET-EN 注射避孕劑對雌二醇濃度、月經及心理行為指標的影響 |
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | RCT 事後分析 | Am J Obstet Gynecol | Relugolix 複方（含 norethindrone acetate）在黑人／非裔女性子宮肌瘤患者中，52 週內明顯改善經血過多 |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Phase I 臨床試驗 | Contraception | 20 位古巴女性使用 NEN 注射劑或 NET 迷你避孕藥，排卵前 LH 與 FSH 高峰消失，並觀察到閉經、點狀出血等月經異常 |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 複方注射避孕劑的避孕效果與月經型態改變 |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 同上，為早期版本 |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | 概述 | Obstet Gynecol | 口服 GnRH 拮抗劑（搭配替代量類固醇）治療子宮肌瘤的療效與安全性 |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Review | Pediatr Clin North Am | 青少年荷爾蒙避孕的原則與處置 |
| [3914370](https://pubmed.ncbi.nlm.nih.gov/3914370/) | 1985 | Review | Clin Ther | 口服避孕藥現況（無摘要） |
| [3071312](https://pubmed.ncbi.nlm.nih.gov/3071312/) | 1988 | Review | Aust Fam Physician | 口服避孕藥的選擇（無摘要） |
| [12335903](https://pubmed.ncbi.nlm.nih.gov/12335903/) | 1979 | Review | Contracept Fertil Sex | 子宮內膜異位症與不孕（無摘要） |

## 香港上市資訊

共 12 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症文字，因此省略這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58408 | NORMENS TAB 5MG | PRIMAL CHEMICAL CO LTD |
| HK-53880 | MEDORONE TAB 5MG | STAR MEDICAL SUPPLIES LTD |
| HK-49738 | NORDRON TAB 5MG | HITPHARM PHARMACEUTICAL CO LTD |
| HK-59181 | NORETONE TAB 5MG | WAI LUN TRADING CO |
| HK-22468 | NORCOLUT TAB 5MG | MEKIM LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 8 個臨床試驗中沒有一個是單獨以 Norethisterone 治療閉經。Phase 3 試驗都是含 Norethisterone 的複方，治療的是子宮肌瘤經血過多，閉經只是出血結果。
- 文獻多為避孕相關的舊文獻，閉經在其中常是副作用。
- 原適應症、作用機轉與安全性資料都有缺口，且香港仿單資料缺漏屬阻擋性缺口，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊原適應症、警語與禁忌症（阻擋性缺口）。
- 從 DrugBank 補充作用機轉資料。
- 檢索 Norethisterone 單方治療閉經（區分原發性與繼發性）的臨床試驗與文獻。
- 釐清各試驗與文獻中閉經是治療目標還是不良反應，並人工審閱標註為「待審」的文獻。
- 確認劑型與給藥途徑是否適用於新適應症。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

