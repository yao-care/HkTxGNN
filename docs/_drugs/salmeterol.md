---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 800
evidence_level: L5
indication_count: 3
monitor_inn: "SALMETEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
last_modified_at: 2026-11-03
description: "Salmeterol：預測新適應症為呼吸道畸形 (respiratory malformation)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Salmeterol
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

## Salmeterol: 呼吸道畸形 (respiratory malformation)
{: .text-alpha }

## 一句話總結

Salmeterol 是一種長效 β2 腎上腺素受體促效劑（吸入型支氣管擴張劑）。
TxGNN 模型預測它可能對**呼吸道畸形 (respiratory malformation)** 有效，
但目前僅有 **2 個間接相關的臨床試驗**，且沒有直接研究此疾病的文獻，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 呼吸道畸形 (respiratory malformation) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 15 張／共 15 張） |
| 許可證數 | 15 張（有效 15 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就藥理類別而言，salmeterol 屬於長效 β2 受體促效劑，可放鬆氣道平滑肌，並可能影響纖毛擺動頻率與氣道清除功能。

這與呼吸道畸形的關聯並不明確。β2 促效劑對纖毛及氣道清除的調節，理論上可能對部分氣道結構或纖毛異常的疾病有幫助，但對畸形本身並無任何實證。TxGNN 的高分較可能反映模型在網路上與氣道疾病的鄰近性，而非具體的作用機轉。

因此，此預測目前應視為待驗證的假說，而非有依據的治療方向。

## 臨床試驗證據

這兩個試驗均未直接研究呼吸道畸形：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | 不適用 | 暫停 | 無資料 | 比較 salmeterol 與 albuterol 或安慰劑長期用於囊狀纖維化，吸入 6 個月；屬間接相關 |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | 不適用 | 完成 | 1 | 孕期氣喘治療與不良妊娠結局；僅 1 人，無療效資料，關注胎兒安全性 |

## 文獻證據

資料中的文獻多為其他呼吸道疾病、一般性回顧或個案報告，並無直接針對呼吸道畸形的研究。與主題最接近的項目如下：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | RCT（資料標示為回顧） | JAMA Pediatrics | 吸入型皮質類固醇單用或合併長效 β2 促效劑，用於早產兒童肺功能下降；非針對畸形 |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | 個案報告 | Arerugi | 原發性纖毛運動不良症病例，曾被當作氣喘治療；非針對畸形 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35936 | SEREVENT INHALER 25MCG/ACTUATION | 資料未載明 | 資料未載明 |
| HK-51376 | SEROFLO 125 INHALER | 資料未載明 | 資料未載明 |
| HK-51378 | SEROFLO 50 INHALER | 資料未載明 | 資料未載明 |
| HK-48128 | SERETIDE INHALER 25/50 | 資料未載明 | 資料未載明 |
| HK-44735 | SERETIDE ACCUHALER 50MCG/250MCG | 資料未載明 | 資料未載明 |

目前香港共有 15 張有效許可證，皆為上市中；以上僅列出前 5 張。

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆潛在交互作用，主要包括：
  - 重大：Clarithromycin
  - 中度：Acarbose、Isometheptene、Famotidine、Epinephrine、Canagliflozin、Dapagliflozin、Empagliflozin 等
  - 輕微：Hydrocortisone、Triamcinolone、Dexamethasone、Budesonide 等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測分數，兩個相關試驗均與呼吸道畸形無直接關係，且沒有直接研究此疾病的文獻，證據等級為 L5。
- 作用機轉的連結薄弱，不足以支持進一步投入。

**若要推進需要：**
- 從呼吸道畸形的疾病生物學出發，建立具體的機轉假說
- 取得 salmeterol 完整的作用機轉資料
- 取得香港仿單的警語與禁忌症資料
- 先進行臨床前或小型探索性研究，確認是否有任何療效訊號

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

