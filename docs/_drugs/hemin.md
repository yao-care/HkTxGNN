---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hemin：預測新適應症為血小板減少性紫斑症 (Thrombocytopenic Purpura)（證據等級 L5）。原適應症：急性間歇性紫質症 (acute intermittent porphyria)"
monitor_inn: "Hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
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

## Hemin：從急性間歇性紫質症到血小板減少性紫斑症
{: .text-alpha }

## 一句話總結

Hemin 原本用於治療急性間歇性紫質症 (acute intermittent porphyria)。
TxGNN 模型預測它可能對**血小板減少性紫斑症 (Thrombocytopenic Purpura)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關的文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性間歇性紫質症 (acute intermittent porphyria) |
| 預測新適應症 | 血小板減少性紫斑症 (Thrombocytopenic Purpura) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

註：原適應症來自 TxGNN 知識圖譜的適應症關聯，香港許可證本身未載明核准適應症文字。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Hemin 可補充體內血基質 (heme) 池，並抑制肝臟 ALAS1 酵素，這是它用於急性間歇性紫質症的基礎。

Hemin 也可能誘導血基質加氧酶-1 (heme oxygenase-1)，理論上可能影響免疫或發炎路徑。但現有資料並未證實它與血小板減少性紫斑症之間有直接關聯，預測分數僅來自知識圖譜的推論。

此外，排名前 10 的預測多屬凝血或補體相關疾病（如血友病、C1 抑制劑缺乏、血管性血友病），機轉上缺乏支持。這些預測較可能反映圖譜結構上的相似性，而非真實療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：排名第 2 的預測「血友病」檢索到 3 篇文獻，但內容均為 givosiran 或急性肝型紫質症的研究，與 Hemin 用於血友病無關，因此未列入本表。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68135 | NORMOSANG CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/10ML | 未載明 | 未載明 |

持證商：TALENT INTERNATIONAL TRADING (HK) LIMITED

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 74 筆交互作用，以下為部分範例：
  - **嚴重 (Major)**：Ethinylestradiol、Estradiol、Conjugated estrogens、Butalbital、Amobarbital、Phenobarbital
  - **中度 (Moderate)**：Acetylsalicylic acid（阿斯匹靈）、Abciximab、Alteplase、Apixaban、Dipyridamole、Anagrelide、Antithrombin III 等抗凝血或抗血小板藥物

  多項中度交互作用屬於影響凝血或血小板功能的藥物，若用於血小板減少性疾病，需特別留意。

- **其他注意事項**：預測資料中提到，Hemin 輸注曾與短暫性凝血異常和血栓性靜脈炎相關。此點對凝血異常或血栓傾向的疾病尤其值得關注。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測僅來自模型分數，沒有任何臨床試驗或直接相關文獻（證據等級 L5）。
- 缺乏機轉依據，且 Hemin 本身有凝血相關不良反應，用於血小板或凝血疾病有安全疑慮。

**若要推進需要：**
- 取得 Hemin 的詳細作用機轉資料，並評估與血小板減少性紫斑症的機轉關聯
- 進行系統性文獻回顧與前臨床研究，確認是否有任何支持證據
- 取得香港衛生署核准的仿單，確認警語、禁忌症與核准適應症
- 針對凝血與血栓風險進行專門的安全性評估
- 確認給藥途徑與劑型是否符合新適應症的需求
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

