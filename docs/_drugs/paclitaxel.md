---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 643
evidence_level: L5
indication_count: 5
---

# Paclitaxel
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

# Paclitaxel：從原適應症（許可證未載明）到女性乳癌

## 一句話總結

Paclitaxel 是紫杉烷類（taxane）細胞毒性抗腫瘤藥物，香港已有 17 張許可證，但許可證資料未載明原適應症。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **50 個臨床試驗**支持，其中包含多個已完成的 Phase 3 試驗。
本次資料未收錄相關文獻（0 篇）。乳癌其實是 paclitaxel 的既有臨床用途，較接近「標準治療的驗證」，而非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L1（資料包原判 L2，依下方說明上修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

證據等級說明：
- 資料包原判 L2，原因是 NCT00281658 的標題被截斷，無法確認 paclitaxel 是否為核心治療組。
- 但 NCT00553358（NeoALTTO）的簡介明確寫出各組皆為 paclitaxel 組合，NCT00004067 的方案（AC→Taxol ± Herceptin）也包含 Taxol。
- 這兩個試驗都是已完成的 Phase 3 隨機試驗，加上 NCT00281658 共 3 個，符合 L1「≥2 個已完成 Phase 3 RCT」的條件。
- 這些試驗檢驗的是組合療法，paclitaxel 單獨的貢獻無法分離。

## 為什麼這個預測合理？

Paclitaxel 的作用機轉是穩定微管（microtubule），使快速分裂的腫瘤細胞停滯在有絲分裂期並走向凋亡。資料包的 MOA 欄位本身是空的，上述機轉描述來自資料包的預測推理內容。

這個機轉不依賴荷爾蒙受體訊號，所以在雌激素受體陰性、三陰性乳癌，以及荷爾蒙治療失效的情況下，仍是常用的細胞毒性骨幹藥物。在乳癌中，它的使用場景包括：

- 與 HER2 標靶藥物（trastuzumab、pertuzumab、lapatinib）併用。
- 與免疫檢查點抑制劑（atezolizumab、pembrolizumab）併用。
- 在 AC-T 等輔助或新輔助化療方案中使用。

資料包中的預測結果顯示，乳癌的不同亞型（ER 陰性、ER 陽性、荷爾蒙抗性）都獲得高分預測與臨床試驗支持。

## 臨床試驗證據

以下列出 10 個最相關的試驗（共 50 個），優先列已完成的 Phase 3 與 paclitaxel 為主要治療或對照組者。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | 完成 | 444 | 隨機雙盲，lapatinib + paclitaxel 對比安慰劑 + paclitaxel，用於 ErbB2 擴增的轉移性乳癌 |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | 完成 | 455 | Neo ALTTO：新輔助 lapatinib、trastuzumab 或兩者合併，皆加 paclitaxel，用於 HER2 陽性乳癌 |
| [NCT00004067](https://clinicaltrials.gov/study/NCT00004067) | Phase 3 | 完成 | 2130 | AC→Taxol 對比 AC→Taxol + Herceptin，用於淋巴結陽性且 HER2 過度表現的乳癌 |
| [NCT00005581](https://clinicaltrials.gov/study/NCT00005581) | Phase 3 | 未知 | 1000 | Epirubicin + paclitaxel 對比 CEF，用於淋巴結陽性乳癌的輔助治療 |
| [NCT02954055](https://clinicaltrials.gov/study/NCT02954055) | Phase 2 | 完成 | 140 | 隨機試驗，節拍式口服化療（VEX）對比每週 paclitaxel，用於 ER 陽性/HER2 陰性轉移性乳癌 |
| [NCT02301988](https://clinicaltrials.gov/study/NCT02301988) | Phase 2 | 完成 | 151 | 雙盲，ipatasertib + paclitaxel 對比安慰劑 + paclitaxel，用於早期三陰性乳癌的新輔助治療 |
| [NCT05189067](https://clinicaltrials.gov/study/NCT05189067) | Phase 2/3 | 未知 | 190 | 輔助 paclitaxel + trastuzumab 對比 docetaxel + trastuzumab，用於 I 期 HER2 陽性乳癌 |
| [NCT00006256](https://clinicaltrials.gov/study/NCT00006256) | Phase 2 | 完成 | 44 | Paclitaxel 同步乳房放射治療，用於早期乳癌（規模小、年代較早） |
| [NCT03096418](https://clinicaltrials.gov/study/NCT03096418) | Phase 4 | 招募中 | 50 | 新輔助每週 paclitaxel 與療效生物標記，檢驗染色體不穩定性假說 |
| [NCT03799679](https://clinicaltrials.gov/study/NCT03799679) | Phase 4 | 未知 | 60 | Nab-paclitaxel 接續高劑量 epirubicin + cyclophosphamide，用於三陰性乳癌的新輔助治療 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 17 張許可證，以下列出 5 張。資料來源未提供劑型與核准適應症欄位，劑型欄為依品名判讀。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68100 | PACLITAXEL ADVAGEN CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/50ML | 輸注用濃縮液 | 未載明 |
| HK-68817 | PAZENIR POWDER FOR DISPERSION FOR INFUSION 100MG | 輸注用分散粉末 | 未載明 |
| HK-60886 | PACLITAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/16.7ML | 輸注用濃縮液 | 未載明 |
| HK-61437 | PAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/16.7ML | 輸注用濃縮液 | 未載明 |
| HK-59318 | SINDAXEL 6MG/ML (100MG) CONC FOR SOL FOR INFUSION | 輸注用濃縮液 | 未載明 |

## 細胞毒性

Paclitaxel 屬於傳統細胞毒性化療藥物（紫杉烷類）。以下為依藥物類別的判斷，資料包未提供 DrugBank toxicity 資料。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類、微管穩定劑） |
| 骨髓抑制風險 | 中至高（嗜中性白血球減少為主要劑量限制毒性） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類）、肝功能、周邊神經病變症狀、過敏反應 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

實際警語與注意事項請以原廠仿單為準。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乳癌多個亞型都有已完成的 Phase 3 隨機試驗與多個 Phase 2 試驗，paclitaxel 作為骨幹或對照組，證據充分，但這些試驗多為組合療法。
- 香港仿單的警語與禁忌資料缺失（資料缺口 DG001，嚴重度為 Blocking），在補齊前不宜進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 補上許可證的核准適應症文字，確認香港是否已核准乳癌。
- 補上 DrugBank 的作用機轉與原適應症資料。
- 確認 NCT00281658 中 paclitaxel 是否為核心治療組。
- 區分不同亞型的定位：ER 陽性乳癌在可行時通常優先考慮內分泌治療加 CDK4/6 抑制劑，化療為次選。
- TxGNN 另一個預測「Ehrlich tumor carcinoma」是小鼠移植腫瘤模型，僅有前臨床證據，不屬人類適應症，建議列為 Hold。

本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

