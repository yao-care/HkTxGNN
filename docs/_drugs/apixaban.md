---
layout: default
title: Apixaban
parent: 中證據等級 (L3-L4)
nav_order: 65
evidence_level: L4
indication_count: 10
---

# Apixaban
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Apixaban：從抗凝血治療到偏頭痛

## 一句話總結

Apixaban 是口服 Xa 因子抑制劑（抗凝血藥）。TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前只有 **1 個間接相關的臨床試驗**和 **4 篇文獻**，且現有病例報告顯示 apixaban 無效，甚至可能使症狀惡化。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.02% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，apixaban 是選擇性 Xa 因子抑制劑，屬於直接口服抗凝血劑（DOAC），機轉上與偏頭痛沒有直接關聯。

唯一的假說是間接的。伴隨先兆的偏頭痛可能與卵圓孔未閉（PFO）或抗磷脂抗體相關的微栓塞事件有關，抗凝血治療或許能減少這類事件。有病例報告指出，warfarin、heparin 等抗凝血藥曾使部分偏頭痛患者症狀緩解。

不過這個假說目前缺乏支持。Apixaban 相關的兩份病例報告都不利：一例在改用 apixaban 後偏頭痛復發，換回 warfarin 又緩解；另一例在開始使用 apixaban 後偏頭痛惡化。因此 99% 的模型分數不宜直接解讀為臨床上有前景。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | 完成 | 664 | 比較 PFO 封堵、抗凝血藥與抗血小板藥預防中風復發。終點是中風，不是偏頭痛，也非 apixaban 專屬試驗，沒有偏頭痛療效資料 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | 回溯性研究（75 人） | Lupus | 難治型偏頭痛合併抗磷脂抗體的患者，探討抗血栓治療的反應。藥物細節不明，不是 apixaban 專屬 |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | 病例報告＋文獻回顧 | The Neurologist | 伴隨先兆的偏頭痛在開始使用 apixaban 後惡化。DOAC 對偏頭痛的影響文獻稀少且看法不一 |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | 病例報告 | Headache | 55 歲女性使用 warfarin 時先兆型偏頭痛緩解 12 年，改用 apixaban 3 週內復發，換回 warfarin 後數日緩解 |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | 病例報告 | Headache | 前庭型偏頭痛在使用 warfarin 與 topiramate 後緩解，非 apixaban |

## 香港上市資訊

香港共有 10 張許可證，以下列出 5 張主要許可證（資料庫未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61377 | ELIQUIS TAB 2.5MG | Pfizer Corporation Hong Kong Limited |
| HK-62094 | ELIQUIS TAB 5MG | Pfizer Corporation Hong Kong Limited |
| HK-68458 | APO-APIXABAN TABLETS 2.5MG | Hind Wing Co Ltd |
| HK-68846 | APIXABAN TABLETS 2.5MG | I & C (Hong Kong) Limited |
| HK-68847 | APIXABAN TABLETS 5MG | I & C (Hong Kong) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何試驗直接測試 apixaban 對偏頭痛的療效。唯一的臨床試驗以中風復發為終點，文獻僅有病例報告和一項藥物不明的回溯性研究。
- 現有 apixaban 病例顯示無效或可能惡化，機轉假說也很薄弱，證據等級僅為 L4。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料，這是進入安全性篩選的前提。
- 補充 apixaban 的作用機轉資料（如 DrugBank）。
- 針對特定族群（如 PFO 或抗磷脂抗體陽性的先兆型偏頭痛）進行系統性文獻回顧，釐清抗凝血劑類別效應與 apixaban 是否有差異。
- 在此之前，不建議投入偏頭痛的臨床開發。

**補充觀察：** 其他預測適應症中，類風濕性關節炎 (rheumatoid arthritis) 有前臨床研究（PMID 32141012）顯示 apixaban 透過抑制 FXa 相關的 JAK2/STAT3 與 MAPK 訊號而有抗關節炎作用，機轉上比偏頭痛更連貫。但仍缺乏人體療效資料，可列為後續研究問題。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

