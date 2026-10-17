---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Empagliflozin：預測新適應症為典型僵人症候群 (Classic Stiff Person Syndrome)（證據等級 L5）。原適應症：第 2 型糖尿病 (Type 2 Diabetes Mellitus)"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin：從第 2 型糖尿病到僵人症候群（Classic Stiff Person Syndrome）

## 一句話總結

Empagliflozin 是一種用於第 2 型糖尿病的藥物，在香港已有單方與複方產品上市。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病 (Type 2 Diabetes Mellitus) |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.06% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

註：香港許可證資料中未提供核准適應症文字，上表「原適應症」取自知識圖譜中的適應症關聯。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Empagliflozin 一般已知為 SGLT2 抑制劑，但本次整理的資料並未提供機轉內容，因此無法從資料中建立與僵人症候群之間的機轉連結。

僵人症候群是一種自體免疫性神經疾病，常與抗 GAD65 抗體及 GABA 神經傳導受損有關。SGLT2 抑制與這類病理之間的關聯並不明確。

較可能的解釋是：GAD65 自體免疫與糖尿病之間存在關聯，模型的高分可能部分反映了這種疾病間的共現關係，而非真正的治療效果。此外，局灶性僵肢症候群（Focal Stiff Limb Syndrome，同屬僵人症候群譜系）取得完全相同的分數 (99.06%)，顯示預測可能來自知識圖譜中共享的疾病節點特徵，而非獨立證據。

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
| HK-64095 | JARDIANCE TABLETS 10MG | 錠劑 | 未提供 |
| HK-64096 | JARDIANCE TABLETS 25MG | 錠劑 | 未提供 |
| HK-65353 | GLYXAMBI TABLETS 10MG/5MG | 錠劑 | 未提供 |
| HK-65354 | GLYXAMBI TABLETS 25MG/5MG | 錠劑 | 未提供 |
| HK-64242 | JARDIANCE DUO TABLETS 12.5MG/1000MG | 錠劑 | 未提供 |

以上列出 5 張主要許可證，共 10 張有效許可證，均由 Boehringer Ingelheim (HK) Ltd 持有。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下為部分範例：
  - 中度：Phenylephrine、Acebutolol、Acetazolamide、Formoterol、Pseudoephedrine、Nifedipine、Epinephrine、Ethinylestradiol、Hydrocortisone、Salbutamol、Ethanol、Furosemide
  - 輕度：Hydrocortisone（外用）、Alclometasone（外用）

其他警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型預測 (L5)，沒有臨床試驗、文獻或機轉資料支持。
- 預測分數可能受糖尿病與 GAD65 自體免疫的關聯，或相近疾病共享節點特徵影響，不宜視為獨立證據。

**若要推進需要：**
- 補齊作用機轉 (MOA) 資料，評估 SGLT2 抑制與僵人症候群病理的可能連結
- 進行文獻回顧，確認是否有任何前臨床或病例報告
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選
- 若有前臨床證據，再考慮設計探索性研究

---

### 其他預測適應症（供參考）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 2 | 局灶性僵肢症候群 (Focal Stiff Limb Syndrome) | 99.06% | L5 | Hold |
| 3 | 眼骨發育不良 (Opsismodysplasia) | 99.03% | L5 | Hold |

Opsismodysplasia 為由 INPPL1 突變造成的罕見骨骼發育不良，涉及 PI3K／胰島素訊號路徑。雖然與葡萄糖及胰島素訊號有推測性的關聯，但尚未驗證；且對兒童骨骼疾病使用 SGLT2 抑制劑也會引發安全性疑慮。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

