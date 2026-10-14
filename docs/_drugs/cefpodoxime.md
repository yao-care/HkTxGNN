---
layout: default
title: Cefpodoxime
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Cefpodoxime
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

# Cefpodoxime：從細菌感染到退化性關節炎（骨關節炎易感性）

## 一句話總結

Cefpodoxime 是第三代頭孢菌素類抗生素，香港已有 2 張有效許可證。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未列明適應症文字 |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.35% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cefpodoxime 屬於第三代頭孢菌素，一般認為其作用是結合青黴素結合蛋白 (PBP)，抑制細菌細胞壁合成。這是抗菌作用，與骨關節炎的致病過程沒有已知的連結。

骨關節炎主要由軟骨退化、機械壓力與低度發炎所驅動，「易感性」則偏向遺傳因素。沒有任何證據顯示 Cefpodoxime 能影響這些路徑。0.993 的高分來自知識圖譜的網路關係，較可能是圖譜相鄰性造成的假象，而非真實的生物學關聯。

其他預測的適應症也有類似情形，包括骨關節炎、類風濕性關節炎、血紅素病變，以及多種罕見骨骼發育不良（如 brachyolmia、pseudoachondroplasia 等）。這些預測同樣沒有機轉依據，也沒有臨床證據。

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
| HK-64662 | CACEF 100 DISPERSIBLE TABLETS 100MG | 未提供 | 未提供 |
| HK-59185 | CP 200 TAB 200MG | 未提供 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 78 筆交互作用，以下為部分中度（Moderate）交互作用：
  - 制酸劑與胃酸抑制劑：Famotidine、Ranitidine、Cimetidine、Nizatidine、Omeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole、Rabeprazole、Pantoprazole、Aluminum hydroxide、Calcium carbonate、Magaldrate、Magnesium carbonate/hydroxide/oxide
  - 胺基糖苷類抗生素：Kanamycin、Neomycin
  - 其他：Balsalazide

主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只來自模型分數，沒有臨床試驗、文獻或機轉支持。抗菌藥物用於退化性或遺傳性骨關節疾病，在生物學上缺乏合理性。
- 香港許可證資料沒有適應症與警語資料，安全性評估也無法完成。

**若要推進需要：**
- 從香港衛生署取得並解析仿單（適應症、警語、禁忌症）。
- 從 DrugBank 補充作用機轉 (MOA) 資料。
- 進行文獻與臨床試驗檢索，確認是否有任何前臨床或機轉證據支持骨關節炎方向。
- 若找不到任何生物學依據，建議不再優先投入此預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

