---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosaprepitant：預測新適應症為腎因性抗利尿不適當症候群 (nephrogenic syndrome of inappropriate antidiuresis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia"]
---

# Fosaprepitant
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

# Fosaprepitant：從（原適應症未載明）到腎因性抗利尿不適當症候群

## 一句話總結

Fosaprepitant 是 aprepitant 的前驅藥物（prodrug），屬於 NK1 受體拮抗劑，香港已有上市許可證，但本報告所彙整的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (nephrogenic syndrome of inappropriate antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載。根據已知藥理，Fosaprepitant 是 aprepitant 的前驅藥物，作用為阻斷 substance P/神經激肽-1 (NK1) 受體。一個可能但未經證實的連結是：下視丘與腦幹的 NK1 訊號可能調節血管加壓素（vasopressin）的釋放與水分平衡。

然而，NSIAD 的成因是血管加壓素 V2 受體（AVPR2）的功能增強型突變，作用位置在血管加壓素釋放的下游。因此 NK1 拮抗作用理論上無法矯正這個根本缺陷，機轉上的合理性有限。

0.999 的高分是模型預測結果，並無臨床試驗或文獻佐證，應審慎解讀。

其他排名較前的預測（肺囊蟲病、痲瘋病、隱球菌腦膜炎、多發性內分泌腫瘤）同樣只有模型預測，也沒有明確的機轉依據，且都沒有試驗或文獻支持。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68703 | FOSAPREPITANT POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 150MG | 輸注用濃縮液粉劑（依品名） | 資料未載明 |

## 安全性考量

- **知識圖譜標示的疾病禁忌**：肝衰竭（liver failure）。此資料來自 TxGNN 知識圖譜（PrimeKG）的藥物—疾病關聯，並非仿單內容。
- **藥物交互作用**：共查得 100 筆交互作用。其中列為**重大 (Major)** 的有 Eliglustat、Naloxegol；**中度 (Moderate)** 的包括 Rabeprazole、Lansoprazole、Cimetidine、Clarithromycin、Miconazole、Dexamethasone、Hydrocortisone、Betamethasone、Budesonide、Triamcinolone、Pioglitazone、Saxagliptin、Glimepiride、Nateglinide、Alosetron、Dronabinol、Naldemedine 等。
- Fosaprepitant 為中度 CYP3A4 抑制劑，若用於需合併多種藥物的族群（例如抗黴菌藥物），須特別留意交互作用。

主要警語與仿單禁忌症資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數支持，沒有臨床試驗或文獻，證據等級為 L5。
- 首位預測 NSIAD 的病因在 V2 受體下游，與 NK1 拮抗的機轉不相符。
- 仿單的警語與禁忌症資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 針對 NSIAD 進行文獻與臨床試驗的系統性檢索，並評估 NK1 拮抗劑與血管加壓素 V2 受體路徑的前臨床證據
- 若仍要探索，優先進行前臨床或機轉驗證，並考量肝功能不全族群的風險與交互作用管理
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

