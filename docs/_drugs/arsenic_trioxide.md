---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide（三氧化二砷）：從未載明適應症到未分類骨髓增生異常症候群

## 一句話總結

Arsenic Trioxide 是一種抗腫瘤藥物，香港現有 1 張口服溶液許可證（Arsenol），但許可證資料未載明核准適應症。
TxGNN 預測它可能對**未分類骨髓增生異常症候群 (Unclassified Myelodysplastic Syndrome)** 有效，預測分數很高，但**這個亞型本身沒有任何臨床試驗或文獻**，只能間接引用上層「骨髓增生異常症候群 (MDS)」的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 未分類骨髓增生異常症候群 (Unclassified Myelodysplastic Syndrome) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5（僅有模型預測；上層 MDS 條目另有間接證據，見下文） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻，Arsenic Trioxide 在血液惡性腫瘤中的作用包括：
- 誘導細胞凋亡（調節 BCL2 家族基因、NF-κB/FLIP 路徑）
- 促進細胞分化
- 抗血管新生

這些作用主要來自 MDS 的離體與細胞研究。

模型分數很高，較可能是因為藥物在 MDS 與血液惡性腫瘤中的已知活性，並非來自這個亞型的直接證據。「未分類 MDS」是 MDS 的一個分類項目，因此上層 MDS 的證據可以作為間接支持，但不能直接視為此亞型有效。

值得注意的是，一項招募中的 Phase 2 試驗（NCT06778187）使用口服 Arsenic Trioxide（Arsenol®），與香港許可證的品名相符。不過試驗族群是 TP53 突變的髓系惡性腫瘤，並非未分類 MDS。

## 臨床試驗證據

**此亞型：** 目前無相關臨床試驗登記。

**間接證據（上層 MDS 條目，列出最相關的 10 項）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | 招募中 | 24 | 口服 Arsenic 用於 ESA 與 luspatercept 治療失敗的低風險 MDS，劑量遞增與擴展 |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | 招募中 | 30 | 口服 Arsenic Trioxide（Arsenol®）加維生素 C 與低強度治療，用於 TP53 突變髓系惡性腫瘤 |
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | 已終止 | 55 | Arsenic Trioxide 加維生素 C 用於 MDS，是 MDS 專屬砷劑組合中最大的一組 |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | 已完成 | 7 | Decitabine、Arsenic Trioxide 與維生素 C 的先導試驗，評估安全性 |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | 已完成 | 13 | 靜脈 Decitabine 加 Arsenic Trioxide 與維生素 C，用於 MDS 與 AML |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | 已完成 | 30 | Arsenic Trioxide 加 gemtuzumab ozogamicin 用於進展期 MDS |
| [NCT00274820](https://clinicaltrials.gov/study/NCT00274820) | Phase 2 | 已完成 | 15 | Thalidomide、Arsenic Trioxide、Dexamethasone 與維生素 C 組合，用於骨髓纖維化或 MDS/MPN 重疊疾病 |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | 已終止 | 60 | Arsenic Trioxide 加 Thalidomide 用於各風險等級 MDS，療效未獲確認 |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | 已完成 | 92 | 隨機比較 Decitabine、Decitabine 加 Carboplatin、Decitabine 加 Arsenic，用於復發難治或年長 AML/MDS |
| [NCT03377725](https://clinicaltrials.gov/study/NCT03377725) | Phase 3 | 已撤回 | 0 | Decitabine 加 Arsenic Trioxide 對比單用 Decitabine，因零收案而無任何證據 |

## 文獻證據

**此亞型：** 目前無相關文獻。

**間接證據（上層 MDS 條目，列出最相關的 10 篇）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | 系統性回顧／網絡統合分析 | Hematology | 系統性評估含 Arsenic Trioxide 方案對 MDS 的療效與不良事件，並探討最佳組合；既有試驗樣本小且結論不一 |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | 回溯性臨床研究 | Hematology | Decitabine 加 Arsenic Trioxide 用於年長高風險 MDS，評估療效與安全性 |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase I/II 臨床研究 | Leuk Res | Arsenic Trioxide 加低劑量 cytarabine，49 位中高風險 MDS 患者，完全緩解率 17%，4 週內死亡率 8% |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | 臨床研究 | Leuk Res | Arsenic Trioxide、Thalidomide 與 retinoic acid 組合用於較高風險 MDS |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Curr Hematol Malig Rep | Arsenic Trioxide 具促凋亡、抗增殖、抗血管新生作用，可用於包含 MDS 的血液惡性腫瘤 |
| [15610661](https://pubmed.ncbi.nlm.nih.gov/15610661/) | 2005 | Review | Curr Hematol Rep | 同一作者的早期回顧，整理單用與合併治療的 MDS 經驗 |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clin Lymphoma Myeloma | Arsenic Trioxide 在急性前骨髓細胞白血病中效果顯著，並回顧其在白血病與 MDS 的新數據 |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | 離體研究 | J Hematol Oncol | Arsenic Trioxide 對 MDS 患者的有效率約 20%；治療前後骨髓比較顯示 BCL2 家族凋亡基因表現改變 |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | 機轉研究 | Blood | 探討 NF-κB 與 FLIP 在 Arsenic Trioxide 誘導 MDS 細胞凋亡中的角色 |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | 前臨床（小鼠） | Immunopharmacol Immunotoxicol | 比較雄黃（口服砷劑）與 Arsenic Trioxide（靜脈砷劑）在 MDS 小鼠模型的免疫變化 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59724 | ARSENOL ORAL SOLUTION 1MG/ML | 口服溶液（依品名） | 資料未載明 |

製造商為 Unicorn Laboratories（American Unicorn Laboratories Limited）。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗腫瘤藥物，作用涉及促凋亡與分化誘導 |
| 監測項目 | 心電圖（QT 間期）、電解質、血液常規（CBC）、肝腎功能 |
| 骨髓抑制風險、致吐性分級、處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **心臟毒性**：證據包中的機轉評估提到需關注 QT 間期延長與砷毒性，尤其在非惡性腫瘤族群。
- **藥物交互作用**：查詢無結果。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 「未分類 MDS」這個亞型只有模型預測（L5），沒有直接的試驗或文獻。
- 上層 MDS 的證據相對豐富，包括多個 Phase 1/2 試驗、2023 年系統性回顧與 2025 年的回溯研究，但多為單臂研究，多項已終止，唯一的 Phase 3 因零收案而撤回，尚無隨機確認性證據。
- 香港仿單資料尚未取得，安全性篩查無法進行。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與核准適應症（此為阻擋項）
- 補充 DrugBank 的作用機轉資料
- 把評估重心轉到上層「骨髓增生異常症候群」條目，該條目證據等級較高、建議為 Research Question 階段
- 確認未分類 MDS 是否納入現有 MDS 試驗的收案條件（例如 NCT06670222）
- 制定 QT 間期與電解質的監測計畫

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

