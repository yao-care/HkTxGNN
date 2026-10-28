---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
last_modified_at: 2026-10-23
description: "Fosaprepitant：預測新適應症為腎因性抗利尿不適當症候群（證據等級 L5）。原適應症：許可證未載明"
---

# Fosaprepitant
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

## Fosaprepitant：從（未載明原適應症）到腎因性抗利尿不適當症候群
{: .text-alpha }

## 一句話總結

Fosaprepitant 是 aprepitant 的前驅藥物（NK1 受體拮抗劑）。本次整理的資料中，香港許可證未載明核准適應症文字。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fosaprepitant 是 aprepitant 的前驅藥物，屬於 Substance P/NK1 受體拮抗劑。

NSIAD 是由血管加壓素 V2 受體（AVPR2）功能獲得性突變所致。Substance P/NK1 訊號在此路徑中沒有已知的角色，因此兩者之間**沒有確立的機轉連結**。

TxGNN 的高分只是計算預測，沒有臨床或文獻支持，應視為待驗證的假說，而非可行動的證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68703 | FOSAPREPITANT POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 150MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**：知識圖譜（非仿單文字）記錄與**肝衰竭**有禁忌關聯。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分範例：
  - **嚴重 (Major)**：Eliglustat、Naloxegol
  - **中度 (Moderate)**：Rabeprazole、Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、Cimetidine、Clarithromycin、Pioglitazone、Glimepiride 等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或文獻直接研究 NSIAD，且機轉上缺乏合理連結（NK1 訊號與 AVPR2 路徑無關）。
- 證據等級為 L5。

**若要推進需要：**
- 取得 NK1 拮抗作用與 AVPR2/抗利尿調控之間的機轉或前臨床證據
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補齊作用機轉（MOA）資料
- 若有前臨床訊號，再考慮設計探索性研究

---

**補充說明（其他預測項目）：** 排名前 10 的預測中，僅「視網膜炎 (retinitis)」有 1 篇前臨床文獻（PMID 32058829，小鼠 UVR-B 誘發眼部模型，顯示 fosaprepitant 可阻斷眼部組織 NKR-1 表現），但該模型與感染性或遺傳性視網膜炎不同，僅屬標靶作用證據。其餘項目（肺囊蟲症、痲瘋病、隱球菌腦膜炎、多發性內分泌腫瘤、顱內膿瘍、惡性瘧疾、包蟲症、高精胺酸血症）皆無試驗或文獻支持，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

