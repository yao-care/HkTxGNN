---
layout: default
title: Etofenamate
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 5
---

# Etofenamate
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

# Etofenamate：從肌肉骨骼局部消炎到脊椎關節病變

## 一句話總結

Etofenamate 是一種 NSAID 類外用抗炎藥，透過抑制 COX 酶減少局部前列腺素生成，廣泛用於肌肉骨骼疼痛與關節發炎的局部緩解。
TxGNN 模型預測它可能對**脊椎關節病變易感性 (Spondyloarthropathy, susceptibility to)** 有效，TxGNN 評分高達 **99.9996%**，為本批預測最高分，但目前**無臨床試驗或文獻**直接支持此藥物用於該適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無香港上市記錄（已知為外用 NSAID，用於肌肉骨骼局部消炎止痛） |
| 預測新適應症 | 脊椎關節病變易感性 (Spondyloarthropathy, susceptibility to) |
| TxGNN 預測分數 | 99.9996% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Etofenamate 屬於非類固醇消炎止痛藥（NSAID），透過抑制環氧化酶（COX-1/COX-2）來減少前列腺素 E2（PGE2）的生成，進而降低關節炎症傳導與疼痛訊號。此藥通常製成外用凝膠或乳膏，穿透皮膚後在局部組織發揮抗炎效果。目前缺乏 DrugBank 詳細 MOA 資料，機轉描述係依據其 NSAID 藥物類別特性推論。

脊椎關節病變（Spondyloarthropathy, SpA）是一組以脊柱、骶髂關節慢性炎症為核心特徵的疾病族群，包含強直性脊椎炎（AS）、乾癬性關節炎等亞型，炎症反應由 PGE2 介導的關節滑膜增生所驅動。根據 ASAS/EULAR 治療指引，**NSAID 類藥物是 SpA 的一線治療**，celecoxib、diclofenac、naproxen、indomethacin 等均已有充分 Phase 3 RCT 支持。

Etofenamate 的 COX 抑制機轉與上述藥物屬同一藥理類別，TxGNN 知識圖譜捕捉到「NSAID 類 → COX 抑制 → PGE2 ↓ → SpA 炎症緩解」的強烈節點關聯，評分達 0.9999961。值得注意的是，排名第 2 的預測適應症為**強直性脊椎炎（Ankylosing Spondylitis, 99.9984%）**，與 SpA 族群高度重疊，進一步強化此機轉推論的一致性。然而，etofenamate 主要為外用製劑，全身性抗炎效果有限，目前無本藥物特定的 SpA 臨床研究，仍需進一步評估投藥途徑的可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 NSAID 類藥物治療脊椎關節病變已有充分的類別級別（class-level）臨床證據，且 TxGNN 預測分數極高，但目前完全缺乏 etofenamate 本身用於此適應症的特定研究資料（L5），香港亦無上市許可；加上其外用製劑的全身暴露量能否達到 SpA 所需抗炎效果，尚未有評估，安全性與 MOA 資訊均不完整，目前無法進入正式再利用評估流程。

**若要推進需要：**
- 補充 etofenamate 的詳細 MOA 及安全性資料（DrugBank API 查詢、原廠仿單 PDF 解析）
- 評估投藥途徑可行性：外用製劑的皮膚穿透率及系統性血藥濃度是否足以發揮全身性抗炎效果
- 執行針對 etofenamate 在肌肉骨骼/關節炎相關研究的文獻回顧（PubMed、EMBASE 關鍵字擴展搜尋）
- 評估 NSAID class-level 證據（AS/SpA 一線用藥 RCT）是否可外推至 etofenamate，並比較藥動學差異
- 若計畫申請香港上市，需先釐清藥監局的許可路徑（如透過原產地許可外推或在地臨床資料要求）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

