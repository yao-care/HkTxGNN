---
layout: default
title: Netarsudil
parent: 僅模型預測 (L5)
nav_order: 614
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

# Netarsudil：從開角型青光眼與高眼壓症到青光眼（含原發性遺傳性青光眼）

## 一句話總結

Netarsudil 是一種眼用滴劑成分，原本用於治療開角型青光眼與高眼壓症。
TxGNN 模型預測它可能對**青光眼 (Glaucoma)** 有效（預測分數 99.47%），目前有 **28 個臨床試驗**和 **18 篇文獻**支持這個方向。
需要注意：此預測與藥物既有核准適應症高度重疊，屬於適應症內的延伸，而非真正的跨疾病再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開角型青光眼、高眼壓症 |
| 預測新適應症 | 青光眼 (Glaucoma)；另有排名第 1 的「原發性遺傳性青光眼 (Primary hereditary glaucoma)」，但無直接證據（L5、Hold） |
| TxGNN 預測分數 | 99.47%（青光眼）；99.50%（原發性遺傳性青光眼） |
| 證據等級 | L1（青光眼）；L5（原發性遺傳性青光眼） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails（青光眼）；Hold（原發性遺傳性青光眼） |

---

## 為什麼這個預測合理？

目前缺乏經核實的詳細作用機轉資料。依藥物類別的一般知識，Netarsudil 是 Rho 激酶（ROCK1/ROCK2）抑制劑，也具有去甲腎上腺素轉運體（NET）抑制作用。它主要透過增加小樑網的房水流出、降低上鞏膜靜脈壓來降低眼壓，並可能減少房水生成。

青光眼的核心可控風險因子是眼壓，而 Netarsudil 直接作用於眼壓調控。因此，對青光眼整體，以及涉及房水流出受阻的遺傳性青光眼，機轉上都具合理性。

對「原發性遺傳性青光眼」而言，目前沒有專屬的臨床試驗或文獻，高預測分數僅是模型推論，需要特定亞型的研究來驗證。

---

## 臨床試驗證據

以下為相關性較高的試驗（共登記 28 項，列出 10 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02558374](https://clinicaltrials.gov/study/NCT02558374) | Phase 3 | 完成 | 708 | Netarsudil 0.02% 每日一次 vs Timolol 0.5% 每日兩次，評估降眼壓療效與安全性（6 個月） |
| [NCT02674854](https://clinicaltrials.gov/study/NCT02674854) | Phase 3 | 完成 | 750 | 複方 PG324（Netarsudil/Latanoprost）vs 單方 Netarsudil 與 Latanoprost（3 個月） |
| [NCT02207491](https://clinicaltrials.gov/study/NCT02207491) | Phase 3 | 完成 | 411 | Netarsudil vs Timolol 的降眼壓療效與安全性（3 個月） |
| [NCT02207621](https://clinicaltrials.gov/study/NCT02207621) | Phase 3 | 完成 | 756 | Netarsudil 每日一次／兩次 vs Timolol（12 個月） |
| [NCT04620135](https://clinicaltrials.gov/study/NCT04620135) | Phase 3 | 完成 | 245 | 日本族群中 Netarsudil vs Ripasudil（4 週） |
| [NCT03284853](https://clinicaltrials.gov/study/NCT03284853) | Phase 3 | 完成 | 436 | Netarsudil/Latanoprost 複方 vs Ganfort（MERCURY 3，6 個月） |
| [NCT03233308](https://clinicaltrials.gov/study/NCT03233308) | Phase 2 | 完成 | 20 | 安慰劑對照，驗證小樑網房水流出能力的提升（機轉研究） |
| [NCT05283395](https://clinicaltrials.gov/study/NCT05283395) | Phase 4 | 完成 | 136 | 由 Latanoprost 類方案換用 Rocklatan 的降眼壓效果（12 週） |
| [NCT04981886](https://clinicaltrials.gov/study/NCT04981886) | Phase 4 | 狀態未知 | 115 | Rhopressa vs Lumigan 用於正常眼壓性青光眼 |
| [NCT06449352](https://clinicaltrials.gov/study/NCT06449352) | Phase 4 | 完成 | 100 | 正常眼壓性青光眼患者加用 Netarsudil vs Brimonidine |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37615697](https://pubmed.ncbi.nlm.nih.gov/37615697/) | 2024 | RCT | Graefe's Arch Clin Exp Ophthalmol | MERCURY-3：Netarsudil/Latanoprost 複方與 Bimatoprost/Timolol 的療效與安全性比較 |
| [37603205](https://pubmed.ncbi.nlm.nih.gov/37603205/) | 2023 | RCT | Adv Ther | J-ROCKET：Netarsudil 每日一次與 Ripasudil 每日兩次的比較 |
| [41915113](https://pubmed.ncbi.nlm.nih.gov/41915113/) | 2026 | RCT | Adv Ther | J-ROCKET-2：Netarsudil 加 Latanoprost 對日本原發性開角型青光眼／高眼壓症的療效 |
| [40719703](https://pubmed.ncbi.nlm.nih.gov/40719703/) | 2025 | RCT | J Glaucoma | 早期青光眼中 Dorzolamide 與 Netarsudil 比較；Netarsudil 的 OCTA 參數改善較多，副作用相當 |
| [34550421](https://pubmed.ncbi.nlm.nih.gov/34550421/) | 2022 | 世代研究 | Graefe's Arch Clin Exp Ophthalmol | Netarsudil 0.02% 的真實世界 6 個月療效與安全性 |
| [31695162](https://pubmed.ncbi.nlm.nih.gov/31695162/) | 2020 | Review | Eye | 回顧 Latanoprostene bunod、Netarsudil 及其與 Latanoprost 複方等新青光眼藥物 |
| [31663782](https://pubmed.ncbi.nlm.nih.gov/31663782/) | 2020 | Review | Expert Opin Pharmacother | Netarsudil-Latanoprost 固定複方治療青光眼與高眼壓症 |
| [33148002](https://pubmed.ncbi.nlm.nih.gov/33148002/) | 2021 | Review | Ann Pharmacother | 評估 Netarsudil 作為開角型青光眼／高眼壓症第一線治療的角色 |
| [36113700](https://pubmed.ncbi.nlm.nih.gov/36113700/) | 2022 | 病例系列 | J AAPOS | 16 名兒童青光眼中 9 例（56%）出現角膜蜂窩狀變化 |
| [36223296](https://pubmed.ncbi.nlm.nih.gov/36223296/) | 2022 | 病例系列 | J Glaucoma | 使用後出現淚點部分狹窄或完全閉鎖，停藥後可逆 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68269 | RHOPRESSA EYE DROPS 0.02% W/V | 眼用滴劑 | 未提供 |
| HK-68150 | ROCKLATAN EYE DROPS | 眼用滴劑 | 未提供 |

兩張許可證均由 Santen Pharmaceutical (Hong Kong) Limited 持有，狀態皆為有效。Rocklatan 為 Netarsudil 與 Latanoprost 的複方製劑。

---

## 安全性考量

- **藥物交互作用**：資料庫僅顯示藥理標靶層面的關聯，即抑制 ROCK1 與 ROCK2，並無具臨床分級的藥物間交互作用。
- **已知眼部不良事件（來自文獻）**：
  - 上皮角膜病變、角膜蜂窩狀變化（PMID 32637736、36113700、36650088）
  - 淚點狹窄或閉鎖（PMID 36223296、35231471）
  - 結膜脆弱，可能影響手術（PMID 41675443）
  - 渦狀角膜病變（PMID 37971506）

警語與禁忌症的完整資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（青光眼）；Hold（原發性遺傳性青光眼）**

**理由：**
- 青光眼方面有多個已完成的 Phase 3 隨機對照試驗，且香港已有上市產品。但此適應症與既有核准適應症重疊，屬於適應症內的延伸。
- 原發性遺傳性青光眼僅有模型預測，缺乏專屬試驗與文獻，證據等級為 L5，建議暫緩。

**若要推進需要：**
- 取得香港核准的適應症文字與仿單（警語、禁忌症），確認許可範圍。
- 補充經核實的作用機轉資料。
- 針對原發性遺傳性青光眼、兒童青光眼與正常眼壓性青光眼，進行亞型專屬的臨床研究。
- 建立角膜、結膜與淚點相關不良事件的監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

