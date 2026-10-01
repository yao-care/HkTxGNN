---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 5
---

# Pemetrexed
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

# Pemetrexed：從來源資料未列載的原適應症，到惡性腹膜間皮瘤

## 一句話總結

Pemetrexed（培美曲塞）是多標的抗葉酸類化療藥，來源資料未記載原適應症。
TxGNN 模型預測它可能對**惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma)** 有效，
目前有 **10 個臨床試驗**和 **20 篇文獻**支持這個方向，但多為合併療法試驗、回溯性研究與綜述，缺乏腹膜專一的隨機對照證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3（資料包標示 L2，但腹膜適應症無已完成的 Phase 2/3 RCT，僅有單臂 Phase 2 與回溯性研究，依判定規則降為 L3） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

註：原適應症欄位在來源資料與許可證中均為空白，故不列出。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（來源資料未收錄）。以下機轉來自一般藥理知識：Pemetrexed 抑制胸苷酸合成酶 (TS)、二氫葉酸還原酶 (DHFR) 與 GARFT，阻斷嘌呤與嘧啶合成，使快速增生的腫瘤細胞無法複製。

腹膜間皮瘤與胸膜間皮瘤組織型態相近，且都依賴葉酸路徑合成核苷酸。因此可合理推測，胸膜間皮瘤已確立的 pemetrexed + cisplatin 方案也可能適用於腹膜。文獻也佐證這個做法：Nagata 等人（2019）指出，該方案雖是胸膜間皮瘤的標準治療，並常被用於腹膜間皮瘤，但在腹膜的療效仍不明確。

同一份資料中，**胸膜間皮瘤**的證據強得多，包括已完成的 Phase 3 試驗（NCT00190762）與多篇 RCT（如 PMID 12860938）。這顯示 pemetrexed 在間皮瘤中的活性已獲驗證，也代表此預測可能更接近「適應症延伸」，而非全新發現。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | 完成 | 48 | Pemetrexed + gemcitabine 用於胸膜或腹膜間皮瘤一線治療，評估安全性、存活與腫瘤反應（本組唯一直接涵蓋腹膜的 Phase 2） |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | 招募中 | 66 | 卡鉑 + pemetrexed + bevacizumab，加或不加 atezolizumab，用於腹膜間皮瘤（隨機分組） |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | 招募中 | 28 | 信迪利單抗 + bevacizumab + pemetrexed + 順鉑，用於無法切除的腹膜間皮瘤（單臂） |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | 暫停 | 66 | PIPAC 加全身化療 vs 單用全身化療（順鉑 + pemetrexed），用於腹膜間皮瘤一線治療 |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | 招募中 | 64 | 減積手術與 HIPEC 後，比較腹腔內與靜脈化療；資料未顯示 pemetrexed 是否為受試藥 |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | 未知 | 40 | Talazoparib 於含鉑一線化療後的維持治療（胸膜或腹膜間皮瘤） |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | 進行中（不再招募） | 30 | TRC102 + 順鉑 + pemetrexed，用於晚期實體瘤或間皮瘤 |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | 完成 | 19 | 順鉑 + pemetrexed + imatinib 用於無法切除或轉移性間皮瘤，決定最大耐受劑量 |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | 終止 | 85 | ADI-PEG 20 + pemetrexed + 順鉑，多種腫瘤混合（含腹膜間皮瘤劑量遞增組） |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | 撤回 | 0 | Vorinostat + pemetrexed-順鉑，用於胸膜間皮瘤；無受試者，無資料 |

## 文獻證據

本組文獻中沒有針對腹膜間皮瘤的 RCT，以下依證據類型由強到弱排列。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | 未分類（研究設計未明） | Jpn J Clin Oncol | 評估一線順鉑 + pemetrexed 用於晚期腹膜間皮瘤的療效與安全性（摘要未呈現結果數字） |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | 回溯性研究 | Expert Rev Anticancer Ther | 回溯評估一線 pemetrexed + 順鉑在腹膜間皮瘤的療效，並指出腹膜間皮瘤的治療結果差異大 |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | 多中心研究 | Ann Surg Oncol | 分析腹膜間皮瘤的臨床病理特徵、預後與治療選項 |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | 病例報告 | BMJ Case Rep | 1 例腹膜間皮瘤初治對順鉑 + pemetrexed 反應良好，復發後再次使用仍有效 |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | 病例報告 | J Immunother | 2 例對鉑類無反應的腹膜間皮瘤，探討化療加免疫檢查點抑制劑 |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | 病例報告／世代 | Pleura Peritoneum | 雙向化療使原本無法切除的腹膜間皮瘤得以手術並接受 HIPEC |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | 腹膜間皮瘤診療路徑；CRS + HIPEC 的中位總存活為 34–92 個月，5 年存活約 20% |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | 腹膜間皮瘤治療回顧，選定病人以減積手術 + HIPEC 為首選 |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | 腹膜間皮瘤的診斷與處置，美國每年約 800 例 |
| [22104079](https://pubmed.ncbi.nlm.nih.gov/22104079/) | 2012 | Review | Cancer Treat Rev | 瀰漫性腹膜間皮瘤治療進展 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53331 | ALIMTA POWDER FOR CONC FOR SOLN FOR INF 500MG（Eli Lilly Asia） | 未提供 | 未提供 |
| HK-64687 | PEMETREXED POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG（Chemillennium International） | 未提供 | 未提供 |
| HK-66750 | PEMIREX POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG（Golden Billion Health Products） | 未提供 | 未提供 |
| HK-68928 | PEMETREXED AFT POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG（United Italian Corp） | 未提供 | 未提供 |
| HK-68755 | PEMETREXED ADVAGEN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG（Advagen） | 未提供 | 未提供 |

以上為 17 張許可證中的 5 張。品名顯示皆為輸液用濃縮粉末劑。

## 細胞毒性

以下為一般藥理分類，來源資料未提供 DrugBank toxicity 內容，正式資訊請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸代謝拮抗劑） |
| 骨髓抑制風險 | 中至高（一般藥理認知，常見嗜中性白血球減少、血小板減少、貧血） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能（腎功能不足會影響清除） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Pemetrexed + 鉑類是胸膜間皮瘤的標準方案，腹膜間皮瘤有已完成的 Phase 2、多個進行中的 Phase 2 試驗與回溯性研究支持，機轉上也合理。
- 但腹膜專一的對照證據不足，且香港仿單的警語與禁忌尚未取得（資料缺口 DG001，嚴重度為 Blocking），因此只適合附條件推進。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌與適應症文字，完成安全性篩選。
- 補充 DrugBank 的作用機轉與 toxicity 資料。
- 核對來源記錄為何缺少原適應症，因為胸膜間皮瘤已有 Phase 3 證據，此預測可能屬於已核准用途的延伸。
- 追蹤 NCT05001880、NCT06543069 等進行中的腹膜間皮瘤試驗結果。
- 區分各試驗中 pemetrexed 是受試變項還是背景化療，避免高估其單藥貢獻。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

