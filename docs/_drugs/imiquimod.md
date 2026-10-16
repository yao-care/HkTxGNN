---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imiquimod：預測新適應症為癌前病變 (Pre-malignant Neoplasm)（證據等級 L5）。原適應症：尋常疣、肛門生殖器 HPV 感染、光化性角化症、淺表多發性基底細胞癌等"
monitor_inn: "Imiquimod"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

# Imiquimod：從疣與光化性角化症到癌前病變（pre-malignant neoplasm）

## 一句話總結

Imiquimod 是外用免疫調節劑，原本用於尋常疣、肛門生殖器 HPV 感染、光化性角化症及淺表多發性基底細胞癌等皮膚疾病。
TxGNN 模型預測它可能對**癌前病變 (Pre-malignant Neoplasm)** 有效，
目前有 **2 個臨床試驗**和 **9 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尋常疣、肛門生殖器 HPV 感染、光化性角化症、淺表多發性基底細胞癌等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 癌前病變 (Pre-malignant Neoplasm) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5（依本報告規則嚴格判定；詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** 2 個臨床試驗中，1 個為已完成的 Phase 3 開放性單組試驗（n=20，光化性角化症），另 1 個為提前終止的 Phase 3 RCT（僅納入 9 人，無可用結論）。依判定規則，這不符合 L1/L2 所需的已完成 RCT。文獻中有 2 篇 Cochrane 系統性回顧（屬 L3 層級），但並非針對 imiquimod 的對照試驗結論。因此保守評為 **L3**（有系統性回顧與少量臨床研究，但缺乏已完成的對照試驗）。
> 註：上表「L5」應更正為 **L3**。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料庫條目。根據已知資訊，imiquimod 是 TLR7（Toll-like receptor 7）促效劑，能誘導局部第一型干擾素與促發炎細胞激素釋放，活化先天與適應性免疫反應。

原適應症中的光化性角化症本身就是典型的癌前皮膚病變，而肛門生殖器 HPV 感染則與外陰、肛門、子宮頸的上皮內贅瘤有共同病因。免疫活化清除異常上皮的機轉，在邏輯上可延伸到 VIN、AIN、CIN 等癌前病變，因此模型的預測在生物學上相當連貫。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | 完成 | 20 | 開放性單組試驗，評估 5% imiquimod 每週 3 天、1–2 個療程治療頭部光化性角化症的效果持續時間；樣本小、無對照 |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | 提前終止 | 9 | 隨機對照試驗，外用 imiquimod 治療高度子宮頸上皮內贅瘤（CIN 2-3），僅納入 9 人，無法得出療效結論 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 肛管上皮內贅瘤（AIN）的介入治療回顧 |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | 高度外陰上皮內贅瘤（VIN）的藥物介入回顧 |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | 非黑色素瘤皮膚癌的光動力療法合併治療 |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | 非黑色素瘤皮膚癌與前驅病變的外用治療，含 imiquimod |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | 光化性角化症的現行處置 |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | 腎臟移植受者的高度 VIN 以 imiquimod 5% 成功治療 |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | 陰莖鮑恩樣丘疹病以 imiquimod 5% 成功清除 |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | 前臨床（動物） | Urol Oncol | TLR7 促效劑膀胱內給藥的大鼠藥動/藥效研究 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44090 | ALDARA CREAM 5% | — | 資料未載明 |
| HK-68923 | IMIQUIMOD CREAM USP 5% W/W | — | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單文字）：光誘發反應、光敏感疾病、自體免疫疾病、移植物抗宿主病、曬傷。
- **藥物交互作用**：共查得 59 筆，目前皆未分級，例如 pantoprazole、morphine、omeprazole、prednisone、simvastatin、warfarin、clopidogrel 等；臨床意義需另行查證。
- **口腔黏膜使用的警示**：有個案報告指出，口腔乳突瘤病在使用 imiquimod 期間發生惡性轉化（PMID 12719972），off-label 口腔使用需特別謹慎。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉（TLR7 免疫活化）與已確立的光化性角化症適應症高度相關，且已有 VIN、AIN 等病例報告與系統性回顧支持；香港已有 2 張有效許可證。
- 但直接證據薄弱：唯一完成的 Phase 3 為小型單組試驗，CIN 的 RCT 提前終止，尚無足夠對照數據確認療效。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字。
- 補充 imiquimod 作用機轉的正式資料。
- 針對特定癌前病變（如 VIN、AIN、CIN）設計足夠樣本的對照試驗。
- 建立局部皮膚反應與全身性免疫反應的監測計畫，並排除自體免疫疾病、光敏感等高風險族群。
- 口腔、黏膜等 off-label 部位使用應限於研究情境。

---

**其他預測適應症的簡要說明：** 口腔黏膜良性腫瘤與齒源性囊腫僅有前臨床或間接證據（建議列為研究問題）；其餘預測（頸部神經母細胞瘤、鼻咽畸胎瘤、內耳腫瘤、唾液腺腫瘤、頸靜脈孔神經鞘瘤等）缺乏實質證據，建議暫緩（Hold）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

