---
layout: default
title: Ethyl Chloride
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ethyl Chloride：預測新適應症為手足搐搦性白內障 (Tetanic Cataract)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Ethyl chloride"
predicted_indications: ["tetanic cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "craniostenosis cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "acne (disease)"]
---

# Ethyl Chloride
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

## Ethyl chloride：從（原適應症未載明）到白內障（tetanic cataract）
{: .text-alpha }

## 一句話總結

Ethyl chloride（氯乙烷）是一種外用揮發性冷卻噴劑／局部麻醉劑，本次整理的資料中並未載明其核准適應症。
TxGNN 模型預測它可能對**手足搐搦性白內障 (Tetanic Cataract)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型的計算預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 手足搐搦性白內障 (Tetanic Cataract) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ethyl chloride 是外用揮發性冷卻劑／局部麻醉劑，主要用於皮膚表面的冷凍麻醉，與晶狀體生物學之間沒有已知的作用關聯。

手足搐搦性白內障繼發於低血鈣或副甲狀腺功能低下，外用冷卻劑在機轉上難以處理這類成因。因此，這項預測目前找不到合理的生物學解釋，較可能反映知識圖譜中白內障各亞型相互鄰近所產生的計算假象。

其他排名靠前的預測也多為白內障亞型（成熟、未成熟、糖尿病性、老年性、核性、皮質性等），分數介於 99.6%～99.8%，同樣沒有任何臨床試驗或文獻支持。唯一非白內障的預測是痤瘡（99.5%），其連結僅限於皮膚冷凍療法在皮膚科的使用，並不能說明對痤瘡病理（皮脂、C. acnes、發炎）有療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44967 | ETIDERM SHAMPOO 10% (VET) | 未載明 | 未載明 |

該許可證為獸用（VET）洗毛劑產品，由 VIRBAC H.K. TRADING LIMITED 持有，狀態為有效。這並非人用的氯乙烷噴劑許可證。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病關聯，並非仿單內容）：冷球蛋白血症 (cryoglobulinemia)、冷球蛋白血症性血管炎 (cryoglobulinemic vasculitis)、第 II 型混合型冷球蛋白血症 (type II mixed cryoglobulinemia)。這些疾病與冷刺激相關，使用冷卻劑時需特別留意。

其餘警語、禁忌與藥物交互作用資訊，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測皆只有模型分數，沒有任何臨床試驗或文獻，也找不到合理的作用機轉；對外用冷卻劑而言，白內障（眼內晶狀體疾病）在給藥途徑上也不可行。
- 香港唯一的許可證為獸用產品，且知識圖譜顯示與冷球蛋白相關疾病存在禁忌關聯。

**若要推進需要：**
- 補充 Ethyl chloride 的作用機轉資料（例如查詢 DrugBank）
- 取得香港衛生署仿單，確認警語與禁忌
- 釐清原適應症與人用劑型的上市狀況
- 以文獻與前臨床研究驗證是否存在任何生物學關聯；在此之前，不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

