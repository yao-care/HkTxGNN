---
layout: default
title: Netarsudil
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 2
---

# Netarsudil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Netarsudil：從青光眼機轉延伸到原發性遺傳性青光眼

## 一句話總結

Netarsudil（DrugBank DB13931）是 Rho 激酶（ROCK）抑制劑，用於降低眼內壓；目前 Evidence Pack 未提供其原始核准適應症紀錄。TxGNN 模型針對兩個相關疾病給出高分預測：**青光眼 (Glaucoma)** 與其亞型 **原發性遺傳性青光眼 (Primary Hereditary Glaucoma)**。前者已有 **36 個臨床試驗**（含多個完成的 Phase 3 RCT）與 **20 篇文獻**支持，證據充分；後者僅有 **1 個招募中試驗**，屬機轉推論階段，證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（香港無許可證紀錄，`original_indications` 為空） |
| 預測新適應症 ① | 青光眼 (Glaucoma) — TxGNN 分數 99.47%（rank 9349） |
| 預測新適應症 ② | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) — TxGNN 分數 99.50%（rank 8958） |
| 證據等級 | ① 青光眼：L1　② 原發性遺傳性青光眼：L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | ① Proceed with Guardrails　② Hold |

---

## 為什麼這個預測合理？

Netarsudil 是 Rho 激酶（ROCK）抑制劑，同時具有正腎上腺素轉運蛋白抑制作用。其藥理機轉為增加小樑網（trabecular meshwork）房水外流、降低鞏膜靜脈壓，直接降低眼內壓（IOP）。目前缺乏詳細的完整 MOA 文件（DrugBank 查詢未回傳結構化資料），但上述機轉已由多篇文獻及臨床試驗證實。

「青光眼」這項預測實質上並非全新的老藥新用假設，而是與 netarsudil 已知核准用途（單方 Rhopressa®、複方 Rocklatan®）高度重疊的機轉驗證——IOP 升高正是青光眼的核心病理生理，ROCK 抑制劑透過改善房水排出阻力直接對應此機轉，因此證據極為紮實（多個完成的 Phase 3 RCT）。

「原發性遺傳性青光眼」則是在青光眼機轉基礎上，針對特定遺傳亞群的延伸推論。目前僅有一項尚在邀請招募、且主要終點聚焦於角膜內皮保護（而非此遺傳亞型療效）的試驗（NCT06969586），並無直接針對此亞群的療效資料，屬理論相關性而非實證支持。

---

## 臨床試驗證據

### ① 青光眼 (Glaucoma) — 主要佐證

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02558374](https://clinicaltrials.gov/study/NCT02558374) | Phase 3 | 完成 | 708 | Netarsudil vs Timolol 0.5%，6個月活性對照，降眼壓療效與安全性核心關鍵試驗 |
| [NCT02207621](https://clinicaltrials.gov/study/NCT02207621) | Phase 3 | 完成 | 756 | Netarsudil QD/BID vs Timolol BID，12個月降眼壓療效與安全性 |
| [NCT02674854](https://clinicaltrials.gov/study/NCT02674854) | Phase 3 | 完成 | 750 | PG324（複方）vs 單方成分，3個月降眼壓療效比較 |
| [NCT02558400](https://clinicaltrials.gov/study/NCT02558400) | Phase 3 | 完成 | 718 | PG324 vs Netarsudil 與 Latanoprost 單方，12個月療效與安全性 |
| [NCT03284853](https://clinicaltrials.gov/study/NCT03284853) | Phase 3 | 完成 | 436 | MERCURY-3：Netarsudil/Latanoprost 複方 vs Bimatoprost/Timolol，6個月 |
| [NCT04620135](https://clinicaltrials.gov/study/NCT04620135) | Phase 3 | 完成 | 245 | Netarsudil QD vs Ripasudil BID，日本 POAG/OHT 患者，4週療效比較 |
| [NCT02207491](https://clinicaltrials.gov/study/NCT02207491) | Phase 3 | 完成 | 411 | Netarsudil vs Timolol，3個月降眼壓療效與安全性 |
| [NCT02246764](https://clinicaltrials.gov/study/NCT02246764) | Phase 3 | 完成 | 93 | Netarsudil QD/BID vs Timolol BID，12個月長期安全性 |
| [NCT07082816](https://clinicaltrials.gov/study/NCT07082816) | Phase 3 | 進行中 | 489 | 重新調配 PG324 配方之降眼壓療效與安全性，持續累積證據 |
| [NCT06441643](https://clinicaltrials.gov/study/NCT06441643) | Phase 2 | 完成 | 426 | AR-17043 與 PG043（AR-17043/Latanoprost）劑量反應研究 |

### ② 原發性遺傳性青光眼 (Primary Hereditary Glaucoma)

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | 邀請招募中 | 50 | 主要評估 ROCK 抑制劑對 Fuchs 角膜內皮失養症合併青光眼患者之角膜內皮保護作用，非以此遺傳亞型療效為主要終點 |

---

## 文獻證據

從青光眼相關文獻中，依 RCT > Review > Case report 優先排序：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37615697](https://pubmed.ncbi.nlm.nih.gov/37615697/) | 2024 | RCT | Graefe's Arch Clin Exp Ophthalmol | MERCURY-3：Netarsudil/Latanoprost 複方與 Bimatoprost/Timolol 之隨機比較 |
| [31842637](https://pubmed.ncbi.nlm.nih.gov/31842637/) | 2019 | RCT | Expert Rev Clin Pharmacol | Netarsudil/Latanoprost 複方降眼壓療效與安全性回顧 |
| [35979215](https://pubmed.ncbi.nlm.nih.gov/35979215/) | 2022 | RCT（統合分析） | Frontiers in Medicine | Netarsudil/Latanoprost 複方 vs 單方之系統性回顧與統合分析 |
| [37603205](https://pubmed.ncbi.nlm.nih.gov/37603205/) | 2023 | RCT | Advances in Therapy | J-ROCKET：Netarsudil vs Ripasudil 之 Phase 3 安全性與療效比較 |
| [31695162](https://pubmed.ncbi.nlm.nih.gov/31695162/) | 2020 | Review | Eye (London) | 新型青光眼藥物：latanoprostene bunod、netarsudil 與複方之綜述 |
| [33148002](https://pubmed.ncbi.nlm.nih.gov/33148002/) | 2021 | Review | Ann Pharmacother | Netarsudil 作為開角型青光眼一線治療角色之文獻回顧 |
| [31663782](https://pubmed.ncbi.nlm.nih.gov/31663782/) | 2020 | Review | Expert Opin Pharmacother | Netarsudil-Latanoprost 複方治療青光眼之綜述 |
| [30323550](https://pubmed.ncbi.nlm.nih.gov/30323550/) | 2018 | Review | Clin Ophthalmol | Netarsudil 治療開角型青光眼之藥理輪廓與現有證據 |
| [33843288](https://pubmed.ncbi.nlm.nih.gov/33843288/) | 2021 | Review | Eur J Ophthalmol | Netarsudil 治療慢性原發性開角型青光眼及高眼壓症之新藥綜述 |
| [36223296](https://pubmed.ncbi.nlm.nih.gov/36223296/) | 2022 | Case Report | J Glaucoma | 局部使用 Netarsudil 後淚小點部分/完全閉鎖之病例報告 |

---

## 香港上市資訊

Netarsudil 目前尚未在香港取得藥品許可證（`total_licenses = 0`），無上市品項資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本 Evidence Pack 中，TFDA 仿單警語/禁忌屬 **Blocking 級資料缺口**，尚未完成安全性初評所需的解析，DDI 查詢亦無結果。）

---

## 結論與下一步

**決策：**
- 青光眼 (Glaucoma)：**Proceed with Guardrails**
- 原發性遺傳性青光眼 (Primary Hereditary Glaucoma)：**Hold**

**理由：**
青光眼適應症有多個完成的 Phase 3 RCT（含 MERCURY 系列、J-ROCKET）直接支持療效與安全性，證據等級達 L1，但此本質上是對藥物既有核准用途的證據彙整，而非嚴格意義的老藥新用；由於香港尚無許可證，仍須走完整的地區註冊流程並補齊安全性資料才能推進。原發性遺傳性青光眼僅有理論機轉支持與 1 個非直接相關的招募中試驗，證據不足以支持進一步行動。

**若要推進需要：**
- 取得 TFDA／原廠仿單警語與禁忌症資料，解除 Blocking 級資料缺口
- 補齊 DrugBank 完整 MOA 與藥物交互作用資料
- 若欲推進原發性遺傳性青光眼亞型，需規劃該族群專屬的臨床證據收集
- 評估香港藥品註冊路徑（目前 0 張許可證，未上市）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

