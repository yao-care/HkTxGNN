---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Dexamethasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dexamethasone：從全身性糖皮質素到圓形禿

## 一句話總結

Dexamethasone 是強效糖皮質素（類固醇），在香港已有多張上市許可證。
TxGNN 模型預測它可能對**圓形禿 (Alopecia Areata)** 有效。
目前有 **1 篇隨機對照試驗、多篇世代研究與 1 篇系統性回顧／網絡統合分析**支持這個方向，但**沒有相關的臨床試驗登記**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 圓形禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2（僅 1 篇小型 RCT，期別未確認，保守看待介於 L2–L3） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。根據已知資訊，Dexamethasone 是強效糖皮質素，可抑制免疫反應。

圓形禿是 T 細胞介導的自體免疫性毛囊攻擊。Dexamethasone 可抑制這種免疫攻擊，並協助恢復毛囊的免疫豁免狀態。這也是全身性類固醇脈衝療法用於圓形禿的公認理由。

文獻中有口服 Dexamethasone 小劑量脈衝（mini-pulse）的 RCT、多個前瞻性與回溯性世代研究，以及比較全身性類固醇與 JAK 抑制劑的統合分析。JAK 抑制劑無法使用或取得困難時，類固醇脈衝是常見的替代方案。

## 臨床試驗證據

系統以藥名比對出的登記試驗**全部是腫瘤研究，沒有任何一項支持圓形禿適應症**。以下列出其中 10 項供參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | 未知 | 74 | 口服類固醇預防 regorafenib 引起的疲倦與不適（用類固醇，但與落髮無關） |
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | 未知 | 118 | 多發性骨髓瘤：Pomalidomide＋Dexamethasone±Ixazomib（Dexamethasone 為背景用藥） |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | 完成 | 56 | 新診斷多發性骨髓瘤：Durvalumab＋Lenalidomide±Dexamethasone 劑量探索 |
| [NCT01055496](https://clinicaltrials.gov/study/NCT01055496) | Phase 1 | 完成 | 103 | 非何杰金氏淋巴瘤：Inotuzumab 合併 R-CVP 或 R-GDP（不相關） |
| [NCT05408026](https://clinicaltrials.gov/study/NCT05408026) | Phase 1/2 | 撤回 | 0 | 復發／難治性多發性骨髓瘤四藥合併（不相關） |
| [NCT02773030](https://clinicaltrials.gov/study/NCT02773030) | Phase 1/2 | 進行中（不招募） | 466 | 多發性骨髓瘤：CC-220 單用或合併 Dexamethasone（不相關） |
| [NCT00282087](https://clinicaltrials.gov/study/NCT00282087) | Phase 2 | 完成 | 47 | 子宮平滑肌肉瘤輔助化療（不相關） |
| [NCT01126736](https://clinicaltrials.gov/study/NCT01126736) | Phase 1/2 | 完成 | 98 | 非小細胞肺癌：Eribulin＋Pemetrexed（不相關） |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | 完成 | 24 | 復發膠質母細胞瘤：Cabazitaxel（不相關） |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | 完成 | 19 | 惡性間皮瘤：Cisplatin＋Pemetrexed＋Imatinib（不相關） |

## 文獻證據

以下依證據強度排序（RCT > 系統性回顧／統合分析 > 世代研究 > 個案）。部分摘要在資料中被截斷，所以只摘要可確認的內容。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | 30 名嚴重、非進行期的兒童圓形禿，比較口服 Dexamethasone mini-pulse 與 DPCP 接觸敏化療法的療效與安全性（開放label；摘要中未見結果數據） |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | 系統性回顧／網絡統合分析 | Arch Dermatol Res | 比較全身性類固醇、口服 JAK 抑制劑與接觸免疫療法用於重度圓形禿的療效與安全性 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | 回顧兒童圓形禿脈衝式類固醇的劑量方案、給藥方式與副作用，指出劑量方案尚未建立共識 |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | 前瞻性世代 | J Clin Med | 真實世界評估 Dexamethasone mini-pulse 的療效、安全性與反應相關因子 |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | 多中心世代 | Dermatologic Therapy | 口服 Dexamethasone mini-pulse 用於中重度圓形禿；JAK 抑制劑成本高、可近性低，因此類固醇仍有需求 |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | 前瞻性世代 | Dermatologic Therapy | 73 名重度兒童圓形禿，比較 1 天與 3 天靜脈 Dexamethasone 脈衝，併用外用 Clobetasol |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | 世代（長期追蹤） | Dermatologic Therapy | 65 名兒童／青少年，口服 Dexamethasone 每 4 週一次併用外用類固醇，追蹤中位數 96 個月 |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | 比較研究 | Dermatology | 比較三種全身性類固醇給藥方式的療效、復發率與副作用 |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | 臨床研究 | J Dermatol | 30 名廣泛性圓形禿，每週連續 2 天口服 5 mg Dexamethasone 脈衝 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | 個案報告 | J Dermatol Treat | JAK 抑制劑不適用時，口服 Dexamethasone mini-pulse 使重度圓形禿達到長期緩解 |

## 香港上市資訊

資料庫中共 20 張許可證，以下列出 5 張。許可證資料未提供劑型與核准適應症文字，因此僅列出可確認的欄位。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-25481 | DEXAMED TAB 0.5MG | STAR MEDICAL SUPPLIES LTD |
| HK-45805 | DEXAMETHASONE TAB 0.5MG (PENTAGON) | MEYER PHARMACEUTICALS LTD |
| HK-05188 | DEXMETHA TAB 0.5MG | SYNCO (H.K.) LIMITED |
| HK-06450 | DEXASONE TAB 0.5MG | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-62402 | TRANKALDEX TABLETS 0.5MG | EUROPHARM LAB CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 篇 RCT、多個世代研究與 1 篇統合分析，且機轉合理。但 RCT 規模小（30 名兒童）且為開放label，登記試驗中也沒有直接支持的研究，因此需要設限地推進。
- 停藥後復發常見。長期全身性類固醇有毒性風險，包括下視丘－腦下垂體－腎上腺軸（HPA 軸）抑制，以及骨骼、代謝與兒童生長方面的影響。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症（目前缺漏，屬阻擋性缺口，無法進入安全性篩選）。
- 補齊 DrugBank 的作用機轉資料。
- 確認 PMID 36086930 RCT 的期別、設計與結果數據。
- 制定劑量上限、療程長度與監測計畫（HPA 軸、骨密度、血糖、兒童生長），並與 JAK 抑制劑做比較。
- 其餘 9 個預測適應症（如禿髮性黏蛋白沉積症、休止期落髮、禿髮性毛囊炎等）目前僅有模型預測、缺乏實證，均為 L5／Hold，暫不推進。所有預測分數都接近飽和（約 0.99），不具區辨力。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

