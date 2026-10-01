---
layout: default
title: Clopidogrel
parent: 中證據等級 (L3-L4)
nav_order: 216
evidence_level: L3
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L3** | 預測適應症: **8** 個
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

# Clopidogrel：從抗血小板治療到伴腦幹先兆偏頭痛

## 一句話總結

Clopidogrel 是 P2Y12 抗血小板藥物，臨床上用於預防心血管與腦血管血栓事件。
TxGNN 模型預測它可能對**伴腦幹先兆偏頭痛 (Migraine with brainstem aura)** 有效。
目前沒有直接針對此亞型的臨床試驗，只有 **16 篇文獻**，多為觀察性研究，且集中在有卵圓孔未閉 (PFO) 的一般先兆偏頭痛患者。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 伴腦幹先兆偏頭痛 (Migraine with brainstem aura) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題） |

註：證據包內香港許可證的核准適應症文字皆為空白，因此不列「原適應症」欄。

---

## 為什麼這個預測合理？

Clopidogrel 是不可逆的 P2Y12 受體拮抗劑，屬於前驅藥，主要經 CYP2C19 代謝活化。
證據包沒有提供 DrugBank 的詳細作用機轉資料，以下說明取自預測的機轉推論。

偏頭痛先兆的可能誘發因素有兩個。
- 血小板活化及其釋放的血清素。
- 微小栓子經 PFO 等右向左分流通道造成的反常栓塞。

抗血小板藥物在理論上可以介入這兩條路徑。
另有前臨床研究指出，小膠質細胞的 P2Y12 訊號（RhoA/ROCK）參與慢性偏頭痛，但這一項屬於一般偏頭痛的機轉。

需要注意的限制：
- 現有臨床資料涵蓋的是「伴先兆偏頭痛」整體，且以 PFO 患者為主，沒有任何一項專門針對腦幹先兆亞型。
- 因此推論到此亞型屬於間接外推。
- 部分文獻其實是 PFO 封堵術（PRIMA 試驗）或其他抗血小板藥（ticagrelor、ticlopidine）的研究，並非 clopidogrel 本身。

---

## 臨床試驗證據

此預測適應症（伴腦幹先兆偏頭痛）目前無相關臨床試驗登記。

較上層的「偏頭痛 (Migraine disorder)」在預測清單中排名第 2，有下列與 clopidogrel 直接相關的試驗，可作為間接參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | 完成 | 220 | CANOA：阿斯匹靈加 clopidogrel，預防經導管 ASD 封堵術後新發偏頭痛 |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | 未知 | 50 | Clopidogrel 用於伴右向左分流的偏頭痛預防 |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | 未知 | 1000 | COMPETE：比較抗凝、抗血小板與偏頭痛專用藥物對合併 PFO 偏頭痛的效果，尚無結果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | 先導 RCT | Cephalalgia | 隨機對照先導試驗，評估 clopidogrel 預防偏頭痛（摘要未提供結果數據） |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | 系統性回顧 | Headache | 探討抗血栓藥物用於偏頭痛預防的角色 |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT（PFO 封堵，非藥物） | Eur Heart J | PRIMA：對藥物治療無效的伴先兆偏頭痛，評估經皮 PFO 封堵 |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | 世代研究 | Heart | 封堵術後抗凝方案改變與先兆偏頭痛症狀的關係，標題指出 clopidogrel 可減少症狀 |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | 世代／病例系列 | J Investig Med | 難治性偏頭痛合併 PFO，在原有預防藥物上加 clopidogrel 75 mg/日，追蹤 3、6 個月 |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | 回溯性世代 | Cephalalgia | 回顧 clopidogrel 作為右向左分流偏頭痛患者的主要治療 |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | 回溯性世代 | Neurology | 回顧 thienopyridine 類藥物用於偏頭痛合併 PFO 的仿單外使用經驗 |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | 開放標籤先導（ticagrelor，非 clopidogrel） | Neurology | TRACTOR：評估 ticagrelor 對難治性偏頭痛合併 PFO 的效果 |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | 病例系列 | J Interv Cardiol | ASD 封堵後 13 人中 5 人出現劇烈偏頭痛，給予 300 mg clopidogrel 後疼痛迅速緩解 |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | 個案報告（ticlopidine） | Cephalalgia | ASD 封堵後新發偏頭痛，ticlopidine 有效 |

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。證據包未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58832 | NORPLAT TAB 75MG | CHARIOT PHARMA LIMITED |
| HK-60493 | CLOPRA TAB 75MG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-58265 | DCLOT-75 TAB 75MG | DELTAPHARM LIMITED |
| HK-60372 | COPIDREL TAB 75MG | VIEWBEST HOLDINGS LIMITED |
| HK-66774 | LOPIGROL TABLETS 75MG | THE INTERNATIONAL MEDICAL COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

已知的一點提醒：clopidogrel 是前驅藥，主要經 CYP2C19 活化，因此併用會影響此酵素的藥物時需注意。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數很高（99.44%），但此亞型沒有任何臨床試驗，現有文獻以觀察性研究為主，證據等級為 L3。
- 較有價值的證據集中在 PFO 相關的一般先兆偏頭痛，直接外推到腦幹先兆屬於間接推論。
- 建議先列為研究問題，不進入臨床應用評估。

**若要推進需要：**
- 補充香港衛生署仿單的警語與禁忌症，這是進入安全性篩選的前提。
- 補充 DrugBank 作用機轉資料。
- 取得 CANOA（PMID 26551304、32965476）及 COMPETE 的實際結果，確認 clopidogrel 在偏頭痛的療效與出血風險。
- 查證腦幹先兆亞型是否有獨立的病例或亞群分析。
- 評估此亞型患者是否有 PFO 等右向左分流，作為可能的目標族群。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

