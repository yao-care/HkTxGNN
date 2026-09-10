---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 5
---

# Pioglitazone
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

# Pioglitazone：適應症資料缺口下的多項罕見疾病老藥新用推論

## 一句話總結

Pioglitazone（DrugBank DB01132）目前於香港**未上市**，且原始適應症與作用機轉資料尚未補齊。
TxGNN 模型本輪針對 5 個候選適應症給出高分預測，排名第一為**Opsismodysplasia（骨骼發育不良症）**（預測分數 99.59%），
但**5 項候選均無任何臨床試驗或文獻佐證**，證據等級全數為 L5，屬純模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（未提供，見 DG001/DG002） |
| 預測新適應症 | Opsismodysplasia（排名第一，另有 4 項同批候選） |
| TxGNN 預測分數 | 99.59%（rank 1，opsismodysplasia） |
| 證據等級 | L5（全部 5 項候選皆為 L5，僅模型預測、無臨床/文獻佐證） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Pioglitazone 詳細的作用機轉（MOA）正式資料（DG002，High severity）。不過本次證據包中各候選適應症的機轉推論文字均一致指出，Pioglitazone 為 **PPAR-γ 促效劑**，此為其藥理分類中已知的共通線索。

以排名最高的 opsismodysplasia 為例，該病由 INPPL1（SHIP2）基因突變導致，PPAR-γ 在成骨/脂肪細胞分化平衡中雖有調控角色，但與 INPPL1 路徑僅存在間接、非特異性交集，缺乏直接機轉證據。其餘候選（stiff person syndrome 家族、thiamine-responsive dysfunction syndrome）同樣僅有理論層級的間接連結，主要病理（自體免疫/GABA 傳導異常、粒線體能量代謝異常）均未見與 PPAR-γ 路徑的直接分子對應。

相對而言，排名第五的 **drug-induced localized lipodystrophy** 機轉關聯性最高：PPAR-γ 是脂肪細胞分化的主調控因子，thiazolidinediones 類藥物已知會誘發皮下脂肪重新分布，且 PPAR-γ 突變本身即為部分家族性脂肪失養症的致病機轉。即便如此，這仍屬機轉合理、但完全無臨床驗證的推論層級。

## 其他預測候選（同批評估）

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策階段 |
|------|--------|-----------|---------|---------|
| 1 | Opsismodysplasia | 99.59% | L5 | Hold |
| 2 | Focal stiff limb syndrome | 99.50% | L5 | Hold |
| 3 | Classic stiff person syndrome | 99.50% | L5 | Hold |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | L5 | Hold |
| 5 | Drug-induced localized lipodystrophy | 99.30% | L5 | Hold |

## 臨床試驗證據

目前無相關臨床試驗登記（5 項候選皆查無 ClinicalTrials.gov / ICTRP 紀錄）。

## 文獻證據

目前無相關文獻（5 項候選皆查無 PubMed 紀錄）。

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA/香港仿單警語與禁忌尚未取得，列為 Blocking 資料缺口 DG001）

## 結論與下一步

**決策：Hold**

**理由：**
- 5 項候選適應症證據等級均為 L5，無任何臨床試驗或文獻支持，機轉連結亦多屬間接推論。
- 該藥物於香港未上市，且原廠仿單警語/禁忌（DG001，Blocking）與作用機轉（DG002，High）皆為缺口，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌資料（DG001）
- 透過 DrugBank API 或其他來源補齊 Pioglitazone 完整作用機轉（DG002）
- 針對至少一項候選適應症（建議優先 drug-induced localized lipodystrophy，機轉關聯性相對最高）補強臨床或文獻證據
- 確認香港上市與許可證登記現況
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

