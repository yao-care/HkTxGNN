---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Anifrolumab：預測新適應症為糖尿病性白內障 (Diabetic Cataract)（證據等級 L5）。原適應症：香港許可證未載明適應症文字（國際上核准用於中重度 SLE）"
monitor_inn: "Anifrolumab"
predicted_indications: ["diabetic cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "mature cataract", "craniostenosis cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic retinopathy"]
---

# Anifrolumab
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

## Anifrolumab：從系統性紅斑性狼瘡到糖尿病性白內障
{: .text-alpha }

## 一句話總結

Anifrolumab 是一種針對第一型干擾素受體（IFNAR1）的單株抗體，已在香港取得許可證，國際上核准用於中重度系統性紅斑性狼瘡（SLE）。
TxGNN 模型預測它可能對**糖尿病性白內障 (Diabetic Cataract)** 有效，但目前**沒有臨床試驗**，也沒有直接支持此用途的文獻，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字（國際上核准用於中重度 SLE） |
| 預測新適應症 | 糖尿病性白內障 (Diabetic Cataract) |
| TxGNN 預測分數 | 98.50% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Anifrolumab 是第一型干擾素受體（IFNAR1）的拮抗型抗體，可阻斷第一型干擾素訊號，在 SLE 中的療效已被證實。

然而，目前沒有任何資料支持第一型干擾素訊號阻斷與糖尿病性晶體混濁之間的生物學關聯。糖尿病性白內障主要與代謝與滲透壓機制（如多元醇路徑）有關，與第一型干擾素路徑並無已知連結。此預測分數較可能反映知識圖譜中白內障相關節點的共同註解，而非實際的生物學證據。

TxGNN 同時預測了多種白內障類型（強直性、未成熟、成熟、老年性、皮質性等），分數均在 98.3%–98.5% 之間。這種集中現象也提示預測可能來自圖譜結構。另一個預測的「糖尿病視網膜病變」（98.2%）在生物學上相對較合理，因為干擾素相關發炎曾在視網膜疾病中被討論，但同樣沒有任何試驗或文獻支持，仍屬推測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對糖尿病性白內障，目前無相關文獻。

在同一組預測的「皮質性白內障」項下，有一篇間接相關文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/) | 2025 | Review | International Journal of Molecular Sciences | 探討新興與傳統 SLE 療法的眼科安全性考量。依標題與摘要判斷，內容著重於狼瘡治療的眼部不良反應（如糖皮質激素相關白內障風險），並非 Anifrolumab 治療白內障的效益，不支持藥物再利用。 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67661 | SAPHNELO CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/2ML（廠商：AstraZeneca Hong Kong Limited） | 未載明（濃縮輸注液） | 未載明 |

---

## 安全性考量

- **藥物交互作用**：目前資料僅顯示 Anifrolumab 與其藥理標的 IFNAR1（第一型干擾素 α/β 受體 1）的藥理作用關係（拮抗結合），並未列出具臨床意義的藥物交互作用，也無分級資訊。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗，也沒有支持療效的文獻（證據等級 L5）。
- 第一型干擾素阻斷與糖尿病性白內障之間，缺乏可支持的生物學理由。

**若要推進需要：**
- 補齊作用機轉資料，並建立干擾素訊號與晶體病變（或視網膜發炎）的機轉假說。
- 進行前臨床驗證（例如糖尿病動物模型或晶體/視網膜細胞模型）。
- 取得香港仿單的警語與禁忌症，以進行安全性篩選。
- 若要優先探索眼科方向，可考慮先評估生物學上較合理的「糖尿病視網膜病變」。
- 評估全身性抗體用於眼部適應症的給藥途徑可行性與風險效益。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

