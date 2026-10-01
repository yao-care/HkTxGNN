---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine：從腫瘤化療到胃腺癌及近端胃息肉症 (GAPPS)

## 一句話總結

Capecitabine 是 5-FU 的口服前驅藥，屬於氟嘧啶類抗癌藥，在香港已有 20 張上市許可證。
TxGNN 模型預測它可能對**胃腺癌及近端胃息肉症 (Gastric adenocarcinoma and proximal polyposis of the stomach, GAPPS)** 有效。
但這項預測目前有 **0 個臨床試驗**和 **0 篇文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 胃腺癌及近端胃息肉症 (GAPPS) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Capecitabine 是 5-FU 的口服前驅藥，會在腫瘤組織中經胸腺嘧啶磷酸化酶轉換為 5-FU。5-FU 抑制胸苷酸合成酶，並嵌入 RNA 和 DNA，因此機轉上可能適用於胃部腫瘤。

GAPPS 是罕見的遺傳性症候群，與 APC 基因啟動子 1B 的變異有關，並帶有胃腺癌風險。胃腺癌與氟嘧啶類化療有明確關聯，這是預測合理的來源。

但目前沒有針對 GAPPS 的藥物專屬依據。0.999 的分數只反映知識圖譜上的關聯，不代表已有臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未記錄劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63404 | CAPECITABINE-TEVA FILM-COATED TABLETS 500MG | Teva Pharmaceutical Hong Kong Limited |
| HK-62914 | CAPECITABINE SANDOZ TABLET 500MG | Sandoz Hong Kong Limited |
| HK-62913 | CAPECITABINE SANDOZ TABLET 150MG | Sandoz Hong Kong Limited |
| HK-68949 | CAPECITABINE TABLETS 500MG | Viatris Healthcare Hong Kong Limited |
| HK-68773 | FACIVIX TABLETS 150MG | Lotus Pharmaceutical HK Limited |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氟嘧啶類，5-FU 前驅藥） |
| 骨髓抑制風險 | 依藥物類別判斷為中度，請參考原廠仿單確認 |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

本資料包沒有 toxicity 資料，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症總覽

排名第 1 的 GAPPS 沒有任何證據，但同一批預測中有幾項證據明顯較強。

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|-----|-----------|------|---------|------|
| 1 | 胃腺癌及近端胃息肉症 (GAPPS) | 99.94% | L5 | Hold |
| 2 | 印戒細胞胃腺癌 | 99.94% | L2 | Proceed with Guardrails |
| 3 | 胃管狀腺癌 | 99.94% | L1 | Proceed with Guardrails |
| 4 | 微侵襲性胃癌 | 99.94% | L5 | Hold |
| 5 | 胃賁門腺癌 | 99.91% | L2 | Proceed with Guardrails |
| 6 | 唾液腺型胃癌 | 99.91% | L3 | 列為研究問題 |
| 7 | 胃幽門癌 | 99.91% | L4 | Hold |
| 8 | 胃體癌 | 99.90% | L1 | Proceed with Guardrails |
| 9 | EB 病毒相關胃癌 | 99.90% | L4 | Hold |
| 10 | 惡性胃顆粒細胞瘤 | 99.89% | L5 | Hold |

- **胃管狀腺癌（L1）**：有多個 Phase 3 RCT，包括 CLASSIC、RESOLVE、ToGA、GLOW、CheckMate 649、KEYNOTE-859。這些試驗多用含 Capecitabine 的方案（如 CAPOX），證據是 Capecitabine 在組合療法中的表現。
- **胃體癌（L1）**：有 Phase 3 試驗 NCT02494583，但其中大多是一般胃癌／胃食道交界癌的研究，並非胃體專屬，Capecitabine 的貢獻也是間接的。
- **印戒細胞胃腺癌與胃賁門腺癌（L2）**：有 Phase 2 試驗。印戒細胞組織型通常對化療較不敏感，不能直接沿用一般胃癌的結果。

## 結論與下一步

**決策：Hold**

**理由：**
- GAPPS 是罕見遺傳性症候群，目前沒有任何臨床試驗或文獻，證據等級僅 L5，僅憑模型分數不足以推進。
- 若要在胃癌方向推進，證據較強的是胃管狀腺癌等組織型。這些應以「含 Capecitabine 的組合方案」評估，不能視為 Capecitabine 單獨有效的證據。

**若要推進需要：**
- 取得香港衛生署的原廠仿單（警語與禁忌症），這是目前阻擋安全性篩選的缺口。
- 補充 Capecitabine 的作用機轉資料，可查詢 DrugBank。
- 針對 GAPPS 做專屬文獻與試驗檢索，確認是否有病例或機轉證據。
- 若改以胃管狀腺癌為主軸，需確認各試驗中 Capecitabine 的實際角色，以及各司法管轄區的核准適應症。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

