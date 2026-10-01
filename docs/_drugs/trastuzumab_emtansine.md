---
layout: default
title: Trastuzumab Emtansine
parent: 高證據等級 (L1-L2)
nav_order: 883
evidence_level: L2
indication_count: 10
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Trastuzumab emtansine：從 HER2 陽性乳癌到黃體素受體陽性乳癌

## 一句話總結

Trastuzumab emtansine（T-DM1，商品名 KADCYLA）是 HER2 標靶的抗體藥物複合體，原本用於 HER2 陽性乳癌。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，
目前有 **4 個臨床試驗**支持這個方向，**無相關文獻**。
這個預測本質上是已上市 HER2 陽性乳癌適應症中的 HR+ 亞群，不是全新的疾病領域。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（依藥理知識判斷；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位為資料缺口）。依已知藥理，T-DM1 由 trastuzumab 與微管抑制劑 DM1 組成，抗體部分會辨識 HER2，把 DM1 送入表現 HER2 的腫瘤細胞。

黃體素受體 (PR) 陽性是乳癌的荷爾蒙受體亞型，不是獨立的藥物標靶。T-DM1 是否有效取決於腫瘤是否 HER2 陽性，與 PR 狀態無關。因此這個預測的實際意義是 HER2+/HR+ 乳癌，屬於已上市適應症的一個亞群，而不是真正跨疾病的老藥新用。

需要注意，TxGNN 分數 (99.82%) 反映的是知識圖譜中的鄰近程度，本身不能證明療效。**防護條件：僅限 HER2 陽性疾病。**

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | 進行中（不再招募） | 164 | T-DM1 合併 pertuzumab 用於早期 HER2 陽性乳癌術前治療，探討 HER2 異質性的影響；族群與 HR+/HER2+ 重疊，但標題未見 PR 專屬分析 |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | 完成 | 454 | IMpassion050：atezolizumab 對照安慰劑，合併術前 ddAC-PacHP 用於早期 HER2 陽性乳癌；T-DM1 在此試驗的角色與 PR 陽性分層需人工確認 |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | 已終止 | 139 | DECRESCENDO：HER2 陽性、ER 陰性、淋巴結陰性且達 pCR 者的輔助化療降階研究；提前終止，ER 陰性族群與 PR 陽性不相符 |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | 不適用 | 完成 | 1151 | 回溯性觀察研究，估計 HER2-low 轉移性乳癌的盛行率與治療模式；僅為描述性資料，無 T-DM1 療效證據 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63487 | KADCYLA 凍乾注射粉 100mg（輸注濃縮液用） | ROCHE HONG KONG LIMITED |
| HK-63486 | KADCYLA 凍乾注射粉 160mg（輸注濃縮液用） | ROCHE HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體 (ADC)，含微管抑制劑 DM1 作為細胞毒性成分 |

骨髓抑制風險、致吐性分級、監測項目與處置防護的資料不足，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 Phase 2 與 Phase 3 試驗涵蓋 HER2 陽性乳癌，證據等級為 L2。
- 這些證據支持的是 HER2 陽性族群，並非針對 PR 陽性本身，且 T-DM1 已是 HER2 陽性乳癌的既有用藥。因此只有在限定 HER2 陽性時才適合推進。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症（目前為阻斷性資料缺口，無法進入安全性篩選）。
- 補齊作用機轉資料（可查詢 DrugBank）。
- 人工確認 NCT03726879 中 T-DM1 的角色與 PR 陽性分層，再決定證據等級能否上調。
- 針對 PR 陽性/HER2 陽性亞群做專門的文獻檢索。排名第 4 的「luminal A 或 B 乳癌」預測中，已有 HR+/HER2+ 早期乳癌的 WSG-ADAPT-TP 試驗 5 年存活報告 (PMID 36809046) 可作為起點。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

