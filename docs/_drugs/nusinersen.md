---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nusinersen：預測新適應症為腎性低鎂血症 (Renal Hypomagnesemia)（證據等級 L5）。原適應症：脊髓性肌肉萎縮症 (spinal muscular atrophy)"
monitor_inn: "Nusinersen"
predicted_indications: ["renal hypomagnesemia", "generalized pustular psoriasis", "atypical hypotonia-cystinuria syndrome", "spermatic cord cancer", "congenital secondary polycythemia", "acquired secondary polycythemia", "immune dysregulation-inflammatory bowel disease-arthritis-recurrent infections syndrome", "hyperphenylalaninemia due to tetrahydrobiopterin deficiency", "IgG4-related mesenteritis", "leukoencephalopathy-palmoplantar keratoderma syndrome"]
---

# Nusinersen
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

# Nusinersen：從脊髓性肌肉萎縮症到腎性低鎂血症

## 一句話總結

Nusinersen 是一種反義寡核苷酸藥物，原本用於治療脊髓性肌肉萎縮症 (spinal muscular atrophy)。
TxGNN 模型預測它可能對**腎性低鎂血症 (Renal Hypomagnesemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脊髓性肌肉萎縮症 (spinal muscular atrophy) |
| 預測新適應症 | 腎性低鎂血症 (Renal Hypomagnesemia) |
| TxGNN 預測分數 | 50.00% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Nusinersen 是針對 SMN2 前驅 mRNA 剪接的反義寡核苷酸，可提高 SMN 蛋白表現，其在脊髓性肌肉萎縮症中的角色已被確立。

然而，腎性低鎂血症源自腎小管的鎂transport缺陷（例如 CNNM2、TRPM6、EGF、KCNA1 等基因），與 SMN 相關路徑並無已知關聯。因此，**目前找不到合理的機轉連結**。

此外，TxGNN 分數 0.5 沒有區辨力，不能視為有意義的預測訊號。同批預測的其他 9 個疾病（如泛發性膿疱型乾癬、脊髓索癌、IgG4 相關腸繫膜炎等）分數也都是 0.5，且同樣缺乏機轉與臨床證據，整體而言這些預測的可信度皆偏低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65896 | SPINRAZA SOLUTION FOR INJECTION 12MG/5ML | 注射液 | 未提供 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗、文獻，也找不到合理的機轉連結；0.5 的預測分數缺乏區辨力。
- 腎性低鎂血症屬腎小管運輸缺陷，與 Nusinersen 調控 SMN2 剪接的機轉無關。

**若要推進需要：**
- 取得 Nusinersen 的作用機轉資料，並釐清其與鎂代謝或腎小管功能是否有任何關聯
- 提出機轉假說，並以前臨床研究驗證
- 取得香港原廠仿單的警語與禁忌資料，完成安全性篩選
- 評估給藥途徑的相容性（Nusinersen 為鞘內注射，與腎臟疾病的治療需求是否匹配）
- 建議重新檢視其他預測適應症，優先選擇有機轉合理性者
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

