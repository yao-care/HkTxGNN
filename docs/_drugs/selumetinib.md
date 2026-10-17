---
layout: default
title: Selumetinib
parent: 僅模型預測 (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Selumetinib：預測新適應症為週邊神經鞘瘤 (Peripheral nerve schwannoma)（證據等級 L5）。原適應症：神經纖維瘤 (neurofibromatosis)"
monitor_inn: "Selumetinib"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "rhabdoid tumor", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "acromelanosis", "Moynahan syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "peripheral nerve schwannoma", "trigeminal schwannoma"]
---

# Selumetinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Selumetinib：從神經纖維瘤到週邊神經鞘瘤（NF2 相關）

## 一句話總結

Selumetinib 是一種 MEK 抑制劑，原本用於治療神經纖維瘤 (neurofibromatosis)。
TxGNN 模型預測的首位新適應症為家族性泛發性雀斑樣痣，但證據最完整的方向是**週邊神經鞘瘤 (Peripheral nerve schwannoma)**，目前有 **3 個臨床試驗**和 **6 篇文獻**與此方向相關，但尚無已完成且具療效結果的試驗。

> 說明：依預測排名，第 1 名（家族性泛發性雀斑樣痣）僅有模型預測，無任何試驗或文獻。為使報告具決策價值，下文以證據最充分的第 9 名「週邊神經鞘瘤」為主要評估對象，其他預測於快速總覽後簡要列出。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 神經纖維瘤 (neurofibromatosis)（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 週邊神經鞘瘤 (Peripheral nerve schwannoma)（預測排名第 9） |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L3（僅有綜述與病例報告，無已完成的 RCT；嚴格依規則，臨床層面證據仍薄弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（研究性問題，待更多資料） |

**其他高分預測概況：**

| 預測疾病 | 分數 | 證據等級 | 狀況 |
|---------|------|---------|------|
| 家族性泛發性雀斑樣痣 | 99.96% | L5 | 僅模型預測，RAS/MAPK 路徑關聯合理但無證據 |
| 胃皮膚症候群 | 99.96% | L5 | 僅模型預測 |
| 橫紋肌樣腫瘤 (Rhabdoid tumor) | 99.96% | L4 | 有 1 個廣泛篩選試驗與 1 篇前臨床文獻 |
| 先天性多發咖啡牛奶斑—姊妹染色分體交換增加症候群 | 99.96% | L5 | 僅模型預測 |
| 肢端黑變病 | 99.96% | L5 | 僅模型預測 |
| 三叉神經鞘瘤 | 99.95% | L5 | 僅模型預測，由鞘瘤證據推論 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Selumetinib 是 MEK1/2 抑制劑，用於神經纖維瘤（與 RAS/MAPK 路徑活化有關）。其在原適應症中的角色，機轉上可能延伸到同樣涉及此路徑的神經鞘腫瘤。

NF2 相關神經鞘瘤病 (NF2-SWN) 的鞘瘤與 merlin 蛋白缺失有關，會導致下游 RAS/RAF/MEK/ERK 路徑活化。2024 年一篇發表於 Nature Communications 的研究指出，NF1 與 NF2 兩種腫瘤抑制基因在許旺氏細胞腫瘤中存在功能交互作用，為使用 MEK 抑制劑提供了合理的生物學基礎。另有一篇病例報告顯示，selumetinib 在 NF2 相關室管膜瘤患者中達到部分緩解。

不過，這些屬於間接或個案層級的證據。唯一直接以 selumetinib 治療 NF2 相關腫瘤的 Phase 2 試驗提前終止，僅收案 10 人，無法得出療效結論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03095248](https://clinicaltrials.gov/study/NCT03095248) | Phase 2 | 已終止 | 10 | Selumetinib 用於 NF2 相關腫瘤，評估腫瘤是否停止生長及聽力變化；僅收案 10 人，未提供結果，無法支持療效結論 |
| [NCT07707947](https://clinicaltrials.gov/study/NCT07707947) | Phase 2 | 尚未招募 | 20 | 單中心單臂試驗，以 MEK1/2 抑制劑治療 NF2 相關神經鞘瘤病（標題顯示為 MEK 抑制劑，具體藥物未能確認即為 selumetinib），預計 2026 年 7 月開始 |
| [NCT07713745](https://clinicaltrials.gov/study/NCT07713745) | Phase 2 | 尚未招募 | 200 | PRIME-NF2 平台型試驗，涵蓋前庭神經鞘瘤、非前庭神經鞘瘤、腦膜瘤與室管膜瘤；具體試驗組別尚未公布 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37906356](https://pubmed.ncbi.nlm.nih.gov/37906356/) | 2023 | Review | Current Oncology Reports | 回顧 NF1、NF2 與神經鞘瘤病的中樞及週邊神經系統腫瘤處置，指出 MEK 抑制劑的進展 |
| [37046591](https://pubmed.ncbi.nlm.nih.gov/37046591/) | 2023 | 專家共識 | Cancers | EURACAN 對週邊與顱神經腫瘤的診斷與治療建議；因疾病罕見，證據偏少 |
| [38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/) | 2023 | 病例報告 | Mol Ther Methods Clin Dev | NF2 相關室管膜瘤患者使用 selumetinib 後達部分緩解 |
| [38216572](https://pubmed.ncbi.nlm.nih.gov/38216572/) | 2024 | 前臨床 | Nature Communications | NF1 與 NF2 腫瘤抑制基因的功能交互作用與許旺氏細胞腫瘤去分化及治療抗性有關 |
| [33835000](https://pubmed.ncbi.nlm.nih.gov/33835000/) | 2020 | 病例報告 | Acta Dermatovenerol Croat | 無 NF1 的叢狀神經纖維瘤，與療效關聯有限 |
| [40861330](https://pubmed.ncbi.nlm.nih.gov/40861330/) | 2025 | 病例報告 | Surgical Case Reports | NF1 相關巨大縱膈腔神經鞘瘤的手術處置，與藥物療效關聯有限 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67363 | KOSELUGO CAPSULES 25MG | 膠囊 | 未提供 |
| HK-67362 | KOSELUGO CAPSULES 10MG | 膠囊 | 未提供 |

兩張許可證均為單方、有效，持有者為 ASTRAZENECA HONG KONG LIMITED。

---

## 細胞毒性

Selumetinib 屬標靶藥物（MEK 抑制劑），用於腫瘤相關疾病。目前所編整的資料缺乏細胞毒性相關內容，請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：共查得 84 筆交互作用。列出的 20 筆中，**重大 (Major)** 等級包括：
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Cobicistat

  **中度 (Moderate)** 等級包括多種抗凝血／抗血小板藥物（如 apixaban、dipyridamole、cilostazol、betrixaban、bivalirudin、cangrelor、abciximab、acetylsalicylic acid），以及 cimetidine、clotrimazole、deferasirox 等。合併使用抗凝血或抗血小板藥物時需特別留意出血風險。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 週邊神經鞘瘤的預測有合理的 RAS/MAPK 機轉基礎，但直接臨床證據不足：唯一的 selumetinib 試驗提前終止且僅收 10 人，其餘兩項試驗尚未開始招募。
- 其他高分預測多數僅為模型輸出，沒有試驗或文獻支持。

**若要推進需要：**
- 追蹤 NCT07707947 與 NCT07713745 的啟動與結果，並確認 NCT03095248 是否有任何已發表數據
- 取得詳細的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症，完成安全性初篩
- 釐清香港核准適應症文字，以確認與預測適應症之間的差距
- 針對 84 筆交互作用（特別是強效 CYP3A4 抑制劑與抗凝血藥物）擬定用藥監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

