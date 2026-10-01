---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 1
---

# Irinotecan
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

# Irinotecan：從已上市抗腫瘤化療藥到女性乳癌

## 一句話總結

Irinotecan 是拓樸異構酶 I 抑制劑類的化療藥，在香港已有 16 張許可證，但本次資料未收錄其原核准適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前有 **20 個臨床試驗**和 **20 篇文獻**與此方向相關，但直接證據有限：多數文獻談的是 irinotecan 活性代謝物 SN-38 的抗體藥物複合體，並非 irinotecan 本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次資料未提供（香港許可證的適應症欄位皆為空白） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L2（僅有 1 個已完成的 Phase 2 隨機試驗，且為口服膠囊劑型，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，DrugBank 的 MOA 欄位是空的。以下說明來自一般藥理知識，並非資料包內容。Irinotecan 是前驅藥，經羧酸酯酶轉換為活性代謝物 SN-38。SN-38 抑制拓樸異構酶 I，造成 DNA 雙股斷裂，使快速分裂的細胞凋亡。這個機轉不限於特定組織，理論上可用於乳癌。

SN-38 在乳癌中的價值已有實例。Sacituzumab govitecan 以 SN-38 為毒性載荷，靶向 TROP-2，已用於轉移性三陰性乳癌與 HR+/HER2- 乳癌，並有 Phase 3 隨機試驗支持。

但這些證據只能證明 SN-38 這個機轉可行，不能證明全身性給予 irinotecan 本身有效，或優於現有乳癌療法。早期文獻（2003 年）也指出 irinotecan 在乳癌中僅有「邊緣活性」。因此這個預測目前較適合視為研究問題，而非可直接應用的結論。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | 完成 | 134 | 已接受 anthracycline、taxane、capecitabine 治療失敗的轉移性乳癌，比較 irinotecan 膠囊 2 種給藥時程（每日 5 天 vs 14 天）；資料包未附療效結果 |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | 未知 | 124 | 中國患者，晚期或轉移性乳癌三線以後單藥 irinotecan，單臂試驗；狀態未知，結果可能未發表 |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | 完成 | 12 | 晚期乳癌先給 irinotecan 再給 capecitabine，評估副作用與最佳劑量 |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | 完成 | 41 | UCN-01 併用 irinotecan，用於難治實體瘤及三陰性乳癌；提供併用安全性資料，但非乳癌專屬 |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | 完成 | 45 | 奈米脂質體 irinotecan (MM-398) 的腫瘤藥物濃度與 ferumoxytol MRI 可行性；劑型不同，族群未確認為乳癌 |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | 未知 | 180 | Navicixizumab 單用或併用 paclitaxel／irinotecan 的籃式試驗，含三陰性乳癌世代 |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | 完成 | 515 | Sacituzumab govitecan（SN-38 抗體藥物複合體）用於多種上皮癌；間接證據 |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | 完成 | 21 | SN-38 奈米粒子製劑 SNB-101 用於晚期實體瘤；間接證據 |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | 完成 | 38 | Irinotecan 併用 gemcitabine 用於實體瘤；非乳癌專屬 |

說明：NCT00072852 是目前最直接的證據，但它使用口服膠囊，而香港已登記的是輸注用濃縮液，劑型不同。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 | Eur J Cancer | PHENOMENAL 研究：脂質體 irinotecan 用於 HER2 陰性乳癌合併腦轉移，該製劑可穿越血腦屏障（間接，劑型不同） |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | Phase 3 RCT | J Clin Oncol | Sacituzumab govitecan 用於 HR+/HER2- 轉移性乳癌（間接，為 SN-38 抗體藥物複合體） |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 1/2 | N Engl J Med | Sacituzumab govitecan 用於難治轉移性三陰性乳癌（間接） |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | 單臂試驗 | J Clin Oncol | Sacituzumab govitecan 用於重度前治療的三陰性乳癌（間接） |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology (Williston Park) | Mitomycin 與 irinotecan 用於晚期乳癌的理論依據；兩者單用活性有限，前臨床顯示序貫給藥有協同作用 |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | 回顧 irinotecan 在淋巴瘤、白血病及乳癌等多種腫瘤的早期活性 |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Review | Breast | 針對 TROP-2 的抗體藥物複合體在轉移性乳癌的臨床發展 |
| [39768216](https://pubmed.ncbi.nlm.nih.gov/39768216/) | 2024 | Review | Cells | Sacituzumab govitecan 用於難治三陰性乳癌的回顧 |
| [31208270](https://pubmed.ncbi.nlm.nih.gov/31208270/) | 2019 | Review | mAbs | 以 irinotecan 活性代謝物 SN-38 為載荷的抗體藥物複合體案例研究 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65614 | IRINOTECAN HYDROCHLORIDE CONCENTRATE FOR SOLUTION FOR INFUSION 40MG/2ML | 輸注用濃縮液（依品名） | 未提供 |
| HK-65613 | IRINOTECAN HYDROCHLORIDE CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/5ML | 輸注用濃縮液（依品名） | 未提供 |
| HK-67415 | IRINOTECAN HYDROCHLORIDE CONCENTRATE FOR SOLUTION FOR INFUSION 40MG/2ML | 輸注用濃縮液（依品名） | 未提供 |
| HK-62948 | IRINOTECAN HYDROCHLORIDE CONCENTRATE FOR SOLUTION FOR INFUSION 40MG/2ML | 輸注用濃縮液（依品名） | 未提供 |
| HK-42884 | CAMPTO CONC FOR INFUSION 20MG/ML | 輸注用濃縮液（依品名） | 未提供 |

## 細胞毒性

以下為依藥物類別的一般判斷，資料包本身沒有毒性資料，實際內容請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（拓樸異構酶 I 抑制劑） |
| 骨髓抑制風險 | 高（嗜中性白血球減少為常見劑量限制毒性） |
| 致吐性分級 | 中 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質；需留意腹瀉與脫水 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前最直接的證據是一項 Phase 2 試驗（NCT00072852），使用口服膠囊，且資料包未附療效結果。文獻的主要支持來自 SN-38 抗體藥物複合體，屬間接證據。
- 香港仿單的警語與禁忌症資料尚未取得，被列為阻斷性缺口，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與適應症文字
- 取得 NCT00072852 與 NCT03562390 的結果，判斷單藥 irinotecan 在乳癌的實際反應率與毒性
- 從 DrugBank 補齊作用機轉資料
- 評估口服膠囊試驗結果能否推及香港現有的輸注劑型
- 與現行乳癌標準治療（含 sacituzumab govitecan）比較，確認 irinotecan 是否有臨床定位

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

