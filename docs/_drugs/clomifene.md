---
layout: default
title: Clomifene
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomifene：預測新適應症為46,XY 性發育異常（睪丸類固醇合成缺陷）（證據等級 L5）。原適應症：女性不孕症 (female infertility)"
monitor_inn: "Clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "longitudinal vaginal septum", "transverse vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "ovarian remnant syndrome"]
---

# Clomifene
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

## Clomifene：從女性不孕症到 46,XY 性發育異常（睪丸類固醇合成缺陷）
{: .text-alpha }

## 一句話總結

Clomifene 是一種選擇性雌激素受體調節劑，原本用於治療女性不孕症（排卵誘導）。
TxGNN 模型預測它可能對 **46,XY 性發育異常（睪丸類固醇合成缺陷）** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 女性不孕症 (female infertility) |
| 預測新適應症 | 46,XY 性發育異常（睪丸類固醇合成缺陷） |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理資訊，Clomifene 是選擇性雌激素受體調節劑（作用標的包含雌激素受體 α，即 ESR1），可阻斷下視丘的雌激素負回饋，使 GnRH、LH 與 FSH 分泌增加。

理論上，增加的促性腺激素刺激可能提高睪丸 Leydig 細胞的驅動力。但此疾病的核心是睪丸類固醇合成酶本身的缺陷，即使上游刺激增加，下游的療效也會受到限制。因此這個關聯目前偏向推測，僅建立在 TxGNN 的預測上。

此外，排名前 10 的預測適應症（如陰道中隔、染色體部分三體/四體症等）多數缺乏機轉依據，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59765 | OVULET TAB 50MG | 錠劑（品名所示） | 未提供 |
| HK-20642 | CLOMIPHENE CITRATE TAB 50MG | 錠劑（品名所示） | 未提供 |
| HK-22571 | CLONIN CAP 50MG | 膠囊（品名所示） | 未提供 |
| HK-65983 | OVA-MIT TABLETS 50MG | 錠劑（品名所示） | 未提供 |
| HK-24713 | FERTILAN TAB 50MG | 錠劑（品名所示） | 未提供 |

另有 HK-35034（DUINUM TAB 50MG），共 6 張有效單方許可證。

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（非仿單內容，僅供參考）：
  - 肝臟與膽囊疾病
  - 甲狀腺與腎上腺功能異常（甲狀腺功能低下、甲狀腺毒症、腎上腺功能不全等）
  - 子宮內膜癌、子宮內膜異位症
  - 腦下垂體腫瘤
  - 多囊卵巢症候群相關之卵巢囊腫、卵巢過度刺激症候群
  - 血栓性靜脈炎
  - 視覺障礙
  - 焦慮症與情緒相關疾患
- **藥物交互作用**：與 Bexarotene 有「嚴重 (Major)」等級的交互作用。另有藥理學資料顯示其作用於雌激素受體 α 與 VRAC 通道。
- 另外，對於預測適應症「卵巢殘餘症候群」，理論上刺激殘留卵巢組織可能加重症狀，需特別留意。

其餘警語與禁忌的仿單資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症僅有模型分數，無臨床試驗或文獻佐證（L5）。
- 睪丸類固醇合成缺陷屬原發性酵素缺陷，Clomifene 的機轉難以彌補，且作用機轉資料也不完整。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症。
- 補齊 Clomifene 的作用機轉（MOA）資料。
- 進行系統性文獻回顧，尤其是 Clomifene 用於男性低促性腺或 Leydig 細胞功能相關疾病的既有研究。
- 評估是否有更具機轉合理性的候選適應症，取代目前僅依 TxGNN 模型（深度學習）分數得出的預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

