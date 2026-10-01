---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atorvastatin：從降血脂用藥到家族性高膽固醇血症

## 一句話總結

Atorvastatin 是一種他汀類（statin）降膽固醇藥物，香港已有 20 張許可證，但許可證資料未載明核准適應症。
TxGNN 模型預測它可能對**家族性高膽固醇血症 (Familial Hypercholesterolemia, FH)** 有效，目前有 **31 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過這較可能是已被廣泛確立的用途，而非真正的老藥新用（詳見下方說明）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（文獻描述用於原發性高膽固醇血症與混合型血脂異常） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L1（多數試驗為併用療法，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據預測理由，atorvastatin 抑制 HMG-CoA 還原酶，使肝臟 LDL 受體上調，進而降低 LDL-C。這是他汀類的核心機轉。

FH 的病理是 LDL 清除受損，導致 LDL-C 長期偏高。他汀類正好透過增加 LDL 受體來加強清除，因此機轉上高度吻合。文獻也指出，高劑量強效他汀是 FH 治療的基石。

這個預測需要留意一點。輸入資料中的原適應症是空的，但 atorvastatin 用於 FH 早已被廣泛確立，因此它較可能是**既有適應症**，而不是新用途。建議先檢查許可證的適應症欄位是否有缺漏。

## 臨床試驗證據

共 31 個相關試驗，以下列出 10 個最相關者。多數 Phase 3 試驗是在 atorvastatin 背景治療上加測其他藥物（如 alirocumab、ezetimibe、torcetrapib），並非單獨測試 atorvastatin。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | 完成 | 400 | Torcetrapib/atorvastatin 複方 vs 最大耐受劑量 atorvastatin 單用，用於雜合子 FH（隨機雙盲） |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | 完成 | 800 | 以頸動脈超音波評估複方與 atorvastatin 單用對雜合子 FH 動脈粥樣硬化的影響 |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | 完成 | 272 | Atorvastatin 用於兒童及青少年雜合子 FH 的 3 年開放標示研究，評估生長發育與降膽固醇效果 |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | 完成 | 39 | Atorvastatin 用於兒童雜合子 FH 的藥動、藥效與安全性，支持劑量與耐受性，但不評估療效 |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | 完成 | 30 | Torcetrapib/atorvastatin 用於純合子 FH（開放、強制滴定、無對照組） |
| [NCT00145431](https://clinicaltrials.gov/study/NCT00145431) | Phase 3 | 終止 | 41 | 複方 vs atorvastatin 單用 vs fenofibrate，用於 III 型高脂蛋白血症；因複方藥物安全性問題提前終止 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | Ezetimibe 加在 atorvastatin 或 simvastatin 上，用於純合子 FH |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | 完成 | 355 | Alirocumab 或 ezetimibe 加在 atorvastatin 上，與加大 atorvastatin 劑量、換用 rosuvastatin 比較 |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 完成 | 486 | Alirocumab 對照安慰劑，用於背景降脂治療控制不佳的雜合子 FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | 完成 | 249 | 設計同上，atorvastatin 為背景治療 |

Torcetrapib 開發計畫已於 2006 年因安全性發現而終止，這是複方藥物的問題，不代表 atorvastatin 本身。

## 文獻證據

共 20 篇文獻，以下列出 10 篇，依證據強度排序。多篇原始資料未標明研究類型，類型欄依標題與摘要判斷。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | 系統性回顧/統合分析 | J Am Coll Cardiol | 量化他汀對雜合子 FH 患者冠心病事件與死亡率的影響 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | 臨床指引 | Endocr Pract | AACE/ACE 血脂異常處置與心血管疾病預防指引 |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | 臨床研究 | J Clin Lipidol | Atorvastatin 用於 6–17 歲雜合子 FH 兒童與青少年，3 年療效與安全性 |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | 臨床比較研究 | Nutr Metab Cardiovasc Dis | 雜合子 FH 中比較 atorvastatin 與 simvastatin 達成 LDL-C 目標的能力 |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | 臨床研究 | Echocardiography | Atorvastatin 改善無冠狀動脈粥樣硬化證據的 FH 患者心肌與周邊血流 |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Atorvastatin 治療原發性高膽固醇血症與混合型血脂異常的療效與安全性回顧 |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | 純合子 FH 降 LDL-C 新藥治療進展 |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | 回溯性研究 | Atherosclerosis | 斯洛伐克 FH 治療現況：最大劑量強效他汀是基石，但仍有許多患者未達標 |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | 基礎研究 | Toxicology | 以 FH 患者 iPSC 骨骼肌細胞比較親脂性與親水性他汀的肌毒性差異 |
| [40874855](https://pubmed.ncbi.nlm.nih.gov/40874855/) | 2026 | 真實世界研究 | J Clin Res Pediatr Endocrinol | 土耳其兒童雜合子 FH 的基因與治療real-world 經驗 |

## 香港上市資訊

香港共有 20 張 atorvastatin 許可證，以下列出 5 張。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57246 | LIPIGET TAB 20MG | CHARIOT PHARMA LIMITED |
| HK-66318 | ATORVASTATIN TABLETS 20MG | CONTROLLED MEDICATIONS LIMITED |
| HK-60719 | ATOTY FC TAB 10MG | KAI YUEN PHARMACEUTICAL CO |
| HK-67373 | CHLOVAS-20 TABLETS 20MG | MEDILINE (HONG KONG) COMPANY LIMITED |
| HK-42330 | LIPITOR TAB 40MG | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
FH 有多個已完成的 Phase 3 試驗，並有系統性回顧與指引支持他汀在 FH 的角色，機轉也明確。但多數試驗以 atorvastatin 為背景治療，且原適應症與安全性資料缺漏，因此需設條件推進。

**若要推進需要：**
- 取得香港衛生署許可證的仿單，補齊核准適應症、警語與禁忌症（此為目前的阻斷性資料缺口）
- 確認 FH 是否已在現有許可證的適應症內，以判斷這是既有適應症還是真正的新用途
- 補充 DrugBank 的作用機轉資料
- 若考慮兒童族群，參考 NCT00827606 與 PMID 27678432 的長期生長發育與安全性資料

**其他預測適應症（僅供參考）：**
- HIV 感染（L2，Research Question）：證據多為 HIV 共病與發炎、動脈粥樣硬化等替代指標，並非抗病毒療效，且需留意與抗反轉錄病毒藥物的交互作用
- 腦幹梗塞（L4，Hold）：僅有間接證據
- CETP 缺乏症、CYP7A1 缺乏所致高膽固醇血症、伴共濟失調步態之神經發展障礙（皆為 L5，Hold）：缺乏直接證據，高分較可能反映知識圖譜的鄰近性

本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

