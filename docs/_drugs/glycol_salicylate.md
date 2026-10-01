---
layout: default
title: Glycol Salicylate
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Glycol Salicylate
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

# Glycol salicylate：從外用止痛到 Glanzmann 血小板無力症

## 一句話總結

Glycol salicylate（水楊酸羥乙酯）是外用水楊酸類成分，在香港以止痛貼布等產品上市。
TxGNN 模型預測它可能對 **Glanzmann 血小板無力症 (Glanzmann thrombasthenia)** 有效。
目前**沒有臨床試驗和文獻**支持，且機轉分析顯示這個預測很可能方向相反，較可能加重出血。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症文字；從產品名稱判斷為外用止痛貼布（肌肉關節疼痛） |
| 預測新適應症 | Glanzmann 血小板無力症 (Glanzmann thrombasthenia) |
| TxGNN 預測分數 | 98.17% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知資訊，水楊酸類藥物會抑制 COX-1，減少血栓素 A2 依賴的血小板聚集。Glycol salicylate 作為外用水楊酸酯，主要用於局部止痛與抗發炎。

Glanzmann 血小板無力症是 GPIIb/IIIa 缺失或功能異常引起的出血性疾病。抗血小板作用預期會**加重出血，而不是治療疾病**。模型的高分很可能反映的是知識圖譜中與血小板生物學的鄰近關係，而不是治療方向。

因此，**這個預測在機轉上不合理**，不建議視為有效的老藥新用候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 13 張許可證，以下列出 5 張主要許可證。資料中的劑型與核准適應症欄位皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66114 | FORTOCOOL PAIN PATCH | FP HEALTHCARE LIMITED |
| HK-56055 | PANADOL PAIN RELIEF PATCH | HALEON HONG KONG LIMITED |
| HK-38738 | SALONSIP PLASTER | HISAMITSU PHARMACEUTICAL (HONG KONG) CO., LIMITED |
| HK-59071 | MENTHOLATUM DEEP COLD PATCH | MENTHOLATUM (ASIA PACIFIC) LIMITED |
| HK-66949 | KORI AFTER HAP F HOT PATCH | MING TAI PHARMACEUTICALS COMPANY O/B SURE BRILLIANT INDUSTRIAL LIMITED |

## 安全性考量

- **機轉層面的顧慮**：水楊酸類的抗血小板作用可能加重出血傾向。對 Glanzmann 血小板無力症這類血小板功能缺陷疾病，這是主要風險。
- **藥物交互作用**：DrugBank 查無交互作用資料。

香港衛生署仿單的警語與禁忌症資料尚未取得，其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測沒有任何臨床試驗或文獻支持，僅為 L5 模型預測。
- 機轉上，抗血小板作用與這個出血性疾病的治療方向相反，且外用製劑的全身暴露量低。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料（目前是阻斷性資料缺口，無法進入安全性篩選）。
- 補齊 DrugBank 的作用機轉資料。
- 若仍想探索，建議轉向排名第 2 的「自體免疫疾病 (autoimmune disease)」（分數 98.16%，L4）。1995 年有一篇 hydroxyethylsalicylate 凝膠用於風濕性疾病的臨床研究（PMID [7759034](https://pubmed.ncbi.nlm.nih.gov/7759034/)），一項雙盲多中心試驗（113 位非關節性風濕背痛患者）顯示止痛效果優於安慰劑。
- 該研究反映的是症狀緩解，不是免疫調節，且研究設計與納入疾病需再確認。這個方向目前只能列為研究問題（Research Question），不是推薦候選。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

