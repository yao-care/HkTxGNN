---
layout: default
title: Tiotropium
parent: 高證據等級 (L1-L2)
nav_order: 750
evidence_level: L1
indication_count: 5
---

# Tiotropium
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Tiotropium：從慢性阻塞性肺病 (COPD) 到阻塞性肺病 (Obstructive Lung Disease)

## 一句話總結

Tiotropium（原廠名 Spiriva）是一種長效毒蕈鹼受體拮抗劑（LAMA），原本核准用於慢性阻塞性肺病 (COPD) 的長期維持治療。TxGNN 模型在本次分析中將「**阻塞性肺病 (Obstructive Lung Disease)**」列為預測分數最高的候選適應症，目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個機轉關聯。但需特別說明：這項預測實質上是對藥物既有核准用途的高度重疊確認，而非傳統定義的「老藥新用」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺病 (COPD)，長效支氣管擴張維持治療 |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式登記於 DrugBank 的結構化作用機轉欄位資料，但根據本次證據收集所整合的機轉推論：Tiotropium 為長效毒蕈鹼受體拮抗劑 (LAMA)，透過阻斷氣道平滑肌 M3 受體達成支氣管擴張效果，直接對應阻塞性肺病的氣流受限病理生理機轉。

需要誠實指出的一點是：「阻塞性肺病」與 tiotropium 的原始核准適應症「COPD」在疾病本體上高度重疊，本次分析原始資料也明確標注此為「**屬藥物核心作用機轉，非典型再利用場景**」。換句話說，TxGNN 在此處的高分預測，較接近對既有已知療效的「機轉再確認」，而非發掘出真正意義上的全新適應症。

同一批預測結果中的第 4 名「COPD, severe early onset」屬於既有適應症的亞群延伸（早發重度 COPD 病人氣道平滑肌收縮機轉相同），證據等級 L2，同樣屬於合理但非新穎的延伸應用。第 5 名「chronic obstructivepulmonary disease」則直接就是 tiotropium 的核准適應症本身。

---

## 臨床試驗證據

以下為與「阻塞性肺病」關聯性最高、樣本數或設計品質最具代表性的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | 完成 | 453 | Tiotropium 5mcg Respimat 作為重度持續性氣喘 add-on 療法之隨機雙盲安慰劑對照試驗 |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | 完成 | 914 | SAFE study：一年期治療對 COPD 患者 FEV1 變化的影響 |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | 完成 | 457 | 24 週上市後療效確認，比較 tiotropium+PRN salbutamol vs 安慰劑 |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | 完成 | 5993 | 大型長期試驗，評估 tiotropium 對 COPD 肺功能下降速率的影響（UPLIFT 研究） |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | 完成 | 872 | 比較合併製劑 GSK573719/GW642444 與 tiotropium 於 COPD 之療效安全性 |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Phase 3 | 完成 | 3686 | 52 週試驗，評估三合一吸入療法對重度 COPD 之療效 |
| [NCT00463567](https://clinicaltrials.gov/study/NCT00463567) | Phase 2/3 | 完成 | 2059 | Indacaterol 劑量選擇試驗，以 tiotropium 為開放標籤活性對照 |
| [NCT02006732](https://clinicaltrials.gov/study/NCT02006732) | Phase 3 | 完成 | 809 | Tiotropium+Olodaterol 固定劑量複方於中重度 COPD 的療效評估 |
| [NCT00274014](https://clinicaltrials.gov/study/NCT00274014) | Phase 3 | 完成 | 1000 | 一年期治療對中重度 COPD 氣流受限嚴重度與惡化事件之影響 |
| [NCT02172287](https://clinicaltrials.gov/study/NCT02172287) | Phase 3 | 完成 | 623 | 六個月雙盲雙模擬試驗，比較 tiotropium、salmeterol 與安慰劑之支氣管擴張效果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | NEJM | 早期(輕中度)COPD 患者長期使用 tiotropium 可改善並延緩肺功能下降 |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Cochrane Review/Meta-analysis | Cochrane DB Syst Rev | Tiotropium vs 安慰劑於 COPD 之系統性回顧，確認療效與安全性 |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane Review | Cochrane DB Syst Rev | Tiotropium vs Ipratropium bromide 於 COPD 治療之比較性系統性回顧 |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Tiotropium 於 COPD 臨床開發歷程完整回顧 |
| [29779416](https://pubmed.ncbi.nlm.nih.gov/29779416/) | 2018 | RCT | Am J Respir Crit Care Med | SUNSET 試驗：長期三合一療法降階至 indacaterol/glycopyrronium 之隨機雙盲試驗 |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT | Lancet Respir Med | DYNAGITO 試驗：Tiotropium+Olodaterol 於預防 COPD 惡化之隨機對照試驗 |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J COPD | 台灣多中心世代研究，比較三種 LABA/LAMA 固定複方之真實世界療效 |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | Meta-analysis | Respirology | 中國 COPD 患者使用 tiotropium 之療效與安全性統合分析 |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Tiotropium bromide 藥理特性與臨床療效綜述 |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Tiotropium 機轉考量與阻塞性肺病臨床特徵綜述 |

---

## 香港上市資訊

本藥物目前於香港尚未取得上市許可（`market_status: 未上市`，許可證數：0），無可供列表之許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 「阻塞性肺病」此一預測本質上與 tiotropium 既有核准適應症（COPD）高度重疊，證據等級達 L1（50+ 個臨床試驗、含多個大型 Phase 3 RCT 如 UPLIFT n=5993），機轉關聯性明確且非投機性推論。
- 然而由於香港尚未上市（DG001：仿單警語/禁忌屬 Blocking 缺口）且正式 MOA 資料缺失（DG002：High 缺口），現階段無法完成完整的 S1 安全性初評，須先補齊資料才能進入下一階段。
- 同批預測中「respiratory malformation」與「Rienhoff syndrome」（rank 2、3）證據等級僅 L4/L5，且原始分析已標註為可能是知識圖譜嵌入雜訊（spurious association），**建議標記為 Hold，不列入積極開發清單**。

**若要推進需要：**
- 向 TFDA（或香港藥監等對應機構）取得正式仿單警語與禁忌症資料，解除 DG001 阻斷性缺口
- 透過 DrugBank API 補齊正式 MOA 描述，完成機轉關聯性分析（DG002）
- 若評估在香港申請上市，需規劃完整當地藥證申請文件與臨床橋接資料
- 對 rank 2、3 之預測結果進行人工複核，確認是否為疾病本體定義誤植或知識圖譜雜訊，避免誤導資源投入
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

