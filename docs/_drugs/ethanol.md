---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 2
---

# Ethanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ethanol：從（原適應症未載明）到偏頭痛

## 一句話總結

Ethanol（乙醇）在香港以外用消毒/皮膚用溶液形式上市，但本次整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有臨床試驗**，且文獻多指向乙醇是偏頭痛的**誘發因子**而非治療藥物，因此這個預測的可信度低。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。乙醇在香港的許可證多為含酒精的外用溶液（例如與 chlorhexidine 的複方溶液），原適應症也未載入資料中，因此無法建立與偏頭痛之間的藥理關聯。

現有文獻反而指向相反方向：乙醇代謝成乙醛後，會經由 CGRP 受體與 TRPA1 訊號在許旺細胞中引發小鼠眼眶周圍的機械性痛覺過敏（PMID 37101198），這被視為偏頭痛的誘發機轉。另有研究探討 ATP 敏感性鉀通道開啟與腦膜痛覺受器活化的關係（PMID 40785517）。

TxGNN 的高分（99.29%）較可能反映疾病-基因或疾病-路徑層面的關聯，而不是治療訊號。因此預測方向很可能不適合作為藥物再利用的依據。

另一個預測適應症「伴腦幹先兆的偏頭痛 (Migraine with Brainstem Aura)」（分數 99.14%）同樣沒有乙醇專屬的證據；檢索到的文獻多為基因關聯研究，以及其他藥物的試驗。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表僅列與乙醇相關度較高的文獻；多數其他檢索結果為其他藥物或基因研究，與乙醇無直接關係，因此未列入。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | 探討酒精與偏頭痛之間的複雜關係（酒精為已知誘發因子） |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | 前臨床（動物/機轉） | J Biomed Sci | 乙醇的代謝物乙醛經 CGRP 受體與 TRPA1 引發小鼠痛覺過敏，與偏頭痛相關 |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | 基因關聯研究 | Headache | 探討 ADH2 基因多型與偏頭痛風險的關聯 |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | 前臨床（機轉） | Cephalalgia | ATP 敏感性鉀通道開啟會活化腦膜痛覺受器，與偏頭痛起源相關 |
| [42153521](https://pubmed.ncbi.nlm.nih.gov/42153521/) | 2026 | 範圍性回顧 | Drug Alcohol Rev | 探討 CGRP 訊號在酒精使用障礙中的角色 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66686 | CHLORHEXIDINE SOLUTION 2% W/V IN ALCOHOL 70% V/V | 未載明 | 未載明 |
| HK-68185 | CARMUSTINE WAYMADE POWDER AND SOLVENT FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | 未載明 | 未載明 |
| HK-68201 | MARSEPT CUTANEOUS SOLUTION 2% W/V + 70% V/V | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為其中部分範例：
  - **重大 (Major)**：Eluxadoline
  - **中度 (Moderate)**：Acarbose、Albiglutide、Acetohexamide、Alogliptin、乙醯水楊酸 (Aspirin)、Atropine、Bupropion、Canagliflozin、Dapagliflozin 等（多為降血糖藥與抗膽鹼藥）
  - **輕微 (Minor)**：Doxycycline、Cimetidine

其餘警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，沒有任何臨床試驗，且現有機轉研究顯示乙醇是偏頭痛的誘發因子，預測方向很可能相反。
- TxGNN 高分不足以抵消這個反向證據，也找不到乙醇用於偏頭痛的支持性研究。

**若要推進需要：**
- 取得香港衛生署許可證的完整適應症與仿單（警語、禁忌症）
- 補充乙醇的作用機轉資料
- 有任何乙醇治療偏頭痛的人體或前臨床證據，才值得重新評估；否則建議不再投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

