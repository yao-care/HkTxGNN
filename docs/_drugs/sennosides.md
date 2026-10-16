---
layout: default
title: Sennosides
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sennosides：預測新適應症為頭皮單純性毛髮稀疏症 (Hypotrichosis simplex of the scalp)（證據等級 L5）。原適應症：資料中許可證未載明核准適應症"
monitor_inn: "SENNOSIDES"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "primary hereditary glaucoma"]
---

# Sennosides
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

# Sennosides：從便秘（緩瀉）到頭皮毛髮稀疏症

## 一句話總結

Sennosides（番瀉苷）是刺激性緩瀉劑，在香港已有多張單方製劑許可證，一般用於緩解便秘。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀疏症 (Hypotrichosis simplex of the scalp)** 有效，但目前**沒有任何臨床試驗或文獻**支持，且機轉上找不到合理關聯，僅屬模型的圖譜預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中許可證未載明核准適應症 |
| 預測新適應症 | 頭皮單純性毛髮稀疏症 (Hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Sennosides 是刺激性緩瀉劑，其活性代謝物 rheinanthrone 由大腸細菌產生，作用於結腸黏膜，增加腸道蠕動與液體分泌，作用主要局限於大腸局部，全身吸收極少。

頭皮單純性毛髮稀疏症是遺傳性毛囊疾病（例如 CDSN、APCDD1、SNRPE 等基因變異所致）。目前找不到任何能把 Sennosides 與毛囊生物學連結起來的路徑。0.993 的高分來自知識圖譜的鄰近關係，並沒有藥理學推理支持，因此**不能視為有生物學依據的預測**。

其他排名靠前的預測同樣缺乏支持：

| 排名 | 預測疾病 | TxGNN 分數 | 評估 |
|------|---------|-----------|------|
| 2 | 先天性毛髮稀疏伴粟丘疹 (Congenital hypotrichosis milia) | 99.23% | 無機轉關聯，可能源自圖譜中相近的毛髮稀疏表型 |
| 3 | 瀰漫性圓禿 (Diffuse alopecia areata) | 99.12% | 圓禿為 T 細胞介導的自體免疫疾病（JAK/STAT、IFN-γ），Sennosides 無相關免疫調節作用 |
| 4 | 開角型青光眼 (Open-angle glaucoma) | 99.11% | 全身吸收極少，不可能作用於眼部；便秘用力可能暫時升高眼壓，但這不是治療依據 |
| 5 | 原發性遺傳性青光眼 (Primary hereditary glaucoma) | 99.10% | 病因為房角發育異常（如 CYP1B1、MYOC），與局部作用的大腸緩瀉劑無關 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68436 | NEPURGO SENNOSIDES TABLETS 20MG | 片劑 | 許可證資料未載明 |
| HK-66475 | WEL-HEALTH LAXATIVE TABLETS 12MG | 片劑 | 許可證資料未載明 |
| HK-68435 | EFORMAT SENNOSIDES TABLETS 20MG | 片劑 | 許可證資料未載明 |
| HK-45031 | PMS-SENNOSIDES TAB 8.6MG | 片劑 | 許可證資料未載明 |
| HK-68434 | EASUWEI SENNOSIDES TABLETS 20MG | 片劑 | 許可證資料未載明 |

另有 4 張單方許可證（HK-63141、HK-64450、HK-61719、HK-37679），全部 9 張皆為有效狀態。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，沒有臨床試驗、沒有文獻，機轉上也無合理關聯，高預測分數只反映圖譜結構。
- 前五名預測（毛髮疾病與青光眼）皆缺乏生物學依據，不建議投入資源。

**若要推進需要：**
- 補齊 Sennosides 的作用機轉資料（MOA）。
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌。
- 若仍想探索，需先有體外或動物模型證據，顯示對毛囊或相關路徑有作用，再重新評估。
- 對其他預測疾病，建議改查是否有更貼近 Sennosides 藥理（如腸道相關）的候選適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

