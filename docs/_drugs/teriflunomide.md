---
layout: default
title: Teriflunomide
parent: 高證據等級 (L1-L2)
nav_order: 734
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L1** | 預測適應症: **1** 個
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

# Teriflunomide：復發緩解型多發性硬化症（RRMS）適應症驗證案例

## 一句話總結

Teriflunomide 是口服免疫調節劑，作用機轉為抑制 DHODH 酶進而阻斷活化淋巴球的嘧啶從頭合成路徑。
TxGNN 模型預測它對**復發緩解型多發性硬化症 (RRMS)** 有效，預測分數高達 **99.24%**；
目前有 **27+ 個臨床試驗**與 **20 篇文獻**支持，證據等級達 **L1**。

> ⚠️ **重要提醒**：根據本評估附帶的機轉分析（`repurposing_rationale`）明確指出，
> 「此為原適應症而非新用途，機轉關聯已於藥理與臨床層級完整驗證」。
> 換言之，Teriflunomide（商品名 Aubagio）本身就是 RRMS 的核准用藥，
> 這個「預測」實質上是**模型準確性的驗證案例**，而非發現全新的老藥新用機會。
> 真正的商業與臨床價值在於：**此藥物目前尚未於香港上市**，若要推進屬於「新藥引進」而非「適應症擴展」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 復發緩解型多發性硬化症 (RRMS) — 原適應症資料於本評估集缺失，依機轉分析判定即為此適應症本身 |
| 預測新適應症 | Relapsing-remitting multiple sclerosis (RRMS)（與原適應症相同） |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails（性質為既有適應症確認，非新用途擴展） |

---

## 為什麼這個預測合理？

Teriflunomide 為 dihydroorotate dehydrogenase (DHODH) 抑制劑，阻斷活化淋巴球的嘧啶從頭合成路徑，
選擇性且可逆地抑制自體反應性 T 細胞與 B 細胞的增殖。

這項機轉連結**並非推測性的老藥新用假說**，而是 RRMS 已確立的藥理與臨床證據——
Teriflunomide 早已透過 TEMSO（NCT00134563）等關鍵樞紐試驗證實療效，並在多國核准用於 RRMS。
TxGNN 模型能以 99.24% 的高分預測出這個關聯，反映了模型正確捕捉了已知的藥理-疾病連結，
可作為模型可信度的正向驗證訊號，但不構成新的臨床開發機會。

目前缺乏該藥物的完整原始適應症清單記錄（原始欄位為空），此為資料缺口，非機轉層面的不確定性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | 完成 | 1088 | TEMSO 樞紐試驗：隨機雙盲安慰劑對照，證實 teriflunomide 降低 RRMS 復發頻率並延緩失能累積（Grade A） |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | 完成 | 742 | TEMSO 長期延伸試驗：記錄長期安全性與療效（Grade A） |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | 完成 | 324 | Teriflunomide vs Interferon beta-1a 頭對頭比較（含長期延伸） |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | 完成 | 106 | 真實世界觀察性有效性研究（Grade B） |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | 進行中未招募 | 900 | 早期積極治療 vs 升階治療策略之實用性試驗（Grade B） |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A | 完成 | 2978 | 大規模真實世界回顧性研究，比較 teriflunomide 與其他 DMT（Grade B） |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | 完成 | 12 | 血清與腦脊髓液中 teriflunomide 14mg 濃度測定 |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | 進行中未招募 | 800 | DELIVER-MS：早期積極治療 vs 升階治療策略比較 |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | 完成 | 30 | 機轉研究：調節性 B 淋巴球作為 teriflunomide 療效核心媒介 |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | 完成 | 147 | Phase II 延伸試驗，長期安全性與療效追蹤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab vs Teriflunomide 頭對頭比較（ASCLEPIOS） |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs Teriflunomide 於復發性 MS 之比較 |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib vs Teriflunomide（BTK 抑制劑比較） |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | Evobrutinib vs teriflunomide，兩項 Phase 3 試驗 |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | Ofatumumab vs teriflunomide，ASCLEPIOS I/II 治療初治患者結果 |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | Ponesimod vs Teriflunomide（OPTIMUM 試驗） |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | RCT | CNS Drugs | Teriflunomide 於 RRMS 患者之 EU SmPC 綜合療效安全性回顧 |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Meta-analysis | Cochrane Database | RRMS 免疫調節劑與免疫抑制劑網絡統合分析 |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide 於 RRMS 之治療綜述 |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | 多發性硬化症診斷與治療綜述 |

---

## 香港上市資訊

目前 Teriflunomide 未於香港上市，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本評估資料集在藥物層級標記了一項**阻斷性（Blocking）資料缺口**——
> 尚缺 TFDA/當地藥監局仿單警語與禁忌症資料，導致無法進入 S1 安全性初評階段。
> 若要推進本案，此為必須優先補齊的項目。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉與臨床證據（含多個 Phase 3 頭對頭 RCT）完整且達 L1 等級，但這是**已知適應症的驗證**，非新發現的老藥新用機會。
- 真正待決策的問題是「是否要將 Teriflunomide 引進香港市場」，而非適應症擴展審查。

**若要推進需要：**
- 補齊仿單警語與禁忌症資料（目前為 Blocking 缺口，阻擋 S1 安全性初評）
- 取得完整作用機轉（MOA）正式資料以取代目前僅存於 rationale 欄位的說明
- 若目標是在香港上市：需啟動一般新藥查驗登記程序，而非老藥新用適應症擴充流程
- 確認此候選案是否應從「老藥新用」清單中移除，改列為「新藥引進評估」項目
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

